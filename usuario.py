from conexao import conecta_db
from menu import opcoes_menu

def menu_usuario(titulo):
    opcoes_menu(titulo)

   
    while True :
        opcao= input ("Escolha uma opção:  ")
        conexao = conecta_db()
        
        if opcao == "1":
            listar_usuario(conexao)
            opcoes_menu(titulo)
        
        elif opcao == "2":
            listar_usuario(conexao)
            consultar_usuario_por_id(conexao)
            opcoes_menu(titulo)

        elif opcao == "3":
            listar_usuario(conexao)
            inserir_usuario(conexao)
            listar_usuario(conexao)
            opcoes_menu(titulo)

        elif opcao == "4":
            listar_usuario(conexao)
            atualizar_usuario(conexao)
            listar_usuario(conexao)
            opcoes_menu(titulo)

        elif opcao == "5":
            listar_usuario(conexao)
            deletar_usuario(conexao)
            listar_usuario(conexao)
            opcoes_menu(titulo)

        elif opcao == "6":
            print ("Sair")
            break
        else: 
            print("Opcão inválida, tente novamente!")


def login(conexao) -> bool:
      login = input("Digite o login: ")
      senha = input("Digite a senha: ")

      cursor = conexao.cursor()
      sql_listar = """ select id, login, admin from usuario 
                     where login = %s and senha = %s 
                 """ 
      dados = (login,senha)
      cursor.execute(sql_listar, dados)
      registro = cursor.fetchone()

      if registro is None:
            print("Usuario e senha invalidos: ")
            return False
      else:
            admin= registro[2]
            return True
    




    
def listar_usuario(conexao):
    cursor = conexao.cursor()
    sql_listar = """ select id, login, admin from usuario 
                     order by id asc
                 """

    # Execução do select no banco de dados
    cursor.execute(sql_listar)
    #recuperar todos registros
    registros = cursor.fetchall()
    
    for registro in registros:
       print(f"| ID: {registro[0]} - Login: {registro[1]} - Admin: {registro[2]}") 

       

def consultar_usuario_por_id(conexao):
        id= (input ("Digite o ID: "))
        cursor = conexao.cursor()
        cursor.execute("select id,login,admin, from usuario where id = " + id)
        registro = cursor.fetchone()

        if registro is None:
                print("usuario não encontrado")
        else:
                print(f"| ID :             {registro[0]}")
                print(f"| Login :          {registro[1]}")
                print(f"| Admin :          {registro[2]}")
            

def inserir_usuario(conexao):
         print("Inserindo o Usuario ...")
         cursor = conexao.cursor()

         Login = input("Login: ")
         senha = input("Senha: ")
         admin = input("Admin: ")
         
         sql_insert = "insert into usuario (login,senha,admin) values ( %s, %s, %s)"
         dados = (Login,senha,admin)
         cursor.execute(sql_insert, dados)
         conexao.commit()

def atualizar_usuario(conexao):
         print("Alterando dados do usuario")
         cursor = conexao.cursor()

         id    = input("Digite o ID: ")
         Login = input("Login: ")
         senha = input("Nome: ")
         admin = input("Admin: ")       
        
         sql_update = "update produto set Login = %s, senha = %s, id = %s, admin = %s where id = %s" 
         dados = (Login,senha,id,admin)

         cursor.execute(sql_update,dados)
         conexao.commit()

def deletar_usuario(conexao):
         print("Qual usuario deseja deletar? ")
         cursor = conexao.cursor()
         id = input("Digite o ID : ")
         sql_delete = "delete from usuario where id = " +id
         cursor.execute(sql_delete)
         conexao.commit()   
    