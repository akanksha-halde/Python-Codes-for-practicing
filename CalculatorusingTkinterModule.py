import tkinter as tk
gui=tk.Tk()
gui.geometry("245x324")
gui.resizable(0,0)
gui.title("Calculator")


def bt_clear():
    global ip 
    ip = "" 
    inp.set("")

def bt_equal():
    global ip
    result = str(eval(ip)) 
    inp.set(result)
    ip = ""
    
def btn_click(item):
    global ip
    ip = ip + str(item)
    inp.set(ip)
    

ip=""
inp = tk.StringVar()
input_frame =tk.Frame(gui, width=245, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=tk.TOP)
input_field =tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=inp, width=50, bg="white", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) 
buttons_frame =tk.Frame(gui, width=245, height=285.5, bg="grey")
 
buttons_frame.pack()
#row1
clear = tk.Button(buttons_frame, text = "C", fg = "black", width = 26, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = tk.Button(buttons_frame, text = "/", fg = "black", width = 8, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
#row2
seven = tk.Button(buttons_frame, text = "7", fg = "black", width = 8, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = tk.Button(buttons_frame, text = "8", fg = "black", width = 8, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = tk.Button(buttons_frame, text = "9", fg = "black", width = 8, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = tk.Button(buttons_frame, text = "*", fg = "black", width = 8, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
#row3
four = tk.Button(buttons_frame, text = "4", fg = "black", width = 8, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = tk.Button(buttons_frame, text = "5", fg = "black", width = 8, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = tk.Button(buttons_frame, text = "6", fg = "black", width = 8, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = tk.Button(buttons_frame, text = "-", fg = "black", width = 8, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth rows
 
one = tk.Button(buttons_frame, text = "1", fg = "black", width = 8, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = tk.Button(buttons_frame, text = "2", fg = "black", width = 8, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = tk.Button(buttons_frame, text = "3", fg = "black", width = 8, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = tk.Button(buttons_frame, text = "+", fg = "black", width = 8, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
zero = tk.Button(buttons_frame, text = "0", fg = "black", width = 17, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = tk.Button(buttons_frame, text = ".", fg = "black", width = 8, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = tk.Button(buttons_frame, text = "=", fg = "black", width = 8, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 

gui.mainloop()


