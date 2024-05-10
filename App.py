def menu():
    print(f"""
  ____  _ _       __  __             
 |  _ \(_) |     |  \/  |            
 | |_) |_| |_ ___| \  / | __ _ _ __  
 |  _ <| | __/ _ \ |\/| |/ _` | '_ \ 
 | |_) | | ||  __/ |  | | (_| | |_) |
 |____/|_|\__\___|_|  |_|\__,_| .__/ 
                              | |    
                              |_|   
          
    [1] - Cadastrar Receita
    [2] - Visualizar Receita
    [3] - Atualizar Receita
    [4] - Apagar Receita
    [5] - Procurar Receita por País
    [6] - Ver Receitas Favoritas
    [7] - Avaliar Receita      
    [8] - Ver Receita Aleatória  
    [0] - Sair do Progama                      
""")
    
def cadastrar_receita():
    nome_receita = input("\nDigite o nome da receita que deseja cadastrar: ").capitalize()
    pais = input(f"Insira o país da receita {nome_receita}: ").capitalize()
    ingredientes = input(f"Insira os ingredientes usados em {nome_receita}: ").capitalize()
    preparo = input(f"Explique o método de preparo: ").capitalize()

    receita = {
        "nome": nome_receita,
        "pais": pais,
        "ingredientes": ingredientes,
        "preparo": preparo
    }

    with open("receitas.txt", "a") as file:
        for key,value in receita.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")

    print(f"\nA receita '{nome_receita}' foi cadastrada com sucesso!")
    

def visualizar_receitas():
    try:
        with open("receitas.txt", "r") as file:
            receitas = file.readlines()
            numero_receita = 1

            for linha in receitas:
                if linha.startswith("nome:"):
                    print(f"\n== RECEITA {numero_receita}: ==\n")
                    numero_receita += 1
                print(linha, end='')
            if numero_receita == 1:
                print("\nNão há receitas cadastradas no sistema.")
            
    except FileNotFoundError:
        print("O arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")



def atualizar_receita():
    pass

def apagar_receita():
    pass

def procurar_receita_por_pais():
    pass

def ver_receitas_favoritas():
    pass

def avaliar_receita():
    pass

def ver_receita_aleatoria():
    pass


def main():
    menu()
    while True:
        opcao = input("\nEscolha uma das opções do menu: ")
        if opcao == '1':
            cadastrar_receita()
        elif opcao == '2':
            visualizar_receitas()
        elif opcao == '3':
            # atualizar_receita()
            print("deve atualizar receita x")
        elif opcao == '4':
            # apagar_receita()
            print("deve apagar receita x")
        elif opcao == '5':
            # procurar_receita_por_pais()
            print("deve exibir receita x do pais y")
        elif opcao == '6':
            # ver_receitas_favoritas()
            print("deve mostrar lista de receitas favoritas")
        elif opcao == '7':
            # avaliar_receita()
            print("deve avaliar receita x")
        elif opcao == '8':
            # ver_receita_aleatoria()
            print("deve exibir receita aleatoria")
        elif opcao == '0':
            print('Encerrando o programa. Até mais!')
            break
        else:
            print('Opção inválida. Tente novamente.')


main()