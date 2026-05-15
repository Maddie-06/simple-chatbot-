from tkinter import *
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", END)
    
    translated = GoogleTranslator(
        source='auto',
        target=language.get()
    ).translate(text)

    output_text.delete("1.0", END)
    output_text.insert(END, translated)

root = Tk()
root.title("Language Translator")
root.geometry("500x400")

Label(root, text="Enter Text").pack()

input_text = Text(root, height=5)
input_text.pack()

language = StringVar()
language.set("hi")

Label(root, text="Target Language Code").pack()
Entry(root, textvariable=language).pack()

Button(root, text="Translate", command=translate_text).pack()

output_text = Text(root, height=5)
output_text.pack()

root.mainloop()