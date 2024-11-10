from pydantic import BaseModel
from typing import List

class CaseModel(BaseModel):
    id: int
    name: str
    description: str
    steps: List[str]
    expected_result: str
    priority: str
