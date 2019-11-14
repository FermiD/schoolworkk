# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:22:13 2019

@author: aqsha
"""

#DISCLAIMER: The usage of tkinter in here is quite heavy. Also I took many ideas on developing this through other samples.

from tkinter import *
#Below: Both are lists. Look at the country_qlist.py file.
from country_qlist import possibleq, possiblea
import random

#Below is to shuffle two lists at once within the same order as each other.
#That is to avoid achieving the non-corresponding capital as the answer.
#After the shuffle, both the lists are read here as tuples.
comb = list(zip(possibleq, possiblea))
shuffled = random.shuffle(comb)
possibleq, possiblea= zip(*comb)


#This 1st class is used to clear up AND set up the main frame.
#If removed, the tkinter frame will be very distorted. Also to move around frames.
class QuizApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frame = {}
        for F in (Quiz1, Quiz2, Quiz3, Quiz4, Quiz5, Quiz6, Quiz7,Finish):
            page_name = F.__name__
            frame = F(master=container, controller=self)
            self.frame[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("Quiz1")
        
        
    def show_frame(self, page_name):
        frame = self.frame[page_name]
        frame.tkraise()

#Classes Quiz2 to 7 are pretty much copies. Except in 7, button leads to the finish.
#Text are formatted to suit the small window, for now. The window is stretchable.        
class Quiz1(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        titlelabel = Label(self, text="The Capitals Quiz", font=('Arial', 18, "bold"))
        titlelabel.pack(side="top")
        Button(self, text="Start the quiz!", command=lambda: controller.show_frame("Quiz2")).pack()
        
class Quiz2(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        
        baselabel = Label(self, text="What is the capital of " + possibleq[0] + "?", font=('Arial', 13, "italic"))
        baselabel.pack(side="top")
        
        self.enter = Entry(self)
        self.enter.pack()
        
        answerbutton = Button(self, text="Answer?", command=self.getinputs)
        answerbutton.pack()
           
        Button(self, text="Next Question", command=lambda: controller.show_frame("Quiz3")).pack()
        
    def getinputs(self):
        the_ans_itself = possiblea[0]
        value = self.enter.get()
        if value == the_ans_itself:
            Label(self, text="Correct! The answer is " + the_ans_itself, font=('Arial', 18, "bold")).pack(side="bottom")
        else:
            Label(self, text="Incorrect! Try again.", font=('Arial', 18, "bold")).pack(side="bottom")
            
class Quiz3(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        
        baselabel = Label(self, text="What is the capital of " + possibleq[1] + "?", font=('Arial', 13, "italic"))
        baselabel.pack(side="top")
        
        self.enter = Entry(self)
        self.enter.pack()
        
        answerbutton = Button(self, text="Answer?", command=self.getinputs)
        answerbutton.pack()
           
        Button(self, text="Next Question", command=lambda: controller.show_frame("Quiz4")).pack()
        
    def getinputs(self):
        the_ans_itself = possiblea[1]
        value = self.enter.get()
        if value == the_ans_itself:
            Label(self, text="Correct! The answer is " + the_ans_itself, font=('Arial', 18, "bold")).pack(side="bottom")
        else:
            Label(self, text="Incorrect! Try again.", font=('Arial', 18, "bold")).pack(side="bottom")
            
class Quiz4(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        
        baselabel = Label(self, text="What is the capital of " + possibleq[2] + "?", font=('Arial', 13, "italic"))
        baselabel.pack(side="top")
        
        self.enter = Entry(self)
        self.enter.pack()
        
        answerbutton = Button(self, text="Answer?", command=self.getinputs)
        answerbutton.pack()
           
        Button(self, text="Next Question", command=lambda: controller.show_frame("Quiz5")).pack()
        
    def getinputs(self):
        the_ans_itself = possiblea[2]
        value = self.enter.get()
        if value == the_ans_itself:
            Label(self, text="Correct! The answer is " + the_ans_itself, font=('Arial', 18, "bold")).pack(side="bottom")
        else:
            Label(self, text="Incorrect! Try again.", font=('Arial', 18, "bold")).pack(side="bottom")
            
class Quiz5(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        
        baselabel = Label(self, text="What is the capital of " + possibleq[3] + "?", font=('Arial', 13, "italic"))
        baselabel.pack(side="top")
        
        self.enter = Entry(self)
        self.enter.pack()
        
        answerbutton = Button(self, text="Answer?", command=self.getinputs)
        answerbutton.pack()
           
        Button(self, text="Next Question", command=lambda: controller.show_frame("Quiz6")).pack()
        
    def getinputs(self):
        the_ans_itself = possiblea[3]
        value = self.enter.get()
        if value == the_ans_itself:
            Label(self, text="Correct! The answer is " + the_ans_itself, font=('Arial', 18, "bold")).pack(side="bottom")
        else:
            Label(self, text="Incorrect! Try again.", font=('Arial', 18, "bold")).pack(side="bottom")
            
class Quiz6(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        
        baselabel = Label(self, text="What is the capital of " + possibleq[4] + "?", font=('Arial', 13, "italic"))
        baselabel.pack(side="top")
        
        self.enter = Entry(self)
        self.enter.pack()
        
        answerbutton = Button(self, text="Answer?", command=self.getinputs)
        answerbutton.pack()
           
        Button(self, text="Next Question", command=lambda: controller.show_frame("Quiz7")).pack()
        
    def getinputs(self):
        the_ans_itself = possiblea[4]
        value = self.enter.get()
        if value == the_ans_itself:
            Label(self, text="Correct! The answer is " + the_ans_itself, font=('Arial', 18, "bold")).pack(side="bottom")
        else:
            Label(self, text="Incorrect! Try again.", font=('Arial', 18, "bold")).pack(side="bottom")
            
class Quiz7(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        
        baselabel = Label(self, text="What is the capital of " + possibleq[5] + "?", font=('Arial', 13, "italic"))
        baselabel.pack(side="top")
        
        self.enter = Entry(self)
        self.enter.pack()
        
        answerbutton = Button(self, text="Answer?", command=self.getinputs)
        answerbutton.pack()
           
        Button(self, text="Finish the quiz", command=lambda: controller.show_frame("Finish")).pack()
        
    def getinputs(self):
        the_ans_itself = possiblea[5]
        value = self.enter.get()
        if value == the_ans_itself:
            Label(self, text="Correct! The answer is " + the_ans_itself, font=('Arial', 18, "bold")).pack(side="bottom")
        else:
            Label(self, text="Incorrect! Try again.", font=('Arial', 18, "bold")).pack(side="bottom")
            
            

class Finish(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        titlelabel2 = Label(self, text="Thank you for playing!", font=('Arial', 18, "bold"))
        titlelabel2.pack(side="top")
        baselabel = Label(self, text="Keep playing to improve your knowledge.", font=('Arial', 12, "italic"))
        baselabel.pack(side="top")
     
#Calls the topmost app which is basically a placeholder for the following frames.
app = QuizApp() 
app.mainloop()
