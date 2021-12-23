# Importamos librerias
import os 
import xlsxwriter
import json




def main(resp):

    # Creamos el objeto de Excel
    name = resp["name_document"]
    wb = xlsxwriter.Workbook(f"./app/static/{name}") 


    f_cell = wb.add_format({
        "font": "Century", # Fuente del texto
        "color":"#00ff00",
        "border":3, # grosor del borde
        "bold":True
    })


    # verificamos que exista el documento de Excel
    ws = wb.add_worksheet(resp["name_sheet"])
    row = 0
    column = 0
    if resp["orientation"] == "y":
        print("llenado de forma vertical")
    for data in  resp["data"]:
        for values in data.values():
            ws.write(row,column,list(data.keys())[0],f_cell)#
            if resp["orientation"] == "y":
                row = row +1
            else:
                column = column + 1
            for value in values:
                print(value)
                ws.write(row,column,value)#
                if resp["orientation"] == "y":
                    row = row + 1
                else:
                    column = column + 1
            if resp["orientation"] == "y":
                row = 0
                column = column + 1
            else:
                column = 0
                row = row + 1
                
    wb.close()
    

if __name__ == "__main__":
    file = open("excel.json",)
    dic = json.load(file)
    main(dic)



