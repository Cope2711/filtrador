import tkinter
import functions

def processDataBTN_Function():
    dataList = functions.convertTxTtoList(dataListTB1)
    originalLen = len(dataList)
    if functions.containData(lineLongerThanTB):
        lenRequired = int(lineLongerThanTB.get("1.0", "end"))
        dataList = [data for data in dataList if len(data) >= lenRequired]
    if functions.containData(lineLessThanTB):
        lenRequired = int(lineLessThanTB.get("1.0", "end"))
        dataList = [data for data in dataList if len(data) <=lenRequired]
    if functions.containData(deleteThisTB):
        dataToFiltred = deleteThisTB.get("1.0", "end")
        for char in dataToFiltred:
            dataList = [item.replace(char, "") for item in dataList]
    if deleteEqualCHBVar.get():
        dataList = list(set(dataList))


    procesedDataLen = len(dataList)
    functions.addTextToLabel(dataListTBLBL1, " - " + str(originalLen))
    functions.addTextToLabel(dataProcesedTBLBL, " - " + str(procesedDataLen))
    functions.insertText(dataList, dataProcesedTB)

def onlyIntWrite(event):
    # Obtener el carácter ingresado
    caracter = event.char
    # Verificar si el carácter es un número o la tecla de borrar (backspace)
    if not caracter.isdigit() and caracter != "\b":
        return "break"  # Evitar la inserción del carácter


# Crear la ventana principal
root = tkinter.Tk()
root.geometry("900x500")
root.resizable(False, False)
root.title("Recepción de Listas")


# Crear los textbox
dataListTBLBL1 = tkinter.Label(root, text="Lista de datos")
dataListTBLBL1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
dataListTB1 = tkinter.Text(root, height=25, width=30)
dataListTB1.grid(row=1, column=0, padx=10, pady=5)

dataProcesedTBLBL = tkinter.Label(root, text="Datos Procesados")
dataProcesedTBLBL.grid(row=0, column=2, padx=10, pady=5, sticky="w")
dataProcesedTB = tkinter.Text(root, height=25, width=30)
dataProcesedTB.grid(row=1, column=2, padx=10, pady=5)

#Filtros de datos
#Mas grande que
lineLongerThanTBLBL = tkinter.Label(root, text="Longitud de linea mas grande que:")
lineLongerThanTBLBL.place(x=550, y=0)
lineLongerThanTB = tkinter.Text(root, height=1, width=10, wrap="none")
lineLongerThanTB.bind("<Key>", onlyIntWrite)
lineLongerThanTB.place(x=550, y=20)

#Menos grande que
lineLessThanTBLBL = tkinter.Label(root, text="Longitud de linea menos grande que:")
lineLessThanTBLBL.place(x=550, y=40)
lineLessThanTB = tkinter.Text(root, height=1, width=10, wrap="none")
lineLessThanTB.bind("<Key>", onlyIntWrite)
lineLessThanTB.place(x=550, y=60)

#Eliminar estos datos de las lineas
deleteThisTBLBL = tkinter.Label(root, text="Eliminar estos datos de cada linea:")
deleteThisTBLBL.place(x=550, y=80)
deleteThisTB = tkinter.Text(root, height=1, width=10, wrap="none")
deleteThisTB.place(x=550, y=100)

#Eliminar lineas repetida
deleteEqualCHBVar = tkinter.BooleanVar()
deleteEqualCHB = tkinter.Checkbutton(root, text="Eliminar lineas iguales (conservar una sola repetición)", variable=deleteEqualCHBVar, onvalue=True, offvalue=False)
deleteEqualCHB.place(x=550, y=120)

# Botón para procesar los datos
processDataBTN = tkinter.Button(root, text="Procesar datos", command=processDataBTN_Function)
processDataBTN.grid(row=2, columnspan=3, pady=10)

# Iniciar el bucle principal
root.mainloop()
