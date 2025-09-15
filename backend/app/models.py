
from sqlalchemy import Table, Column, Integer, String, Float, MetaData, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(128), unique=True, nullable=False),
    Column('hashed_password', String(256), nullable=False),
    Column('is_active', Boolean, default=True),
    Column('created_at', DateTime, server_default=func.now())
)

players = Table(
    'players', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=True),
    Column('name', String(200), nullable=False),
    Column('weight', Float),
    Column('height', Float),
    Column('style', String(100)),
    Column('created_at', DateTime, server_default=func.now())
)
