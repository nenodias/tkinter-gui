import zipfile
import os

class Compactador(object):
    def compactar(self, lista_arquivos):
        with zipfile.ZipFile("arquivo.zip", "w") as arquivo_zip:
            for arquivo in lista_arquivos:
            # testa se é arquivo e se o arquivo existe
                if(os.path.isfile(arquivo) and os.path.exists(arquivo)):
                    # pega o nome do arquivo base, sem o diretório
                    base = os.path.basename(arquivo)
                    # passa o diretório e o nome do arquivo a ser gravado
                    arquivo_zip.write(arquivo, base)