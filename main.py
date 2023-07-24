from Fila import Fila
from fila_normal import FilaNormal
from fila_preferencial import FilaPreferencial

fila_preferencial = FilaPreferencial()
fila_normal = FilaNormal()
fila_preferencial.atualiza_fila()
fila_preferencial.atualiza_fila()
fila_normal.atualiza_fila()


print(fila_preferencial.chama_cliente(5))
print(fila_preferencial.chama_cliente(5))
print(fila_normal.chama_cliente(4))

fila_instancia = Fila()

print(Fila.estatistica("28/04/1997", 28, True))
