
from databases import Database
import os
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+asyncpg://mma_user:mma_pass@localhost:5432/mma_db')
# databases library expects 'postgresql://', but asyncpg driver is specified in SQLAlchemy connection strings.
# For local development using the docker-compose value, this value should work with SQLAlchemy. Adjust if needed.
db = Database(DATABASE_URL)
