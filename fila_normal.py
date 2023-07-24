from Fila import Fila


class FilaNormal(Fila):
    def gera_senha(self) -> None:
        self.senha_atual: str = f'Normal {self.codigo}'
