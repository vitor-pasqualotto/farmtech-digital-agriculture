library(jsonlite)

# Caminho para o JSON exportado pelo python
dados <- fromJSON("../exports/plantacoes.json")

# Verifica se existe dado
if (length(dados) == 0) {
    cat("Nenhum dado encontrado.\n")
    quit()
}

# Extrai colunas
areas <- dados$area
insumos <- dados$quantidade

# Estatísticas da área
media_area <- mean(areas)
desvio_area <- sd(areas)

# Estatísticas do insumo
media_insumo <- mean(insumos)
desvio_insumo <- sd(insumos)

cat("===== ESTATÍSTICAS DAS PLANTAÇÕES =====\n")
cat("Média da área: ", media_area, "\n")
cat("Desvio padrão da área:", desvio_area, "\n")

cat("Média de insumo:", media_insumo, "\n")
cat("Desvio padrão de insumo:", desvio_insumo, "\n")