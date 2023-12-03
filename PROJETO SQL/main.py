import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Nzlt@2023",
    "database": "livraria"
}

def editar_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    livros = cursor.fetchall()
    cursor.close()
    conexao.close()
    return livros


while True:
    menu = int(input("""
        Escolha uma opção:
        1 - Inserir Livro
        2 - Ver livros cadastrados
        3 - Editar Livro
        4 - Deletar Livro
        0 - Sair
    """))

    if menu == 1:
        nome_do_livro = str(input("Digite o nome do livro: "))
        genero_do_livro = str(input("Digite o genero do livro: "))
        autor_do_livro = str(input("Digite o autor do livro: "))
        ano_do_livro = int(input("Digite o ano do livro: "))

        editar_banco(f'''INSERT INTO livros
        (id, titulo, genero, autor, ano_publicacao)
        VALUES(
        DEFAULT,
        "{nome_do_livro}",
        "{genero_do_livro}",
        "{autor_do_livro}",
        "{ano_do_livro}");''')
    elif menu == 2:
        print(consultar_banco("SELECT * FROM Livros"))
    elif menu == 3:
        print("...")
    elif menu == 4:
        print(consultar_banco("SELECT * FROM Livros"))
        escolha = int(input("Digite o ID do livro que você quer deletar: "))
        editar_banco(f"DELETE FROM Livro WHERE id = {escolha}")
    elif menu == 0:
        break
    else:
        print("Opção inválida.")
