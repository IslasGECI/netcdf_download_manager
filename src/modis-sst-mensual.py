# Librerías necesarias
import datetime
import urllib.request
import os

# Función para crear folders por cada año
from funciones.datosnetcdf import makeAnualDirs

# La función range excluye el último valor que se le pasa
anios = range(2003,2018)
meses = range(1, 13)
folderBase = "data/modis-sst-mensual/"
# Crea los folders de cada año
makeAnualDirs(folderBase, anios)

print("Iniciando descarga")
for i, anio in enumerate(anios):
    for j, mes in enumerate(meses):
        dia = datetime.datetime(anio, mes, 1)
        if mes < 12:
            mesproximo = datetime.datetime(anio, mes + 1, 1)
            diaFinMes = int(mesproximo.strftime("%d")) - 1
        else:
            diaFinMes = datetime.datetime(anio, 12, 31).strftime("%d")       
        linkArchivonc = f"https://podaac-opendap.jpl.nasa.gov/opendap/allData/modis/L3/aqua/11um/v2019.0/9km/monthly/{dia.year}/AQUA_MODIS.{dia.year}0101_{dia.year}01{diaFinMes}.L3m.MO.SST.sst.9km.nc?lat[lat[599:1:900]],lon[,lon[599:1:960]]"
        print("{} {} {}".format(dia.year, dia.strftime("%j"), diaFinMes))
        #print(linkArchivonc)
        inicioNombre = linkArchivonc.rfind("/") + 1
        finNombre = linkArchivonc.find(".nc") + 3
        nombreArchivo = "{}/{}/{}".format(folderBase, dia.year, linkArchivonc[inicioNombre:finNombre])
        try:
            # Se guarda el archivo en la carpeta adecuada
            if not os.path.exists(nombreArchivo):                
                urllib.request.urlretrieve (linkArchivonc, nombreArchivo)
            print("Progreso total {0:.2f}%".format( (j + 12*i)*100/(len(anios) * len(meses)) ), end="\r")
        except:
            print("Se terminaron de descargar los datos")
            break
