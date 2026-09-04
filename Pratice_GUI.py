import tkinter as tk
root = tk.Tk()


#Window Size
root.geometry("400x300")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
#weight=1 tells it if theres leftover space, give it to this row / collumn

try:
    with open("demofile.txt", "x") as file:
        pass
except FileExistsError:
    pass


def refreshListbox(listbox):
    listbox.delete(0, tk.END)
    with open("demofile.txt") as file:
        for line in file:
            listbox.insert(tk.END, line.strip())



# ----- Welcome Screen! ----

startingScreen = tk.Frame(root, bg="lightblue") 
startingScreen.grid(row=0, column=0, sticky="nsew") #Sticky tells it to expand north south east west



welcomeMessage = tk.Label(startingScreen, text="Welcome", bg="lightblue", font="50")
welcomeMessage.grid(row=0, column=0, sticky="w")

welcomeMessage = tk.Label(startingScreen, text="View List:", bg="lightblue")
welcomeMessage.grid(row=1, column=0, sticky="w")

def goToFullOutput():
    refreshListbox(task_listbox)          # refresh the list contents first
    fullOutput.tkraise()    # then show the screen

frameB = tk.Button(startingScreen, text="Go to full list", command = goToFullOutput)
frameB.grid(row=1, column=1, sticky="w") #this brings you to the next frame


welcomeMessage = tk.Label(startingScreen, text="Delete part of the list:", bg="lightblue")
welcomeMessage.grid(row=2, column=0, sticky="w")

def goToDeleteLine():
    refreshListbox(task_listbox_delete)          # refresh the list contents first
    deleteLine.tkraise() 


frameD = tk.Button(startingScreen, text="Delete A Line", command=goToDeleteLine)
frameD.grid(row=2, column=1, sticky="w")



welcomeMessage = tk.Label(startingScreen, text="Add new task:", bg="lightblue")
welcomeMessage.grid(row=3, column=0, sticky="w")

def goToWriteLine():
    refreshListbox(task_listbox_write)          # refresh the list contents first
    writeLine.tkraise() 


frameC = tk.Button(startingScreen, text="Write A Line", command=goToWriteLine)
frameC.grid(row=3, column=1, sticky="w") #this brings you to the next frame




#-----Full Output-----
fullOutput = tk.Frame(root, bg="SpringGreen2") 
fullOutput.grid(row=0, column=0, sticky="nsew") #Sticky tells it to expand north south east west

topMessage = tk.Label(fullOutput, text="Full List:", bg="SpringGreen2", font="50")
topMessage.grid(row=0, column=0, sticky="ew")


task_listbox = tk.Listbox(fullOutput, height=10, width=40)
task_listbox.grid(row=1, column=0, sticky="w")




frameA = tk.Button(fullOutput, text="Return", command = lambda: startingScreen.tkraise())
frameA.grid(row=2, column=0, sticky="ew") 

#Write Line

writeLine = tk.Frame(root, bg="SkyBlue1") 
writeLine.grid(row=0, column=0, sticky="nsew") #Sticky tells it to expand north south east west

topMessage = tk.Label(writeLine, text="Adding New Item:", bg="SkyBlue1", font="50")
topMessage.grid(row=0, column=0, sticky="w")


            
task_listbox_write = tk.Listbox(writeLine, height=10, width=30)
task_listbox_write.grid(row=1, column=0, sticky="w")

refreshListbox(task_listbox_write)   
questionMessage = tk.Label(writeLine, text="What would you like to add?", bg="SkyBlue1", font="50")
questionMessage.grid(row=2, column=0, sticky="ew")



task_entry_write = tk.Entry(writeLine, width=30)
task_entry_write.grid(row=3, column=0, sticky="w")

def submit_task():
    
    
    text = task_entry_write.get()
    if text.strip():
        with open("demofile.txt", "a") as file:   # "a" = append, not overwrite
            file.write(text + "\n")
            print("Submitted!")
        task_entry_write.delete(0, tk.END)
        refreshListbox(task_listbox_write)



confirmButton = tk.Button(writeLine, text="Confirm", command=submit_task)
confirmButton.grid(row=4, column=0, sticky="ew")

frameA = tk.Button(writeLine, text="Return", command = lambda: startingScreen.tkraise())
frameA.grid(row=6, column=0) 






#Delete A line

deleteLine = tk.Frame(root, bg="SkyBlue1") 
deleteLine.grid(row=0, column=0, sticky="nsew") #Sticky tells it to expand north south east west

topMessage = tk.Label(deleteLine, text="Deleting Line:", bg="SkyBlue1", font="50")
topMessage.grid(row=0, column=0, sticky="w")





questionMessage = tk.Label(deleteLine, text="Please enter the line number you want to delete", bg="SkyBlue1", font="50")
questionMessage.grid(row=2, column=0, sticky="ew")

task_listbox_delete = tk.Listbox(deleteLine, height=10, width=30)
task_listbox_delete.grid(row=1, column=0, sticky="w")
refreshListbox(task_listbox_delete)  # populate it on startup

task_entry_delete = tk.Entry(deleteLine, width=30)
task_entry_delete.grid(row=3, column=0, sticky="w")

def delete_task():
    text = task_entry_delete.get()
    
    try:
        number = int(text)
    except ValueError:
        print("Not a valid number")
        return  # stop here — nothing more to do if it's not a valid number
    
    with open("demofile.txt", "r") as file:
        lines = file.readlines()
    
    if number < 1 or number > len(lines):
        print("That line number doesn't exist")
        return
    
    del lines[number - 1]  # -1 because list indexes start at 0, but the user sees line numbers starting at 1
    
    with open("demofile.txt", "w") as file:
        file.writelines(lines)
    
    print("Deleted!")
    task_entry_delete.delete(0, tk.END)
    refreshListbox(task_listbox_delete)  # only if deleteLine has its own listbox — see note below


confirmButton = tk.Button(deleteLine, text="Confirm", command=delete_task)
confirmButton.grid(row=4, column=0, sticky="ew")

frameA = tk.Button(deleteLine, text="Return", command = lambda: startingScreen.tkraise())
frameA.grid(row=6, column=0) 






















def readAllLines():
    with open("demofile.txt", "r") as file:
        lines = file.readlines()
    return(lines)




startingScreen.tkraise()


#The actually code behind the command



root.mainloop()
