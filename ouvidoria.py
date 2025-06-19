from operacoesbd import *


# Função para excluir uma manifestação pelo código informado
def excluirManifestacao(conexao):
    codigoExcluir = int(input("Digite o código da manifestação que deseja excluir: "))
    excluir = 'delete from ouvidoria where codigo = (%s)'
    lista = [codigoExcluir]
    exclusao = excluirBancoDados(conexao, excluir, lista)

    if exclusao == 1:
        print("\nA manifestação foi excluída com sucesso.")
    elif exclusao == 0:
        print("\nNão há manifestações com este código para serem apagadas.")


# Função para pesquisar uma manifestação específica pelo código
def pesquisarManifestacoes(conexao):
    consulta = int(input("Digite o código da manifestação que deseja visualizar: "))
    pesquisar = 'select * from ouvidoria where codigo = %s'
    lista = [consulta]
    consultar = listarBancoDados(conexao, pesquisar, lista)

    if len(conexao) == 0:
        print("\nNão há manifestações disponíveis com este código.\n")
    else:
        print("\nCódigo:", consultar[0][0], "| Nome:", consultar[0][1])
        print("Manifestação:", consultar[0][3])
        print()


# Função para exibir a quantidade total de manifestações
def contadorManifestacoes(conexao):
    contador = 'select count(*) from ouvidoria'
    listar = listarBancoDados(conexao, contador)
    print("\nA quantidade de manifestações disponíveis é:", listar[0][0])
    print()


# Função para criar um elogio
def criarManifestacao(conexao,tipo):
    nome = input("Digite seu nome: ")
    manifestacao = input("Descreva sua manifestação: ")
    sql = 'insert into ouvidoria(nomeusuario, tipomanifestacao, manifestacao) values (%s, %s, %s)'
    dados = [nome, tipo, manifestacao]
    insertNoBancoDados(conexao, sql, dados)
    print("\nManifestação adicionada com sucesso!\n")



# Função para listar todas as manifestações
def listarTodos(conexao):
    sql = 'select * from ouvidoria'
    resultados = listarBancoDados(conexao, sql)

    if len(resultados) == 0:
        print("\nNão há manifestações a serem exibidas.\n")
    else:
        print("\nTodas as manifestações:\n")
        for item in resultados:
            print(item[0], "|", item[1])
        print()


# Função para listar apenas os elogios
def listarManifestacao(conexao,tipoManifestacao):
    sql = 'select * from ouvidoria where tipomanifestacao = (%s)'
    manifestacao = [tipoManifestacao]
    resultados = listarBancoDados(conexao, sql,manifestacao)

    if len(resultados) == 0:
        print("\nNão há manifestações de elogio a serem exibidas.\n")
    else:
        print("\nManifestações:\n")
        for item in resultados:
            print(item[0], "|", item[1])
        print()

