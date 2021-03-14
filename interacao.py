import mysql.connector
from mod import db
import os


banco = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'teste'
}
conexao = mysql.connector.connect(**banco)


if __name__ == '__main__':

    while True:
        os.system('cls')
        print('Menu tabela nomes')
        print('1 - inserir nome')
        print('2 - deletar nome')
        print('3 - mostrar tabela')
        print('4 - atualizar dados')
        print('0 - sair da aplicação')
        escolha = None
        escolha = int(input('Escolha: '))
        if escolha == 1:
            nome = input('Nome: ')
            tabela = input('Tabela: ')
            db.inserirDado(nome, tabela, 'nome', conexao)
        elif escolha == 2:
            dado = input('Dado: ')
            tabela = input('Tabela: ')
            coluna = input('Coluna: ')
            db.deletarDado(dado, tabela, coluna, conexao)
        elif escolha == 3:
            tabela = input('Tabela: ')
            db.selecionarTabela(tabela, conexao)
            x = input('pressione enter para continuar...')
        elif escolha == 4:
            novoDado = input('Novo dado: ')
            coluna_alterada = input('Coluna: ')
            tabela = input('Tabela: ')
            ident = int(input('Id ou Código: '))
            db.atualizarDado(novoDado, coluna_alterada, tabela, ident, conexao)
        elif escolha == 0:
            break
