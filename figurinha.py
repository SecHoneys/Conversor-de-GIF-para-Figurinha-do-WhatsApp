import imageio
import os
import requests

# Pede para o usuário fornecer o URL do GIF
gif_url = input("Digite o URL do GIF: ")

# Faz o download do GIF com a biblioteca requests
response = requests.get(gif_url)
with open("input.gif", "wb") as f:
    f.write(response.content)

# Lê o GIF com a biblioteca imageio
with imageio.get_reader("input.gif") as reader:
    # Define a primeira imagem do GIF como a imagem da figurinha
    sticker_data = reader.get_data(0)
    # Salva a imagem em formato PNG
    imageio.imwrite("output.png", sticker_data)

# Renomeia o arquivo para a extensão .webp para que ele possa ser uma figurinha do WhatsApp
os.rename("output.png", "output.webp")

# Remove o arquivo de entrada
os.remove("input.gif")