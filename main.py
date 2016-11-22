import operator

from contas import gerar_contas
from pinterest import criar_conta, seguir_conta

contas = gerar_contas(300, "kivson+teste28{}@gmail.com", 'supersenha@123')

contas_criadas = filter(operator.itemgetter('criado'), map(criar_conta, contas))

seguindo = map(lambda c:seguir_conta('https://br.pinterest.com/kmarcell', c), contas_criadas)

for c in seguindo:
    print(c)