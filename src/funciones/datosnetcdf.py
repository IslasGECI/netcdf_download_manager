import datetime
import os
import urllib.request

def makeAnualDirs(direccionBase, anios):    
    for anio in anios:
        if not os.path.exists(direccionBase + str(anio)):
            os.makedirs(direccionBase + str(anio))

def downloasMonthlyData(linkBase, anios, folderBase):
    meses = range(1, 13)
    for i, anio in enumerate(anios):
        for j, mes in enumerate(meses):
            dia = datetime.datetime(anio, mes, 1)
        if mes < 12:
            mesproximo = datetime.datetime(anio, mes + 1, 1)    
            diaFinMes =  int(mesproximo.strftime("%j")) - 1
            diaFinMes = "{0:0=3d}".format(diaFinMes)
        else:
            diaFinMes = datetime.datetime(anio, 12, 31).strftime("%j")       
        linkArchivonc = linkBase.format(dia.year, dia.strftime("%j"), diaFinMes)        
        inicioNombre = linkArchivonc.rfind("/") + 1
        finNombre = linkArchivonc.find(".nc") + 3
        # Se guarda el archivo en la carpeta adecuada
        nombreArchivo =  "{}/{}/{}".format(folderBase, dia.year, linkArchivonc[inicioNombre:finNombre])
        if not os.path.exists(nombreArchivo):
            try:
                urllib.request.urlretrieve (linkArchivonc, nombreArchivo)
            except:
                pass
        print("Progreso total {0:.2f}%".format( (j + 12*i)*100/(len(anios) * len(meses)) ), end="\r")