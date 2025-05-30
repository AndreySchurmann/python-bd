from cliente import menu_cliente

def menu_principal():
    print("------------------------------------------------------------")
    print(" Menu --> Programa")
    print("-----------------------------------------------------------")
    print("|              1- Cliente                                   |")
    print("|               2- Categoria                                |")
    print("|                3- Produto                                 |")
    print("|                 4- Usuario                                |")
    print("|                  5- Vendas                                |")
    print("|                   6- Sair do sistema                      |")
    print("|-----------------------------------------------------------|")

    while True :
        opcao= input ("Escolha uma opção:  ")
        
        if opcao =="1":
            menu_cliente()
        
        if opcao =="2":
            print("cadastro de categoria")
        ("opcao --Cadastro de categoria")

        if opcao =="3":
            print("cadastro do Produto")
        ("opcao --Cadastro de Produto")

        if opcao =="4":
            print("cadastro do Usuario")
        ("opcao --Cadastro de Usuario")

        if opcao =="5":
            print("cadastro do Vendas")
        ("opcao --Cadastro de Vendas")

        if opcao == "6":
            print ("Sair do sistema")
            break
        else: ("opcao --Sair do sistema")


if __name__ == "__main__":
    menu_principal()


