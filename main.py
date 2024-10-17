import random
import os
from colorama import Fore

# Função para carregar palavras de arquivos
def carregar_palavras(caminho, arquivo):
    with open(os.path.join(caminho, arquivo), 'r', encoding='utf-8') as f:
        return f.read().splitlines()

# Função para gerar nome e história
def gerar_nome_historia():
    # Caminho para a pasta contendo as listas
    caminho = "listas"
    
    # Carregando as listas de arquivos de texto
    titulo_1 = carregar_palavras(caminho, 't1.txt')
    titulo_2 = carregar_palavras(caminho, 't2.txt')
    titulo_3 = carregar_palavras(caminho, 't3.txt')
    historia_1 = carregar_palavras(caminho, 'h1.txt')
    historia_2 = carregar_palavras(caminho, 'h2.txt')
    historia_3 = carregar_palavras(caminho, 'h3.txt')
    historia_4 = carregar_palavras(caminho, 'h4.txt')
    historia_5 = carregar_palavras(caminho, 'h5.txt')
    historia_6 = carregar_palavras(caminho, 'h6.txt')

    # Gerando título aleatório
    titulo = f"{random.choice(titulo_1)} {random.choice(titulo_2)} {random.choice(titulo_3)}"

    # Gerando história aleatória
    historia = f"{random.choice(historia_1)} {random.choice(historia_2)} {random.choice(historia_3)} {random.choice(historia_4)} {random.choice(historia_5)} {random.choice(historia_6)}."

    # Ajuste da história com base em palavras-chave no título
    if any(word in titulo for word in ["Sombra", "Escuro", "Sombrio", "Abissal"]):
        # Caso o tema seja sombrio ou misterioso
        historia = historia.replace("luz", "sombras").replace("estrelas", "escuridão").replace("ondas", "trevas").replace("chamas", "névoa")
    elif any(word in titulo for word in ["Cristal", "Prata", "Radiante", "Brilhante"]):
        # Caso o tema seja claro ou relacionado a luz
        historia = historia.replace("sombras", "luz").replace("escuridão", "estrelas").replace("trevas", "claridade").replace("névoa", "chamas")
    elif any(word in titulo for word in ["Trovão", "Tempestade", "Chama", "Fogo"]):
        # Caso o tema seja relacionado a tempestades, fogo ou energia
        historia = historia.replace("sombras", "tempestades").replace("ondas", "relâmpagos").replace("névoa", "chamas").replace("trevas", "fogo")
    elif any(word in titulo for word in ["Místico", "Fantasma", "Espectral", "Lendário"]):
        # Tema relacionado a magia, mistério ou fantasia
        historia = historia.replace("cidade", "masmorra").replace("floresta", "reino encantado").replace("caverna", "templo místico")

    # Exibindo o resultado
    
    os.system('cls')
    
    print(Fore.GREEN + f"[+]Título: {titulo}")
    print(Fore.GREEN + f"[+]História: {historia}")

# Gerar nome e história aleatória
gerar_nome_historia()
