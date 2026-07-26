import tkinter

def containData(textbox: tkinter.Text | tkinter.Entry) -> bool:
    if isinstance(textbox, tkinter.Text):
        return bool(textbox.get("1.0", "end-1c").strip())

    return bool(textbox.get().strip())

def insertText(datalist: list[str], textbox: tkinter.Text) -> None:
    """Inserta cada dato del datalist como linea en el textbox y elimina los datos existenes en el textbox"""
    textbox.delete('1.0', 'end')
    for item in datalist:
        textbox.insert(tkinter.END, item + "\n")

def convertTxTtoList(textbox: tkinter.Text) -> list[str]:
    """Convierte el contenido del txt a una lista donde cada salto de linea corresponde a list[n]"""
    dataList = textbox.get("1.0", "end").splitlines()
    return dataList

def addTextToLabel(label: tkinter.Label, newText: str) -> None:
    """Añade el text proporcionado al final del texto original"""

    originalText = label.cget("text")
    #En caso de que haya habido una afectacion anterior, con el estandar del - 
    try:
        originalText = originalText[:originalText.index("-") - 1]
    except:
        pass
    newText = originalText + newText
    label.config(text=newText)
