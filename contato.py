from database import conectar
import re

def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email) is not None

def editar_contato(id_contato, nome, telefone, email):
    if not validar_email(email):
        return False, "E-mail inválido!"

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE contatos
    SET nome = %s,
        telefone = %s,
        email = %s
    WHERE id = %s
    """
    cursor.execute(sql, (nome, telefone, email, id_contato))
    conexao.commit()
    cursor.close()
    conexao.close()
    return True, "Contato atualizado com sucesso!"

def excluir_contato(id_contato):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM contatos WHERE id = %s"
    cursor.execute(sql, (id_contato,))
    conexao.commit()
    
    sucesso = cursor.rowcount > 0
    cursor.close()
    conexao.close()
    return sucesso

def buscar_contato(nome):   
    conexao = conectar()
    # Usando dictionary=True para facilitar a leitura no HTML
    cursor = conexao.cursor(dictionary=True) 

    sql = "SELECT * FROM contatos WHERE nome LIKE %s"
    cursor.execute(sql, (f"%{nome}%",))
    resultados = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    return resultados # Retorna a lista de contatos encontrados

def adicionar_contato(nome, telefone, email):
    if not validar_email(email):
        return False, "E-mail inválido!"

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()
    cursor.close()
    conexao.close()
    return True, "Contato cadastrado com sucesso!"

def listar_contatos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True) # Alterado para dictionary

    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()

    cursor.close()
    conexao.close()
    return contatos # Retorna todos os contatos para o Flask