from pydantic import BaseModel


class ParseResponse(BaseModel):
    ics: str
