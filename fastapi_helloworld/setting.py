from starlette.config import Config
from starlette.datastructures import Secret

try:
    Config = Config(".env")
except FileNotFoundError:
    config =Config()

DATABASE_URL = config("postgresql://postgres:root@localhost:5432/newtodo", cast=Secret)

TEST_DATABASE_URL = config("postgresql://postgres:root@localhost:5432/newtodo",cast=Secret)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                 