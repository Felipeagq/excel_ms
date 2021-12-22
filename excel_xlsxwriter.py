# Importamos librerias
import os 
import xlsxwriter
import json


# Cargamos el json
with open('excel.json') as file:
    creation = json.load(file)



# Creamos el objeto de Excel
wb = xlsxwriter.Workbook(creation["name_document"]) 


f_cell = wb.add_format({
    "font": "Century", # Fuente del texto
    "color":"#00ff00",
    "border":3, # grosor del borde
    "bold":True
})


# verificamos que exista el documento de Excel
ws = wb.add_worksheet(creation["name_sheet"])
row = 0
column = 0
if creation["orientation"] == "y":
    print("llenado de forma vertical")
for data in  creation["data"]:
    for values in data.values():
        ws.write(row,column,list(data.keys())[0],f_cell)#
        if creation["orientation"] == "y":
            row = row +1
        else:
            column = column + 1
        for value in values:
            print(value)
            ws.write(row,column,value)#
            if creation["orientation"] == "y":
                row = row + 1
            else:
                column = column + 1
        if creation["orientation"] == "y":
            row = 0
            column = column + 1
        else:
            column = 0
            row = row + 1
            
wb.close()






