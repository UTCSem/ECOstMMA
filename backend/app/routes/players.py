
from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import List, Optional
from ..database import db
from ..models import players
from sqlalchemy import select, insert
router = APIRouter()

class PlayerCreate(BaseModel):
    name: str
    weight: float
    height: float
    style: Optional[str] = None

class PlayerOut(PlayerCreate):
    id: int

@router.post('/', response_model=PlayerOut)
async def create_player(p: PlayerCreate, authorization: Optional[str] = Header(None)):
    query = insert(players).values(name=p.name, weight=p.weight, height=p.height, style=p.style).returning(players.c.id, players.c.name, players.c.weight, players.c.height, players.c.style)
    row = await db.fetch_one(query)
    return dict(row)

@router.get('/', response_model=List[PlayerOut])
async def list_players():
    query = select(players.c.id, players.c.name, players.c.weight, players.c.height, players.c.style)
    rows = await db.fetch_all(query)
    return [dict(r) for r in rows]

@router.get('/{player_id}', response_model=PlayerOut)
async def get_player(player_id: int):
    query = select(players).where(players.c.id == player_id)
    row = await db.fetch_one(query)
    if not row:
        raise HTTPException(404, 'Player not found')
    return dict(row)
