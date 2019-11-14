from Crypto import Random
from Crypto.PublicKey import RSA
import os

class Questao01:
    
    def __init__(self):
        self.gerar_chave('A')
        self.gerar_chave('B')

    def gerar_chave(self, numero):
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)

        chave_publica = key.publickey().export_key().decode()
        chave_privada = key.export_key().decode()

        self.escrever_arquivo(f'chave_publica_{numero}.txt', chave_publica)
        self.escrever_arquivo(f'chave_privada_{numero}.txt', chave_privada)

    def escrever_arquivo(self, nome, texto):
        f = open(nome, 'w+')
        f.write(str(texto))
        f.close()


if __name__ == "__main__":
    q = Questao01()