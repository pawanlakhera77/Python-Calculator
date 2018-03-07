import sys,os
from Tkinter import *
e=0
def one():
          entry.insert(END,'1')
          global e
          e=e+1
def two():
          entry.insert(END,'2')
          global e
          e+=1
def three():
          entry.insert(END,'3')
          global e
          e+=1
def four():
          entry.insert(END,'4')
          global e
          e+=1
def five():
          entry.insert(END,'5')
          global e
          e+=1
def six():
          entry.insert(END,'6')
          global e
          e+=1
def seven():
          global e
          e+=1
          entry.insert(END,'7')
def eight():
          entry.insert(END,'8')
          global e
          e+=1
def nine():
          entry.insert(END,'9')
          global e
          e+=1
def zero():
          entry.insert(END,'0')
          global e
          e+=1
def add():
          entry.insert(END,'+')
          global e
          e+=1
def sub():
          entry.insert(END,'-')
          global e
          e+=1
def mul():
          entry.insert(END,'*')
          global e
          e+=1
def div():
          entry.insert(END,'/')
          global e
          e+=1
def calc():
          try:
                    a=0
                    e=0
                    for key in num.get():
                              if a==1:
                                        entry.insert(e,(float(key)))
                              if key=='/':
                                        a=1
                              else:
                                        a=0
                              e+=1
                    num.set(eval(entry.get()))
          except:
                    num.set('Error')
                    
def  negative():
          try:
                    num.set(eval(entry.get()+'*'+'-1'))
          except:
                    num.set('')
def clearAll():
          num.set('')
def clear():
          global e
          entry.delete(e-1)
          e-=1
def dot():
          global e
          e+=1
          entry.insert(END,'.')
root=Tk()

          
root.minsize(280,320)
root.maxsize(280,320)
root.config(bg='blue')
frame=Frame(root)
frame.pack()
root.title('Calculator')
num=StringVar()
topframe=Frame(root)
topframe.pack(side=TOP)
entry=Entry(frame,textvariable=num,justify='left',bg='white',bd=20,insertwidth=1,font=30)
entry.pack(side=TOP)

button1=Button(topframe,padx=16,pady=16,bd=8,text='1',fg='black',bg='yellow',command=one)
button1.pack(side=LEFT)
button2=Button(topframe,padx=16,pady=16,bd=8,text='2',fg='black',bg='yellow',command=two)
button2.pack(side=LEFT)
button3=Button(topframe,padx=16,pady=16,bd=8,text='3',fg='black',bg='yellow',command=three)
button3.pack(side=LEFT)
button4=Button(topframe,padx=16,pady=16,bd=8,text='/',fg='black',bg='yellow',command=div)
button4.pack(side=LEFT)
button5=Button(topframe,padx=16,pady=16,bd=8,text='-',fg='black',bg='yellow',command=sub)
button5.pack(side=LEFT)


frame1=Frame(root)
frame1.pack(side=TOP)


button1=Button(frame1,padx=16,pady=16,bd=8,text='4',fg='black',bg='yellow',command=four)
button1.pack(side=LEFT)
button2=Button(frame1,padx=16,pady=16,bd=8,text='5',fg='black',bg='yellow',command=five)
button2.pack(side=LEFT)
button3=Button(frame1,padx=16,pady=16,bd=8,text='6',fg='black',bg='yellow',command=six)
button3.pack(side=LEFT)
button4=Button(frame1,padx=16,pady=16,bd=8,text='*',fg='black',bg='yellow',command=mul)
button4.pack(side=LEFT)
button5=Button(frame1,padx=16,pady=16,bd=8,text='+',fg='black',bg='yellow',command=add)
button5.pack(side=LEFT)



frame2=Frame(root)
frame2.pack(side=TOP)

button1=Button(frame2,padx=16,pady=16,bd=8,text='7',fg='black',bg='yellow',command=seven)
button1.pack(side=LEFT)
button2=Button(frame2,padx=16,pady=16,bd=8,text='8',fg='black',bg='yellow',command=eight)
button2.pack(side=LEFT)
button3=Button(frame2,padx=16,pady=16,bd=8,text='9',fg='black',bg='yellow',command=nine)
button3.pack(side=LEFT)
button4=Button(frame2,padx=16,pady=16,bd=8,text='=',fg='black',bg='yellow',command=calc)
button4.pack(side=LEFT)
button5=Button(frame2,padx=16,pady=16,bd=8,text='clear',fg='black',bg='yellow',command=clear)
button5.pack(side=LEFT)



frame3=Frame(root)
frame3.pack(side=TOP)


button1=Button(frame3,padx=16,pady=16,bd=8,text='.',fg='black',bg='yellow',command=dot)
button1.pack(side=LEFT)
button2=Button(frame3,padx=16,pady=16,bd=8,text='0',fg='black',bg='yellow',command=zero)
button2.pack(side=LEFT)

button3=Button(frame3,padx=16,pady=16,bd=8,text='ClearAll',fg='black',bg='yellow',command=clearAll)
button3.pack(side=LEFT)
button4=Button(frame3,padx=14,pady=16,bd=8,text='negative',fg='black',bg='yellow',command=negative)
button4.pack(side=LEFT)
          


root.mainloop()
