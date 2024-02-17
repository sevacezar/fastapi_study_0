from typing import Optional

from pydantic import BaseModel


class STasAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STasAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int