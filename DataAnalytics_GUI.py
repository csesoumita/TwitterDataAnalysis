from tkinter import ttk
from tkinter import filedialog
from tkinter import Text
from tkinter import END
from tkinter import TOP
from tkinter import Frame
from tkinter import Button
from tkinter import BOTH
from past.builtins import execfile

import StreamingAPI
import tweepy
import pymongo
from pymongo.mongo_client import MongoClient
import tkinter as tk
import os
import sys
win=tk.Tk()
win.title("Python GUI")
w = tk.Label(win, text="Social Media Crawled Data Analytics Window",bg='blue',height=2,width=720,font=(None, 14))
w.pack()
#************LSH files LSH_PartA.py and LSH_PartB to be run from commandline due to high time complexity******
def data_display_googleplus():
    execfile('DataAnalytics_GoogleAPI_API_key.py')
    win.fileName= r"C:\Users\SOUMITA\PycharmProjects\Webscience_CourseWork_Final\GoogleAPI_DataAnalytics.txt"
    text_to_read = open(win.fileName).read()
    print(text_to_read)
    print(win.fileName)
    text_to_display = Text(win, height=10, width=60)
    text_to_display.pack()
    text_to_display.insert(END, text_to_read)
def data_display_twitter():
    execfile('DataAnalytics_Twitter.py')
    win.fileName = r"C:\Users\SOUMITA\PycharmProjects\Webscience_CourseWork_Final\Twitter_DataAnalytics.txt"
    text_to_read = open(win.fileName).read()
    print(text_to_read)
    print(win.fileName)
    text_to_display_twitter = Text(win, height=10, width=60)
    text_to_display_twitter.pack()
    text_to_display_twitter.insert(END, text_to_read)

def show_histogram():
    execfile('Histogram.py')
def show_twitter():
    execfile('DataAnalytics_GoogleAPI_API_key.py')

b8=tk.Button(win,text='Display GooglePlus DataAnalytics',command=data_display_googleplus)
b8.pack()
b12=tk.Button(win,text='Show Twitter Data Analytics Histogram',command=show_histogram)
b12.pack()
b12=tk.Button(win,text='Show Twitter Data Analytics ',command=data_display_twitter)
b12.pack()
b11=tk.Button(win,text='Exit',command=exit)
b11.pack()
win.mainloop()