import arcpy

# Set workspace
arcpy.env.workspace = r'C:\Users\Jordan\Desktop'

# Create GDB
folder_path = r'C:\Users\Jordan\Desktop\Lab 4'
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

# Create garage feature from CSV
csv_path = r'C:\Users\Jordan\Desktop\Lab 4\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

# Export XY layer to GDB
input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# Copy building feature from campus GDB
campus = r'C:\Users\Jordan\Desktop\Lab 4\campus.gdb'
buildings_campus = campus + r'\Structures'
buildings = gdb_path + r'\Buildings'
arcpy.Copy_management(buildings_campus, buildings)

# Reproject garage points to buildings CRS
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + r'\Garage_Points_reprojected', spatial_ref)

# Buffer garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + r'\Garage_Points_reprojected', gdb_path + r'\Garage_Points_buffered', 150)

# Intersect buffered garages with buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + r'\Garage_Building_Intersection', 'ALL')

# Export to CSV
arcpy.TableToTable_conversion(gdb_path + r'\Garage_Building_Intersection.dbf', r'C:\Users\Jordan\Desktop\Lab 4', 'nearbyBuildings.csv')