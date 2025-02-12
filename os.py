import os

os.getcwd()
#retorna o caminho ate o diretorio onde vc esta, em forma de string

os.listdir()
#retorna uma lista contendo todos os arquivos e pastas de onde vc esta

#os.chdir()
#escolhe um diretorio para ser direcionado

os.mkdir('Pasta2')
#cria uma pasta

os.rename('Pasta2', 'Teste')
#renomeia

#os.remove()
#remove arquivos
#rmdir()
#remove diretorios

cmd='date'
os.system(cmd)

os.mkdir("Organizador")