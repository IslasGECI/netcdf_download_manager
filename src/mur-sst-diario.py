# Librerías necesarias
import datetime
import urllib.request
import os

# Función para crear folders por cada año
from funciones.datosnetcdf import makeAnualDirs

# La función range excluye el último valor que se le pasa
anios = range(2003,2018)
folderBase = "data/mur-sst-diario/"
# Crea los folders de cada año
makeAnualDirs(folderBase, anios)

print("Iniciando descarga")
for i, anio in enumerate(anios):
    primerDia = datetime.datetime(anio, 1, 1)
    dias = [primerDia + datetime.timedelta(days=x) for x in range(0, 367)]
    for dia in dias:
        linkArchivonc = "https://opendap.jpl.nasa.gov/opendap/allData/ghrsst/data/GDS2/L4/GLOB/JPL/MUR/v4.1/{0}/{1}/{0}{2}{3}090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc.nc4?time[0:1:0],lat[10699:14098],lon[2700:7600],analysed_sst[0:1:0][10699:14098][2700:7600]".format(dia.year,
        dia.strftime("%j"), dia.strftime("%m"), dia.strftime("%d"))
        inicioNombre = linkArchivonc.rfind("/") + 1
        finNombre = linkArchivonc.find(".nc") + 3
        nombreArchivo = "{}/{}/{}".format(folderBase, dia.year, linkArchivonc[inicioNombre:finNombre])
        if not os.path.exists(nombreArchivo):
            try:
                urllib.request.urlretrieve (linkArchivonc, nombreArchivo)
                print("Progreso total {0:.2f}%".format( (dia.day + 365*i)*100/(len(anios) * 365) ), end="\r")
            except:
                # Se terminaron de descargar los datos, este error surgue porque en 2017 aún no estaban completos los datos
                pass
print("Se terminaron de descargar los datos")
