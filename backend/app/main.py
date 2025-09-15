
from fastapi import FastAPI
from .routes import auth, players, health, telemetry, ml
from .database import db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='MMA SaaS API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(health.router, prefix='/health')
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(players.router, prefix='/players', tags=['players'])
app.include_router(ml.router, prefix='/ml', tags=['ml'])
app.include_router(telemetry.router, prefix='/telemetry', tags=['telemetry'])

@app.on_event('startup')
async def startup():
    await db.connect()

@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()

@app.get('/')
async def root():
    return {'msg': 'MMA SaaS API'}
