"""

"""

# Fritz Ohrenschall
# LARP743 -- Project Piece
# Take Census Tracts, Break Fields into Deciles, Output As Raster of Given Sizze


# Import necessary modules
import sys, os, string, math, arcpy, numpy

if arcpy.CheckExtension("spatial") == "Available":
	arcpy.CheckOutExtension("spatial")



# Allow output file to overwrite any existing file of the same name
arcpy.env.overwriteOutput = True
    
# User input

tractsBefore = arcpy.GetParameterAsText(0)
fieldBefore  = arcpy.GetParameterAsText(1)
tractsAfter  = arcpy.GetParameterAsText(2)
fieldAfter   = arcpy.GetParameterAsText(3)
Output       = arcpy.GetParameterAsText(4)
spatialRef   = arcpy.GetParameterAsText(5)

# Name Intermediates
tractsBefore2 = tractsBefore[:-4] + "2.shp"
tractsAfter2  = tractsAfter[:-4]  + "2.shp"

# Project
arcpy.Project_management(tractsBefore, tractsBefore2, spatialRef)
arcpy.Project_management(tractsAfter, tractsAfter2, spatialRef)
arcpy.AddMessage("Projected Maps")

# Calculate Decile
arcpy.AddField_management(tractsBefore2, "Decile", "SHORT", 2, 0, "", "", "", "")
arcpy.AddField_management(tractsAfter2, "Decile", "SHORT", 2, 0, "", "", "", "")

#### Quantiles for Before ####
beforeList = []
attributeTableBefore = arcpy.SearchCursor(tractsBefore2)

for nextRecord in attributeTableBefore:
	beforeList.append(float(nextRecord.getValue(fieldBefore)))
	
del nextRecord
del attributeTableBefore

arcpy.AddMessage(beforeList)

beforeList.sort()

arcpy.AddMessage(beforeList)

# List Length
arcpy.AddMessage(len(beforeList))

# Quantile Values
before10 = beforeList[int(round((len(beforeList)/10)*1))]
before20 = beforeList[int(round((len(beforeList)/10)*2))]
before30 = beforeList[int(round((len(beforeList)/10)*3))]
before40 = beforeList[int(round((len(beforeList)/10)*4))]
before50 = beforeList[int(round((len(beforeList)/10)*5))]
before60 = beforeList[int(round((len(beforeList)/10)*6))]
before70 = beforeList[int(round((len(beforeList)/10)*7))]
before80 = beforeList[int(round((len(beforeList)/10)*8))]
before90 = beforeList[int(round((len(beforeList)/10)*9))]

arcpy.AddMessage(before10)
arcpy.AddMessage(before20)
arcpy.AddMessage(before30)
arcpy.AddMessage(before40)
arcpy.AddMessage(before50)
arcpy.AddMessage(before60)
arcpy.AddMessage(before70)
arcpy.AddMessage(before80)
arcpy.AddMessage(before90)

attributeTableBefore = arcpy.UpdateCursor(tractsBefore2)

for nextRecord in attributeTableBefore:
	if nextRecord.getValue(fieldBefore) < before10:
		nextRecord.setValue("Decile",1)
	elif nextRecord.getValue(fieldBefore) < before20:
		nextRecord.setValue("Decile",2)
	elif nextRecord.getValue(fieldBefore) < before30:
		nextRecord.setValue("Decile",3)
	elif nextRecord.getValue(fieldBefore) < before40:
		nextRecord.setValue("Decile",4)
	elif nextRecord.getValue(fieldBefore) < before50:
		nextRecord.setValue("Decile",5)
	elif nextRecord.getValue(fieldBefore) < before60:
		nextRecord.setValue("Decile",6)
	elif nextRecord.getValue(fieldBefore) < before70:
		nextRecord.setValue("Decile",7)
	elif nextRecord.getValue(fieldBefore) < before80:
		nextRecord.setValue("Decile",8)
	elif nextRecord.getValue(fieldBefore) < before90:
		nextRecord.setValue("Decile",9)
	else:
		nextRecord.setValue("Decile",10)
	attributeTableBefore.updateRow(nextRecord)

del nextRecord
del attributeTableBefore

#### Quantiles for After ####
afterList = []
attributeTableAfter = arcpy.SearchCursor(tractsAfter2)

for nextRecord in attributeTableAfter:
	afterList.append(float(nextRecord.getValue(fieldAfter)))
	
del nextRecord
del attributeTableAfter

arcpy.AddMessage(afterList)

afterList.sort()

arcpy.AddMessage(afterList)

# List Length
arcpy.AddMessage(len(afterList))

# Quantile Values
after10 = afterList[int(round((len(afterList)/10)*1))]
after20 = afterList[int(round((len(afterList)/10)*2))]
after30 = afterList[int(round((len(afterList)/10)*3))]
after40 = afterList[int(round((len(afterList)/10)*4))]
after50 = afterList[int(round((len(afterList)/10)*5))]
after60 = afterList[int(round((len(afterList)/10)*6))]
after70 = afterList[int(round((len(afterList)/10)*7))]
after80 = afterList[int(round((len(afterList)/10)*8))]
after90 = afterList[int(round((len(afterList)/10)*9))]

arcpy.AddMessage(after10)
arcpy.AddMessage(after20)
arcpy.AddMessage(after30)
arcpy.AddMessage(after40)
arcpy.AddMessage(after50)
arcpy.AddMessage(after60)
arcpy.AddMessage(after70)
arcpy.AddMessage(after80)
arcpy.AddMessage(after90)

attributeTableAfter = arcpy.UpdateCursor(tractsAfter2)

for nextRecord in attributeTableAfter:
	if nextRecord.getValue(fieldAfter) < after10:
		nextRecord.setValue("Decile",1)
	elif nextRecord.getValue(fieldAfter) < after20:
		nextRecord.setValue("Decile",2)
	elif nextRecord.getValue(fieldAfter) < after30:
		nextRecord.setValue("Decile",3)
	elif nextRecord.getValue(fieldAfter) < after40:
		nextRecord.setValue("Decile",4)
	elif nextRecord.getValue(fieldAfter) < after50:
		nextRecord.setValue("Decile",5)
	elif nextRecord.getValue(fieldAfter) < after60:
		nextRecord.setValue("Decile",6)
	elif nextRecord.getValue(fieldAfter) < after70:
		nextRecord.setValue("Decile",7)
	elif nextRecord.getValue(fieldAfter) < after80:
		nextRecord.setValue("Decile",8)
	elif nextRecord.getValue(fieldAfter) < after90:
		nextRecord.setValue("Decile",9)
	else:
		nextRecord.setValue("Decile",10)
	attributeTableAfter.updateRow(nextRecord)

del nextRecord
del attributeTableAfter



# Name Intermediates
tractsBeforeDecile = os.path.dirname(tractsBefore) + "/BefDec"
tractsAfterDecile  = os.path.dirname(tractsAfter)  + "/AftDec"


# Rasterize
arcpy.env.extent = "MAXOF"
arcpy.FeatureToRaster_conversion(tractsBefore2, "Decile", tractsBeforeDecile, 5000)
arcpy.env.extent = tractsBeforeDecile
arcpy.FeatureToRaster_conversion(tractsAfter2, "Decile", tractsAfterDecile, 5000)
arcpy.AddMessage("Featured to Raster")

'''
#arcpy.CopyFeatures_management(tractsBefore, tractsBeforeDecile)
#arcpy.CopyFeatures_management(tractsAfter, tractsAfterDecile)

# Output Difference
'''

arcpy.CheckInExtension("spatial")      