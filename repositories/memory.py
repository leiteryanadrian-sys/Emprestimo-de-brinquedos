from typing import Dict
from domain.crianca import Crianca
from domain.brinquedo import Brinquedo
from domain.emprestimo import Emprestimo

class MemoryDB:
    def __init__(self):
        self.crianca_por_id: Dict
        self.brinquedo_por_id: Dict
        self.emprestimo_por_id: Dict

db = MemoryDB()