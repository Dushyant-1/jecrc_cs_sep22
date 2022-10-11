# GUI - graphical user interface
# libraries
# tkinter
# tutle
# pyQT
import tkinter as ttk
app=ttk.Tk()
app.title('My App')
app.geometry("600x400")
ttk.Label(app, text = 'A Simple Text Label').place(x=50,y=50)

app.mainloop()