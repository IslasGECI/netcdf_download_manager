# Librerías necesarias
import datetime
import urllib.request
import os

# Función para crear folders por cada año
from funciones.datosnetcdf import makeAnualDirs

# La función range excluye el último valor que se le pasa
anios = range(2003,2018)
meses = range(1, 13)
folderBase = "data/modis-chl-mensual/"
# Crea los folders de cada año
makeAnualDirs(folderBase, anios)

print("Iniciando descarga")
for i, anio in enumerate(anios):
    for j, mes in enumerate(meses):
        dia = datetime.datetime(anio, mes, 1)
        if mes < 12:
            mesproximo = datetime.datetime(anio, mes + 1, 1)
            diaFinMes =  int(mesproximo.strftime("%j")) - 1
            diaFinMes = "{0:0=3d}".format(diaFinMes)
        else:
            diaFinMes = datetime.datetime(anio, 12, 31).strftime("%j")
        linkArchivonc = "https://opendap.jpl.nasa.gov/opendap/hyrax/allData/modis/L3/aqua/chlA/v2014.0/4km/monthly/{0}/A{0}{1}{0}{2}.L3m_MO_CHL_chlor_a_4km.nc.nc4?chlor_a[935:1751][647:1823],lat[935:1751],lon[647:1823]".format(dia.year,
        dia.strftime("%j"), diaFinMes)
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
print("Se terminaron de descargar los datos")
