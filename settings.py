from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:1@localhost:5432/postgres")
# connect string for the real database

TEST_DATABASE_URL = env.str(
    "TEST_DATABASE_URL",
    default="postgresql+asyncpg://postgres:1@localhost:5433/postgres_test")
# connect string for the test database


HOST = "localhost"
PORT = 8000
