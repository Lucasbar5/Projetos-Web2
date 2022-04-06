from typing import List, Optional
from pydantic import BaseModel, ValidationError

class Aluno_validation(BaseModel):
    id: int
    nome: str
    matricula: int
    semestre: int