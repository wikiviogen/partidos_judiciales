import geopandas
myshpfile = geopandas.read_file('Partidos_Judiciales.shp')
myshpfile.to_file('myJson.geojson', driver='GeoJSON')
