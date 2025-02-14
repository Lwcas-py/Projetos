#listar todos os arquivos e pastas em um diretorio
import os
import shutil



def organizar():

    org=os.listdir(os.getcwd()) 


    for arquivo in org:

        if os.path.isfile(arquivo):
            nome, extensao=os.path.splitext(arquivo)

            if extensao= ".py"
                os.makedirs(Python, exist_ok=True)

            print("Nome: {}, Extensao:{}".format(nome, extensao))
            #print para checar o codigo
    