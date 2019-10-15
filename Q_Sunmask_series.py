from PyQt5.QtCore import QFileInfo, QSettings, QVariant
from qgis.core import *
import qgis.utils
import os, glob, processing, string, time, shutil

MDT = iface.activeLayer()
Output = "C:/Users/cac/GoogleDrive/GitHub/MegaTools/Q_Sunmask_series/output/"
Fecha = "20190320"
SunriseSunset = "0630_2200"
CadaMin = 60

rasterext = MDT.extent()
xmin = rasterext.xMinimum()
xmax = rasterext.xMaximum()
ymin = rasterext.yMinimum()
ymax = rasterext.yMaximum()
extension = "%f,%f,%f,%f" %(xmin, xmax, ymin, ymax)

#generar parametros para sunmask (ints a partir de los strings de entrada)
AAAA=int(Fecha[0:4])
MM=int(Fecha[4:6])
DD=int(Fecha[6:8])
HHi=int(SunriseSunset[0:2])
HHf=int(SunriseSunset[5:7])
HH=range(HHi,HHf)
mm=range(0,60,CadaMin)

for H in HH:
	for m in mm: 
		nfile = str(Output+'/'+'S_'+Fecha+'_'+str(H).zfill(2)+str(m).zfill(2)+'.tif')
		print("Procesando :" + str(nfile))
		processing.run("grass7:r.sunmask.datetime", {
			'elevation':MDT,
			'year':AAAA,
			'month':MM,
			'day':DD,
			'hour':H,
			'minute':m,
			'second':0,
			'timezone':0,
			'east':xmin,
			'north':ymin,
			'-z':True,
			'-s':False,
			'output':nfile,
			'GRASS_REGION_PARAMETER':None,
			'GRASS_REGION_CELLSIZE_PARAMETER':0,
			'GRASS_RASTER_FORMAT_OPT':'',
			'GRASS_RASTER_FORMAT_META':''})