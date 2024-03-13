import tkinter

def containData(textbox: tkinter.Text) -> bool:
    if len(textbox.get("1.0", "end")) <= 1: return False
    else: return True

def insertText(datalist: list[str], textbox: tkinter.Text) -> None:
    """Inserta cada dato del datalist como linea en el textbox y elimina los datos existenes en el textbox"""
    textbox.delete('1.0', 'end')
    for item in datalist:
        textbox.insert(tkinter.END, item + "\n")

def convertTxTtoList(textbox: tkinter.Text) -> list[str]:
    """Convierte el contenido del txt a una lista donde cada salto de linea corresponde a list[n]"""
    dataList = textbox.get("1.0", "end").splitlines()
    return dataList
