import tkinter as tk
def press(v):
    entry.insert(tk.END,v)
def clear():
    entry.delete(0,tk.END)
def calc():
    try:
        res =eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,res)
        
        
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"error")

root=tk.Tk()
root.title("calculator")
root.configure(bg="#1e1e1e")
root.geometry("400x500")
root.resizable(True,False)

entry=tk.Entry(root,font=("Segoe UI",20),bg="#2d2d2d",fg="white",
               bd=0,justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=12,pady=12,ipady=10)

buttons=["7","8","9","/",
        "6","5","4","*",
        "1","2","3","-",
        "0",".","=","+"]

    
r=1
c=0
for i in buttons:
    cmd=calc if i == "=" else lambda x=i:press(x)
    tk.Button(root,text=i,command=cmd,
              font=("Segoe UI",14),
              width=5,height=2,
              bg="#456774" if i in "+-*/="  else "#3a3a3a",
              fg="white",bd=0).grid(row=r,column=c, padx=6,pady=6)
    c+=1
    if c==4:
        c=0
        r+=1
tk.Button(root,font=("Segoe UI",14),text="c",
          command=clear,
          bg="#D29A4B",fg="white",bd=0,width=10,
          height=2).grid(row=r,column=0,columnspan=4,padx=6,pady=6,ipadx=2)
root.mainloop()
