import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tkinter as ttk
from PIL import ImageTk, Image

data=pd.read_csv(r'Day 20/treadmil-users.csv')

app = ttk.Tk()
app.geometry('600x300')
app.geometry('600x400')
app.title('Treadmill Users Analysis')

graphs = ttk.Variable(app)
values = {
    'Pair Plot': 'sns.pairplot(data=data)',
    'Jointplot': "sns.jointplot(data=data,x='{col1}',y='{col2}')",
    'Bar Plot' : "sns.barplot(data=data,x='{col1}',y='{col2}')"
    'Bar Plot' : "sns.barplot(data=data,x='{col1}',y='{col2}')",
    'Box Plot':"sns.boxplot(data=data,x='{col1}',y='{col2}')"
}
## Radio Button
graphs.set(values['Pair Plot'])
@@ -34,18 +36,54 @@
col2=ttk.Variable(app)
col2.set(values[0])
ttk.Label(app,text='Column 2').place(x=150,y=80)
ttk.OptionMenu(app,col1, *values).place(x=150,y=110)
ttk.OptionMenu(app,col2, *values).place(x=150,y=110)

## Option Menu 3
col3=ttk.Variable(app)
col3.set(values[0])
ttk.Label(app,text='Column 3').place(x=150,y=150)
ttk.OptionMenu(app,col1, *values).place(x=150,y=180)
ttk.OptionMenu(app,col3, *values).place(x=150,y=180)

# Canvas
cnv=ttk.Canvas(app,width=600,height=200)
cnv.place(x=250,y=60)

# Label
result=ttk.Variable(app)
ttk.Label(app,textvariable=result).place(x=300,y=300)

def show():
    #print(graphs.get())
    print(col1.get(),col2.get(),col3.get())
    global img
    global cnv

    column1=col1.get()
    column2=col2.get()
    column3=col3.get()

    g=graphs.get()
    if 'col1' in g:
        if column1=='Select':
            result.set('Column 1 must be selected')
            return
    if 'col2' in g:
        if column2=='Select':
            result.set('Column 2 must be selected')
            return
    if 'col3' in g:
        if column3=='Select':
            result.set('Column 3 must be selected')
            return                

    fig=plt.figure(figsize=(5,2))
    # eval and exec will read string as a function
    eval(g.format(col1=column1,col2=column2,col3=column3))
    fig.savefig('graph.png')
    img=ImageTk.PhotoImage(Image.open('graph.png').resize((200,200)))

    cnv.create_image(0,0,anchor=ttk.NW,image=img)
    result.set('Success')
    #plt.show()
    #print(col1.get(),col2.get(),col3.get())

app.mainloop()