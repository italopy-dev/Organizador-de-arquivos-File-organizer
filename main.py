from dictionary import dicionario_extensoes
import os
import shutil

def ver_extensoes(caminho):
    separacao = os.path.splitext(caminho)
    extensao = separacao[1]
    return extensao

def checar_arquivo(arquivo, pasta_destino):
    nome = os.path.basename(arquivo)
    if nome in os.listdir(pasta_destino):
        nome_semext = os.path.splitext(arquivo)[0]
        arquivo2 = f"{nome_semext}2{os.path.splitext(arquivo)[1]}"
        os.rename(arquivo, arquivo2)
        return arquivo2  
    return arquivo

def main(pasta):
    for arq in os.listdir(pasta):
        if os.path.isdir(os.path.join(pasta, arq)):
            continue
        caminho_arquivo = os.path.join(pasta, arq)
        aextensao = ver_extensoes(arq)
        for c, v in dicionario_extensoes.items():
            caminho_destino = os.path.join(pasta, c)
            if aextensao in v:
                if not os.path.isdir(caminho_destino):
                    os.mkdir(caminho_destino)
                caminho_arquivo = checar_arquivo(caminho_arquivo, caminho_destino)
                shutil.move(caminho_arquivo, caminho_destino )
                
if __name__ == "__main__":       
    pasta_escolhida = input("digite o caminho da pasta que quer organizar: ")

    if not os.path.isdir(pasta_escolhida):
        print("PASTA NÃO ENCONTRADA")
    main(pasta_escolhida)



    



            


    




            

    