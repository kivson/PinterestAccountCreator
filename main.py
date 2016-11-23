import funcy
import operator

from contas import gerar_contas
from pinterest import criar_conta, seguir_conta

contas = gerar_contas(300, "kivson+teste56{}@gmail.com", 'supersenha@123')

contas_criadas = filter(operator.itemgetter('criado'), map(criar_conta, contas))

me_seguir = funcy.curry(seguir_conta)(['https://br.pinterest.com/kmarcell', 'https://www.pinterest.com/laismeuchi'])

seguindo = map(me_seguir, contas_criadas)

for c in seguindo:
    print(c)
