from menu import exibir_menu

def main():
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            print("Inserir dados")
        elif opcao == "2":
            print("Listar dados")
        elif opcao == "3":
            print("Atualizar dados")
        elif opcao == "4":
            print("Deletar dados")
        elif opcao == "5":
            print("Saindo do programa...")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()