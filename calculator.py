from tkinter import *

prev = curr = operator = None


def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text = new)
root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

def clear():
    result_label.config(text='')
    
def get_operator(op):
    global prev,operator
    prev = int(result_label['text'])
    operator = op
    result_label.config(text='')
    
def get_result():
    global prev,operator,curr
    
    curr = int(result_label['text'])
    if operator == '+':
        result_label.config(text = str(prev+curr))
    elif operator == '-':
        result_label.config(text = str(prev-curr))
    elif operator == '*':
        result_label.config(text = str(prev*curr))
    else:
        if curr == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text = str(round(prev/curr)))
    
result_label = Label(root,text = '', bg = 'black',fg='white')
result_label.grid(row = 0,column =0, columnspan = 5,pady = (50,25),sticky ='w')
result_label.config(font=('verdana',30,'bold'))

bn7 = Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2, command = lambda : get_digit(7))
bn7.grid(row=1,column=0)
bn7.config(font=('verdana',14))

bn8 = Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_digit(8))
bn8.grid(row=1,column=1)
bn8.config(font=('verdana',14))

bn9 = Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_digit(9))
bn9.grid(row=1,column=2)
bn9.config(font=('verdana',14))

bn_add = Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_operator('+'))
bn_add.grid(row=1,column=3)
bn_add.config(font=('verdana',14))


bn4 = Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_digit(4))
bn4.grid(row=2,column=0)
bn4.config(font=('verdana',14))

bn5 = Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_digit(5))
bn5.grid(row=2,column=1)
bn5.config(font=('verdana',14))

bn6 = Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_digit(6))
bn6.grid(row=2,column=2)
bn6.config(font=('verdana',14))

bn_sub = Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_operator('-'))
bn_sub.grid(row=2,column=3)
bn_sub.config(font=('verdana',14))

bn1 = Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_digit(1))
bn1.grid(row=3,column=0)
bn1.config(font=('verdana',14))

bn2 = Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_digit(2))
bn2.grid(row=3,column=1)
bn2.config(font=('verdana',14))

bn3 = Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_digit(3))
bn3.grid(row=3,column=2)
bn3.config(font=('verdana',14))

bn_mul = Button(root,text='*',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_operator('*'))
bn_mul.grid(row=3,column=3)
bn_mul.config(font=('verdana',14))

bn_clr = Button(root,text='C',bg='#00a65a',fg='white',width=5,height=2,command = lambda: clear())
bn_clr.grid(row=4,column=0)
bn_clr.config(font=('verdana',14))

bn0 = Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_digit(0))
bn0.grid(row=4,column=1)
bn0.config(font=('verdana',14))

bn_equals = Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2, command = get_result)
bn_equals.grid(row=4,column=2)
bn_equals.config(font=('verdana',14))

bn_div = Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2,command = lambda : get_operator('/'))
bn_div.grid(row=4,column=3)
bn_div.config(font=('verdana',14))

root.mainloop()
