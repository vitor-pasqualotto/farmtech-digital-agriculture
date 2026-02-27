from menu import exibir_menu
from calculos_area import area_retangulo, area_trapezio
from manejo_insumos import calcular_insumo

# Vetor que armazenará todas as plantações cadastradas
dados = []

def criar_dados():
    # Pede para o usuário o tipo de cultura
    cultura = input("\nDigite a cultura (Milho/Café): ").strip().lower()

    # Milho utiliza a área de um retângulo 
    if cultura == "milho":
        base = float(input("Base do terreno (m): "))
        altura = float(input("Altura do terreno (m): "))
        # Chama a função para calcular a área
        area = area_retangulo(base, altura)

    # Café utiliza a área de um trapézio 
    elif cultura == "café":
        base_maior = float(input("Base maior (m): "))
        base_menor = float(input("Base menor (m): "))
        altura = float(input("Altura (m): "))
        # Chama a função para calcular a área
        area = area_trapezio(base_maior, base_menor, altura)

    else: 
        print("Cultura inválida!")
        return

    # Pede o insumo
    insumo = input("Digite o nome do insumo: ")
    # Pede a dose do insumo por metro quadrado
    dose = float(input("Dose por m²: "))

    # Chama a função para calcular o insumo
    quantidade = calcular_insumo(area, dose)

    # Cria o objeto para armazenar a nova plantação
    plantacao = {
        "cultura": cultura,
        "area": area,
        "insumo": insumo,
        "quantidade": quantidade
    }

    # Armazena o objeto no vetor
    dados.append(plantacao)

    # Mostra mensagem de sucesso
    print("Plantação cadastrada com sucesso!")

def listar_dados():
    # Verifica se existe alguma plantação cadastrada
    if not dados:
        print("\nNenhuma platação cadastrada.")
        return

    print("\n===== PLANTAÇÕES CADASTRADAS =====")

    # Percorre o vetor mostrando as plantações cadastradas
    for i, plantacao in enumerate(dados):
        print(f"""
            \nÍndice: {i}
            Cultura: {plantacao['cultura']}
            Área: {plantacao['area']:.2f} m²
            Insumo: {plantacao['insumo']}
            Qunatidade necessária: {plantacao['quantidade']:.2f}
        """)

def atualizar_dados():
    # Verifica se existe alguma plantação cadastrada
    if not dados:
        print("\nNenhuma plantação cadastrada para atualizar.")
        return

    # Lista as platações
    listar_dados()

    try:
        # Pede o índice que o usuário deseja atualizar
        indice = int(input("\nDigite o índice da plantação que deseja atualizar: "))

        # Verifica se o índice está correto
        if 0 <= indice < len(dados):

            print("\nEscolha a nova cultura: ")
            print("\n1 - Milho")
            print("2 - Café")

            # Pede a nova cultura
            opcao = int(input("\nOpção: "))

            match opcao:
                # Pede as novas informções para cadastrar milho
                case 1:
                    cultura = "milho"

                    base = float(input("Base do terreno (m): "))
                    altura = float(input("Altura do terreno (m): "))
                    area = area_retangulo(base, altura)

                # Pede as novas informções para cadastrar café
                case 2:
                    cultura = "café"

                    base_maior = float(input("Base maior (m): "))
                    base_menor = float(input("Base menor (m): "))
                    altura = float(input("Altura (m): "))
                    area = area_trapezio(base_maior, base_menor, altura)

                case _:
                    print("\nOpção inválida.")
                    return
            
            # Pede insumo, dose e calcula a quantidade
            insumo = input("Insumo: ")
            dose = float(input("Dose de insumo: "))
            quantidade = calcular_insumo(area, dose)

            # Atualiza a plantação
            dados[indice] = {
                "cultura": cultura,
                "area": area,
                "insumo": insumo,
                "quantidade": quantidade
            }

            # Exibe mensagem de sucesso
            print("\nPlantação atualizada com sucesso.")
        
        else:
            print("\nÍndice inválido.")
            
    except ValueError:
        # Trata o input do usuário, se não for válido exibe mensagem de erro
        print("\nDigite apenas números válidos.")

def deletar_dados():
    # Verifica se existe alguma plantação cadastrada
    if not dados:
        print("\nNenhuma plantação cadastrada para excluir.")
        return

    # Lista as plantações
    listar_dados()

    try:
        # Pede o índice que o usuário deseja excluir
        indice = int(input("\nDigite o índice da plantação que deseja excluir: "))

        # Verifica se o índice está correto
        if 0 <= indice < len(dados):
            # Remove o índice do vetor
            removido = dados.pop(indice)
            # Exibe mensagem de sucesso
            print(f"\nPlantação '{removido['cultura']}' removida com sucesso.")

        else:
            print("\nÍndice inválido.")

    except ValueError:
        # Trata o input do usuário, se não for válido exibe mensagem de erro
        print("\nDigite um número válido.")

def main():
    # Loop para exibir o menu
    while True:
        # Função para mostrar o menu e solicitar uma opção
        opcao = exibir_menu()

        match opcao:
            # Opção de cadastrar nova plantação
            case "1":    
                # Chama função para cadastrar plantação
                criar_dados()

            # Opção para listar platações cadastradas
            case "2":
                # Chama função para listar dados
                listar_dados()

            # Opção para atualizar plantação 
            case "3":
                # Chama função para atualizar dados
                atualizar_dados()

            # Opção para deletar plantação
            case "4":
                # Chama função para deletar dados
                deletar_dados()

            # Opção para sair 
            case "5":
                print("\nSaindo...")
                # Sai do loop
                break

if __name__ == "__main__":
    main()