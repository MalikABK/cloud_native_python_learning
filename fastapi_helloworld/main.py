from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from fastapi_helloworld import setting
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, Depends

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)

# only needed for psycopg 3 - replace postgresql 
# with postgresql+psycopg in settings.DATABASE_URL 
connection_string = str(setting.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg" 
)
