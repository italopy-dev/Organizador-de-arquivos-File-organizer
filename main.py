import os
import shutil
from settings import documentos, compactados, audios, planilhas, imagens, videos, apresentacoes, executaveis, ebooks, jogos, design, codigos

pasta = input("Digite a pasta que quer organizar(o caminho completo): ")
if not os.path.isdir(pasta):
    print("pasta não encontrada")
    exit()

arquivos = os.listdir(pasta)

def mover(arquivo, nome):
    destino = os.path.join(pasta, nome)

    if not os.path.exists(destino):
        os.mkdir(destino)
    
    inicio = os.path.join(pasta, arquivo)
    
    shutil.move(inicio, destino)

for a in arquivos:
    if not os.path.isfile(os.path.join(pasta, a)):
        continue

    extensao = os.path.splitext(a)[1].lower()

    if extensao in documentos:
        mover(a, "documentos")

    elif extensao in compactados:
        mover(a, "compactados")

    elif extensao in audios:
        mover(a, "áudios")

    elif extensao in planilhas:
        mover(a, "planilhas")

    elif extensao in imagens:
        mover(a, "imagens")

    elif extensao in videos:
        mover(a, "videos")

    elif extensao in apresentacoes:
        mover(a, "apresentações")

    elif extensao in executaveis:
        mover(a, "executáveis")

    elif extensao in ebooks:
        mover(a, "ebooks")

    elif extensao in jogos:
        mover(a, "jogos")

    elif extensao in design:
        mover(a, "designs")

    elif extensao in codigos:
        mover(a, "códigos")



    



            


    




            

    