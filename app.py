import sqlite3

def conexao_banco():
    conexao = sqlite3.connect('contatos.db')

    cursor = conexao.cursor()

    sql = '''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )'''
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    return conexao


def adicionar_contato(nome, telefone, email):
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
    INSERT INTO contatos ('nome', 'telefone', 'email')
    VALUES (?, ?, ?);'''
    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()    
    conexao.close()








def listar_contatos():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
    SELECT * FROM contatos;'''
    cursor.execute(sql)
    contatos = cursor.fetchall()
    conexao.close()

    if len(contatos):
        print("### LISTA DE CONTATOS ###")
        print(f"{'ID':<9} | {'Nome':<21} | {'Telefone':<25} | {'Email':<29}")
        print("-" * 80)
        for contato in contatos:
            print(f"ID: {contato[0]:<5} | Nome: {contato[1]:<15} | Telefone: {contato[2]:<15} | Email: {contato[3]:<30}")
    else:
        print("Nenhum contato encontrado.")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
    SELECT * FROM contatos WHERE nome LIKE ?;'''
    cursor.execute(sql, ('%' + nome + '%',))
    contatos = cursor.fetchall()
    conexao.close()

    if len(contatos):
        print("### RESULTADO DA BUSCA ###")
        print(f"{'ID':<9} | {'Nome':<21} | {'Telefone':<25} | {'Email':<29}")
        print("-" * 80)
        for contato in contatos:
            print(f"ID: {contato[0]:<5} | Nome: {contato[1]:<15} | Telefone: {contato[2]:<15} | Email: {contato[3]:<30}")
    else:
        print("Nenhum contato encontrado com esse nome.")

def atualizar_contato():    
    print("### ATUALIZAR CONTATO ###")
    id_contato = input("Digite o ID do contato que deseja atualizar: ")
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo telefone do contato: ")
    novo_email = input("Digite o novo email do contato: ")

    if not novo_nome and not novo_telefone and not novo_email:
        print("Nenhum dado fornecido para atualização.")
        return
    if not id_contato:
        print("ID do contato não fornecido.")
        return
    if not novo_nome:
        print("Nome do contato não fornecido.")
        return
    if not novo_telefone:
        print("Telefone do contato não fornecido.")
        return
    if not novo_email:
        print("Email do contato não fornecido.")
        return

    sql_update = "UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?"
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute(sql_update, (novo_nome, novo_telefone, novo_email, id_contato))
    conexao.commit()
    conexao.close()


def excluir_contato():
    print("### EXCLUIR CONTATO ###")
    id_contato = input("Digite o ID do contato que deseja excluir: ")
    if not id_contato:
        print("ID do contato não fornecido.")
        return
    sql_delete = "DELETE FROM contatos WHERE id = ?"
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute(sql_delete, (id_contato,))
    conexao.commit()
    conexao.close()

def main():
    menu()






def menu():
    while True:

        print("### CONTATOS ###")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato pelo nome")
        print("4 - Atualizar contato")
        print("5 - Excluir contato")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            adicionar_contato(nome, telefone, email)

        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            atualizar_contato()
        elif opcao == "5":
            excluir_contato()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()