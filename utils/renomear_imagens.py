import os
import shutil

def renomear_e_mover_imagens(pastas, destino):
    i = 1  # Inicializa o contador para renomeação
    # Cria a pasta de destino caso ela não exista
    if not os.path.exists(destino):
        os.makedirs(destino)
    
    for pasta in pastas:
        # Verifica se a pasta existe
        if os.path.exists(pasta) and os.path.isdir(pasta):
            for arquivo in os.listdir(pasta):
                # Verifica se o arquivo é uma imagem (com base na extensão)
                if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    # Caminho completo do arquivo original
                    caminho_antigo = os.path.join(pasta, arquivo)
                    
                    # Novo nome para a imagem
                    novo_nome = f"imagem_{i}{os.path.splitext(arquivo)[1]}"
                    caminho_novo = os.path.join(destino, novo_nome)
                    
                    # Copia e renomeia a imagem para a nova pasta
                    shutil.copy(caminho_antigo, caminho_novo)
                    print(f"Imagem {arquivo} copiada para {caminho_novo}")
                    
                    i += 1  # Incrementa o contador

# Exemplo de uso
pastas = ['nao_emissoes_2']  # Lista de pastas com as imagens
destino = 'nao_emissoes_imagens'  # Pasta onde as imagens renomeadas serão salvas
renomear_e_mover_imagens(pastas, destino)
