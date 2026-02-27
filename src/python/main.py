from menu import exibir_menu
from calculos_area import area_retangulo, area_trapezio
from manejo_insumos import calcular_insumo

def main():
    # Vetor que armazenará todas as plantações cadastradas
    dados = []

    # Loop para exibir o menu
    while True:
        # Função para mostrar o menu e solicitar uma opção
        opcao = exibir_menu()

        # Opção de cadastrar nova plantação
        if opcao == "1":    
            # Pede para o usuário o tipo de cultura
            cultura = input("Digite a cultura (Milho/Café)").strip().lower()

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
                continue

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

        # Opção de listar platações cadastradas
        elif opcao == "2":

            # Verifica se existe alguma plantação cadastrada
            if not dados:
                print("\nNenhuma platação cadastrada.")

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