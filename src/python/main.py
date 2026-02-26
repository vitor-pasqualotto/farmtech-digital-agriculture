from menu import exibir_menu
from dados import dados
from calculos_area import area_retangulo, area_trapezio
from manejo_insumos import calcular_insumo

def main():
    while True:
        opcao = exibir_menu()

        if opcao == "1":    
            cultura = input("Digite a cultura (Milho/Café)").strip().lower()

            if cultura == "milho":
                base = float(input("Base do terreno (m): "))
                altura = float(input("Altura do terreno (m): "))
                area = area_retangulo(base, altura)

            elif cultura == "café":
                base_maior = float(input("Base maior (m): "))
                base_menor = float(input("Base menor (m): "))
                altura = float(input("Altura (m): "))
                area = area_trapezio(base_maior, base_menor, altura)

            else: 
                print("Cultura inválida!")
                continue

            insumo = input("Digite o nome do insumo: ")
            dose = float(input("Dose por m²: "))

            quantidade = calcular_insumo(area, dose)

            plantacao = {
                "cultura": cultura,
                "area": area,
                "insumo": insumo,
                "quantidade": quantidade
            }

            dados.append(plantacao)

            print("Plantação cadastrada com sucesso!")

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