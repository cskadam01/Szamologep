import tkinter as tk
import math 



Logs = []


def solve ():
    

    problem = numInput.get() 
    if "Sqrt" in problem:
            problem = problem.replace("Sqrt", "math.sqrt")
    try:
            
            result = eval(problem)
            resultVis.config(text=f"{result}")
            numInput.delete(0, tk.END)
            resultVis.place(x=100, y=200)
            
            
                        

            print(Logs)
            


    except ZeroDivisionError:
            numInput.delete(0, tk.END)
            resultVis.config(text="Nullával nem lehet osztani!", foreground="red")
            resultVis.place(x=100, y=200)
        
    except SyntaxError as e:
            numInput.delete(0, tk.END)
            resultVis.config(text=" Szintaktikai hiba, kérlek ellenőrizd a bevitelt!", foreground="red")
            resultVis.place(x=100, y=200)

    except NameError:
            numInput.delete(0, tk.END)
            resultVis.config(text=" Nem megfelelő változó! ", foreground="red")
            resultVis.place(x=100, y=200)



def insertion (karakter):
    numInput.insert(tk.END, karakter)
    Logs.append(karakter)




def backspace():
    problem = numInput.get() 
    char = len(problem)
    numInput.delete(char-1, tk.END)

def AC():
    numInput.delete(0, tk.END)
    



    




window = tk.Tk()
window.geometry('400x600')

baseCanva = tk.Canvas (window, height=600, width=400, background="#9dbec4", borderwidth=0, highlightthickness=0)
baseCanva.place(x=0, y=0)




#region Szám gombok

button0 = tk.Button(baseCanva, height=2, width=18, text="0", highlightthickness=0, borderwidth=0, command=lambda: insertion("0"))
button0.place(x=100, y=400)   

button1 = tk.Button(baseCanva, height=2, width=4, text="7", highlightthickness=0, borderwidth=0, command=lambda: insertion("7"))
button1.place(x=100, y= 250)
button2 = tk.Button(baseCanva, height=2, width=4, text="4", highlightthickness=0, borderwidth=0, command=lambda: insertion("4"))
button2.place(x=100, y= 300)
button3 = tk.Button(baseCanva, height=2, width=4, text="1", highlightthickness=0, borderwidth=0, command=lambda: insertion("1"))
button3.place(x=100, y= 350)


button4 = tk.Button(baseCanva, height=2, width=4, text="8", highlightthickness=0, borderwidth=0, command=lambda: insertion("8"))
button4.place(x=150, y= 250)
button5 = tk.Button(baseCanva, height=2, width=4, text="5", highlightthickness=0, borderwidth=0, command=lambda: insertion("5"))
button5.place(x=150, y= 300)
button6 = tk.Button(baseCanva, height=2, width=4, text="2", highlightthickness=0, borderwidth=0, command=lambda: insertion("2"))
button6.place(x=150, y= 350)


button7 = tk.Button(baseCanva, height=2, width=4, text="9", highlightthickness=0, borderwidth=0, command=lambda: insertion("9"))
button7.place(x=200, y= 250)
button8 = tk.Button(baseCanva, height=2, width=4, text="6", highlightthickness=0, borderwidth=0, command=lambda: insertion("6"))
button8.place(x=200, y= 300)
button9 = tk.Button(baseCanva, height=2, width=4, text="3", highlightthickness=0, borderwidth=0, command=lambda: insertion("3"))
button9.place(x=200, y= 350)



#region Műveletek

buttonExtract = tk.Button(baseCanva, height=2, width=12, text="-", highlightthickness=0, borderwidth=0, command=lambda: insertion("-"))
buttonExtract.place(x=275, y=250)

buttonAdd = tk.Button(baseCanva, height=2, width=12, text="+", highlightthickness=0, borderwidth=0, command=lambda: insertion("+"))
buttonAdd.place(x=275, y=300)

buttonExtract = tk.Button(baseCanva, height=2, width=4, text="/", highlightthickness=0, borderwidth=0, command=lambda: insertion("/"))
buttonExtract.place(x=275, y=350)

buttonExtract = tk.Button(baseCanva, height=2, width=4, text="*", highlightthickness=0, borderwidth=0, command=lambda: insertion("*"))
buttonExtract.place(x=320, y=350)

buttonSqrt = tk.Button(baseCanva, height=2, width=18, text="Sqrt", highlightthickness=0, borderwidth=0, command=lambda: insertion("Sqrt"))
buttonSqrt.place(x=100, y=450)

buttonSqrt = tk.Button(baseCanva, height=2, width=8, text="(", highlightthickness=0, borderwidth=0, command=lambda: insertion("("))
buttonSqrt.place(x=100, y=500) 
buttonSqrt = tk.Button(baseCanva, height=2, width=8, text=")", highlightthickness=0, borderwidth=0, command=lambda: insertion(")"))
buttonSqrt.place(x=170, y=500) 

buttonSolve = tk.Button(baseCanva, height=2, width=12, text="=", highlightthickness=0, borderwidth=0, command=solve, )
buttonSolve.place(x=275, y=100)


buttonDecimal = tk.Button(baseCanva, height=2, width=12, text=".", highlightthickness=0, borderwidth=0, command=lambda: insertion("."))
buttonDecimal.place(x=275, y=400) 




numInput = tk.Entry(baseCanva,  width=22,  highlightthickness=0, borderwidth=0)
numInput.place(x=100, y=150, height=37)

numDelete = tk.Button(baseCanva, text="C",height=2, width=12,highlightthickness=0, borderwidth=0, command=backspace)
numDelete.place(x=275, y=200)

numClear = tk.Button(baseCanva, text="AC",height=2, width=12,highlightthickness=0, borderwidth=0, command=AC)
numClear.place(x=275, y=150)

resultVis= tk.Label(baseCanva, )

 


window.mainloop()