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

def button_add(listBox):
    if(classInput.get()):
        fileName = classInput.get().replace(" ", "_")
        classInput.delete(0, "end")
        dirList.append(fileName)
        label= ctk.CTkLabel(listBox,anchor="w", text=dirList[len(dirList)-1])
        label.grid(row=len(dirList)-1,column=0,columnspan=2, padx=20)
    
app = ctk.CTk()
app.title("my app")
app.geometry("340x500")

dirList = []

classInput = ctk.CTkEntry(app, placeholder_text="Folder Name")
classInput.grid(row=0,column=0, padx=(20,5),pady=5,sticky="ew")


listTitle = ctk.CTkLabel(app,anchor="w", text="  File Directory")
listTitle.grid(row=1, column=0,padx=20,pady=(20,5),sticky="ew")
folderList = ctk.CTkScrollableFrame(app, width=280, height=10)
folderList.grid(row=2, column=0, padx=20, pady=0, columnspan=2)
create_btn = ctk.CTkButton(app, text="Create Dir", command=lambda:createWeekDir("Test"))
create_btn.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

add_btn = ctk.CTkButton(app, text="Add", command=lambda:button_add(folderList))
add_btn.grid(row=0, column=1, padx=(5,20), pady=5,)

app.mainloop()
