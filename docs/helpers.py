import geopandas as gpd 
import rasterio 


nz = gpd.read_file("../data/nz.gpkg")
nz_height = gpd.read_file("../data/nz_height.gpkg")
world = gpd.read_file("../data/world.gpkg")
cycle_hire = gpd.read_file("../data/../data/cycle_hire.gpkg")
cycle_hire_osm = gpd.read_file("../data/cycle_hire_osm.gpkg")
src_elev = rasterio.open("../output/elev.tif")
src_landsat = rasterio.open("../data/landsat.tif")
src_grain = rasterio.open("../output/grain.tif")
canterbury = gpd.read_file('../data/canterbury.gpkg')
seine = gpd.read_file('../data/seine.gpkg')
us_states = gpd.read_file('../data/us_states.gpkg')
src_dem = rasterio.open('../data/dem.tif')