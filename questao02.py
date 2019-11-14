from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
import utils

class Questao02:
    
    def __init__(self):
        self.texto = utils.selecionar_arquivo()
        self.chave_privada_a = utils.obter_chave('chave_privada_A.txt')
        self.gerar_resumo()

    def gerar_resumo(self):
        rsa = RSA.import_key(self.chave_privada_a)
        hash = SHA256.new(bytearray(self.texto, 'utf-8'))
        signature = PKCS1_PSS.new(rsa).sign(hash)
        utils.escrever_arquivo('assinatura.bin', signature)

if __name__ == "__main__":
    q = Questao02()