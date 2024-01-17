Para convertir el fichero shp (+2 otros dos) originales

pip install geopandas

import geopandas
myshpfile = geopandas.read_file('Partidos_Judiciales.shp')
myshpfile.to_file('myJson.geojson', driver='GeoJSON')

 
Para reducir de tamaño el geojson original (1% es el 1% del tamaño del archivo original)

npm install -g mapshaper
mapshaper myJson.geojson -simplify dp 1% keep-shapes -o format=geojson new.geojson
