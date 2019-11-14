from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
import utils
import base64

class Questao03:
    
    def __init__(self):
        self.texto = utils.selecionar_arquivo()
        
        print('1 - Chave A\n2 - Chave B')
        chave_escolhida = input('Escolha a chave desejada: ')

        if(chave_escolhida == '1'):
            chave_escolhida = 'chave_publica_A.txt'
        else:
            chave_escolhida = 'chave_publica_B.txt'

        self.chave_publica_a = utils.obter_chave(chave_escolhida)
        self.resumo = utils.ler_arquivo('assinatura.bin')
        self.validar()

    def validar(self):
        rsa = RSA.import_key(self.chave_publica_a)
        hash = SHA256.new(bytearray(self.texto, 'utf-8'))
        verifier = PKCS1_PSS.new(rsa)
        if verifier.verify(hash, self.resumo):
            print('Reconhecido')
        else:
            print('Não reconhecido')

if __name__ == "__main__":
    q = Questao03()