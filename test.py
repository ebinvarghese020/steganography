from tkinter import filedialog as fd
from tkinter import filedialog
from tkinter.filedialog import askopenfile


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    return filename


    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )


