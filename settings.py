from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:1@localhost:5432/postgres_test",
)
# connect string for the real database

TEST_DATABASE_URL = env.str(
    "TEST_DATABASE_URL",
    default="postgresql+asyncpg://postgres:1@localhost:5433/postgres_test2",
)
# connect string for the test database


HOST = "localhost"
URL = "https://2cd5ad6b519a32f2d52a6512c0b7c3a8@o4506003606339584.ingest.sentry.io/4506512537354240"

SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
ALGORITHM: str = env.str("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)

APP_PORT = env.int("APP_PORT", default=8000)
SENTRY_URL: str = env.str("SENTRY_URL", default=URL)
