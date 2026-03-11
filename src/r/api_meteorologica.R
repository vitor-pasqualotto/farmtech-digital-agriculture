library(httr)
library(jsonlite)

# Coordenadas de exemplo (Cruzeiro - SP)
latitude <- -22.57
longitude <- -44.97

url <- paste0(
    "https://api.open-meteo.com/v1/forecast?latitude=",
    latitude,
    "&longitude=",
    longitude,
    "&current_weather=true"
)

resposta <- httr::GET(url)

if (httr::status_code(resposta) != 200) {
    cat("Erro ao acessar API.\n")
    quit()
}

texto <- rawToChar(resposta$content)
dados <- jsonlite::fromJSON(texto)

temperatura <- dados$current_weather$temperature
vento <- dados$current_weather$windspeed

cat("===== DADOS METEOROLÓGICOS ATUAIS =====\n")
cat("Temperatura atual:", temperatura, "°C\n")
cat("Velocidade do vento:", vento, "km/h\n")