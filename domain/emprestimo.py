from dataclasses import dataclass

class Emprestimo:
    def __init__(
        self,
        id: int
        crianca_id: int,
        brinquedo_id: int,
        datas: str,
        status: str = "active"
        multa: int,
    ):
        self.id = id
        self.crianca_id = crianca_id
        self.brinquedo_id = brinquedo_id
        self.datas = datas
        self.status = status
        self.multa = multa
    
    def 