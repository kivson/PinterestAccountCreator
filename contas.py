import random
from faker import Factory


def gerar_contas(quantidade, base_email, senha):

    faker = Factory.create('pt_BR')

    for i in range(quantidade):
        yield {
            'email': base_email.format(i),
            'senha': senha,
            'nome_de_usuario': faker.name(),
            'idade_usuario': str(random.randint(19, 50))
        }


def salvar_conta(conta):
    print(conta)