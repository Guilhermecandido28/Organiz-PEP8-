from Fila import Fila


class FilaPreferencial(Fila):

    def gera_senha(self) -> None:
        self.senha_atual: str = f'Preferencial {self.codigo}'
