import mysql.connector


def inserirDado(dado, tabela, coluna, conexao):
    cursorFuncao = conexao.cursor()
    cursorFuncao.execute(f'insert into {tabela} ({coluna}) values ("{dado}");')

    conexao.commit()


def deletarDado(id, tabela, conexao):
    
    cursorFuncao = conexao.cursor()
    cursorFuncao.execute(f'delete from {tabela} where id= ({dado});')

    conexao.commit()


def selecionarTabela(tabela, conexao):
    cursorFuncao = conexao.cursor()
    cursorFuncao.execute(f'select * from {tabela};')
    for (ident, nome) in cursorFuncao:
        print(f'{ident}    {nome}')

    conexao.commit()


def atualizarDado(dadoNovo, coluna_alterada, tabela, ident, conexao):
    cursorFuncao = conexao.cursor()
    cursorFuncao.execute(
        f'update {tabela} set {coluna_alterada} = "{dadoNovo}" where id= ({ident});')

    conexao.commit()
