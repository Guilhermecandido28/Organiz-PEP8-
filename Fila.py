class Fila:
    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual = None

    def gera_senha(self) -> None:
        self.senha_atual: str = self.codigo

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0

        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.gera_senha()
        self.reseta_fila()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente {cliente_atual} dirija-se ao caixa: {caixa}'

    @classmethod
    def estatistica(self, dia: str, agencia: int, options: bool = True) -> dict:
        if options:
            estatistica = {}
            estatistica["dia"] = dia
            estatistica["agencia"] = agencia
            estatistica["clientes"] = self.clientes_atendidos
            estatistica["quantidade_clientes"] = len(self.clientes_atendidos)

        else:
            estatistica = {f'No dia {dia} a {agencia} atendeu {len(self.clientes_atendidos)} clientes.'}

        return estatistica
