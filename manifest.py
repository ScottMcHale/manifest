from textblob import TextBlob 
from newspaper import Article
from tkinter import Tk, Button, Entry, Pack, Frame, Text, Label
import os
import sys
import time



def process():
    article = Article(myUrl.get())
    article.download()
    article.parse()
    article.nlp()

    print(article.summary)

# root, myGUI, inputBox[labelURL, myURL], buttonBox[functions1,2...Exit], outputBox[returns]
# draws main gui with labeled text input box for url
# NEED TO BUILD OUTPUT BOX TO DUMP PROCESS RESULTS INTO
root = Tk()
root.title("Manifest")
myGUI = Frame(root)
myGUI.pack()

inputBox = Frame(myGUI, width=300)
inputBox.pack(side="bottom")

labelUrl = Label(inputBox,text="URL",fg="#594308", bg="#fcf2d7", padx=4)
labelUrl.pack(side="left")

myUrl = Entry(inputBox, relief="flat", bd=4, width=60, bg="#edd79d", fg="white")
myUrl.pack(side="right")

buttonBox = Frame(myGUI, width=300)
buttonBox.pack(side="top")

mySummary = Button(buttonBox, command=process, text="Summary")
mySummary.pack()

# just a quick print to check on one thing or another
print(myUrl.get()) 




root.mainloop()

	
#url = 'https://www.nytimes.com/2021/01/29/health/covid-vaccine-johnson-and-johnson-variants.html'



# print(f'Title:{article.title}')
# print(f'Authors:{article.authors}')
# print(f'Publication Date:{article.publish_date}')
# print(f'Summary:{article.summary}')