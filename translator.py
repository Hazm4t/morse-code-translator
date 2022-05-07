from tkinter import *
import tkinter.font as fnt
import pyperclip

## Get English Alphabet ##
a_alphabet = []

a_file = open("alphabet.txt", "r")
for line in a_file:
    a_alphabet.append(line.split()[0] )


## Get Morse Alphabet ##
b_alphabet = []

b_file = open("morse.txt", "r")
for line in b_file:
    b_alphabet.append(line.split()[0] )


## Create translation dictionary ##
translate_dict = {}

letter_index = 0
for letter in a_alphabet:
    translate_dict[letter] = b_alphabet[letter_index]
    letter_index += 1


## Create decode dict
decode_dict = {}

character_index = 0
for character in b_alphabet:
    decode_dict[character] = a_alphabet[character_index]
    character_index += 1

## Create English-Morse translation function ##
allowed_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def translate(string):
    translated_string = ""

    upper_string = string.upper()

    for letter in upper_string:
        if letter in allowed_letters:
            translated_string += translate_dict[letter]
            translated_string += " "
    
    return translated_string


## Create Morse-English translation function ##
def decode(string):
    decoded_string = ""
    
    for char in string.split():
        try:
            decoded_string += decode_dict[char]
            
        
        except:
            pass
    
    return decoded_string

## GUI ##
window = Tk()
window.title("Morse Code Translator")
window.iconphoto(True, PhotoImage(file='icon.png'))
window.geometry("500x293")
window.resizable(False, False)
window.configure(bg="cyan")

inputText = Text(window, font=fnt.Font(size=15), width=500, height=5)

outputText = Text(window, font=fnt.Font(size=15), state="disabled", width=500, height=5)

translateButton = Button(window, text="Translate", font=fnt.Font(size=20), bg="blue", fg='white')
decodeButton = Button(window, text="Decode", font=fnt.Font(size=20), bg="blue", fg='white')
copyButton = Button(window, text="Copy", font=fnt.Font(size=20), bg="blue", fg='white')

inputText.insert("end", "Insert text here...")

def guiTranslate():
    outputText.config(state="normal")
    outputText.delete(1.0, "end")
    outputText.insert("end", translate(inputText.get(1.0, "end") ) )
    outputText.config(state="disabled")

def guiDecode():
    outputText.config(state="normal")
    outputText.delete(1.0, "end")
    outputText.insert("end", decode(inputText.get(1.0, "end") ) )
    outputText.config(state="disabled")

translateButton.config(command=lambda:guiTranslate() )
decodeButton.config(command=lambda: guiDecode() )
copyButton.config(command =lambda: pyperclip.copy(outputText.get(1.0, "end") ) )

inputText.pack()
outputText.pack()
translateButton.pack(side="left")
decodeButton.pack(side="left")
copyButton.pack(side="left")

window.mainloop()