import customtkinter as ctk
import os
def createWeekDir(name):
    os.makedirs(name, exist_ok=True)  
    for i in range(10):
        if i+1 < 10:
            num = "0"+str(i+1)
        else:
            num = str(i+1)
        os.makedirs(name+"/Week"+num, exist_ok=True)

def button_callback():
    fileName = classInput.get()
    label= ctk.CTkLabel(app,text=fileName)
    label.pack(pady=5)
    
    


app = ctk.CTk()
app.title("my app")
app.geometry("325x500")

classInput = ctk.CTkEntry(app, placeholder_text="Folder Name")
classInput.grid(row=0,column=0, padx=(20,5),pady=20,sticky="ew")
button = ctk.CTkButton(app, text="Add", command=button_callback)
button.grid(row=0, column=1, padx=(5,20), pady=20,)

frame = ctk.CTkFrame(app)
frame.grid(row=1,column=0, padx=20,pady=20, columnspan=2,sticky="ew")


app.mainloop()