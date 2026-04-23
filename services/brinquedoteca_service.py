from domain.crianca import Crianca
from domain.emprestimo import Emprestimo
from domain.brinquedo import Brinquedo
from repositories.memory import db

class BrinquedotecaService:
    def criar_crianca(self, id: int, nome: str = "") -> Crianca:
        #regra simples: se já existe, retorna o mesmo
        if not id.strip()
            raise ValueError("id não pode ser vazio")
        
        if id in db.crianca_por_id:
            return db.crianca_por_id[id]
        crianca = crianca(id=id, nome=nome)
        db.crianca_por_id[id] = crianca
        return crianca