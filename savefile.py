#SAVE FILE

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfilename(defaultextension = ".txt",
                                        filetypes = [
                                            ("Text file",".txt"),
                                            ("HTML file",".html"),
                                            ("All files",".*")
                                        ]
                                        )
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()

window = Tk()
button = Button(text = "save", command = saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
