from langchain_core.pydantic_v1 import BaseModel,Field
from typing import List


class Instagram(BaseModel):
    titles: List[str] = Field(description="5 Headlines on Instagram", min_items=5,max_items=5)
    content: str = Field(description="The main content of Instagram")