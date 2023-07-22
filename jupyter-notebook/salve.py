import os
import csv
from datetime import datetime

def run():

    def criar_pasta(caminho):
        try:
            os.makedirs(caminho)
        except FileExistsError:
            print("A pasta já existe.")
        except Exception as e:
            print(f"Erro ao criar a pasta: {str(e)}")

    def salvar_arquivo(destino, nome_arquivo, conteudo):
        try:
            with open(os.path.join(destino, nome_arquivo), 'w', newline='') as arquivo:
                writer = csv.writer(arquivo)
                writer.writerows(conteudo)
            print(f"Arquivo salvo em {os.path.join(destino, nome_arquivo)}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {str(e)}")

    def ler_arquivo_csv(caminho):
        try:
            with open(caminho, 'r') as arquivo:
                leitor = csv.reader(arquivo)
                conteudo = list(leitor)
            return conteudo
        except Exception as e:
            print(f"Erro ao ler o arquivo: {str(e)}")
            return None

    def main():
        caminho_arquivo = 'C:/Users/ON/Desktop/GuitHub/gitHub_2/src/examples/dc-2d/syscal.csv'  # Coloque aqui o caminho do arquivo CSV
        nome_arquivo = os.path.basename(caminho_arquivo)
        data_hora_atual = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_pasta = f"{nome_arquivo}_{data_hora_atual}"
        caminho_pasta = os.path.join(os.path.dirname(caminho_arquivo), nome_pasta)

        criar_pasta(caminho_pasta)
        conteudo_csv = ler_arquivo_csv(caminho_arquivo)
        if conteudo_csv is not None:
            salvar_arquivo(caminho_pasta, nome_arquivo, conteudo_csv)

    if __name__ == "__main__":
        main()

