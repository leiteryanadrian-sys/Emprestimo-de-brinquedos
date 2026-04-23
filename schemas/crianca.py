from pydantic import BaseModel

class CriancaCreate(BaseModel):
    id: int
    nome: str = ""

class ClienteOut(BaseModel):
    id: int
    nome: str = ""