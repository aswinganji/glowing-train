from tkinter import*
root = Tk()
root.title("Pqwes")
root.geometry("900x600")
from tkinter import ttk

class atlas3b:
    
    def __init__(self):
        
        print("This is to create an element")
    def uiop(self):
        class_btn = Button(root,text = "Bqwertyu",command = self.message)
        class_btn.pack()
        
    def uiop2(self):
        class_btn1 = Label(root,text = "Bqwertyu",fg = "red")
        class_btn1.pack()
        
    def message(self):
        messagebox.showinfo("Click Click!","Crok Crok Crok Crok")
        
    def uiop3(self):
        blah_blah_blah_blah = ["1","2","3","4","5","6"]
        class_btn2 = ttk.Combobox(root,text = "Bqwertyu",value = blah_blah_blah_blah)
        class_btn2.pack()
        
    def choose(self):
        asdfghjklzxcvbnm = poiuytrewq.get()
        if (asdfghjklzxcvbnm == "Button"):
            self.uiop()
            
        if (asdfghjklzxcvbnm == "Label"):
            self.uiop2()
            
        if (asdfghjklzxcvbnm == "Drop"):
            self.uiop3()
            
qwertyasdfg = ["Button","Label","Drop"]
poiuytrewq = ttk.Combobox(root,text = "qwertyuiopasdfghjklzxcvbnm",value = qwertyasdfg)
object1 = atlas3b()
by = Button(root,text = "aszx",command = object1.choose)
poiuytrewq.pack()
by.pack()

root.mainloop()
