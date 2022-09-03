""" Script criado com o intuito de facilitar a renomeação
das imagens utilizadas no corpo dos tutoriais """
import os


pasta = input("Digite o nome da pasta (sem a última barra): ").strip()
prefixo = input("Digite o prefixo das imagens: ").strip()
diretorio = f"C:/Users/<NOME_DO_USUARIO>/Downloads/{pasta}/"


def main():

    for _, arquivo in enumerate(os.listdir(diretorio)):
        nome = prefixo + arquivo
        origem = diretorio + arquivo
        destino = diretorio + nome
        os.rename(origem, destino)


main()
