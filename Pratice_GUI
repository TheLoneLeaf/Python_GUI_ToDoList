import tkinter as tk
root = tk.Tk()

#starting_screen = tk.Frame(root, bg="lightblue")
#deletion_screen = tk.Frame(root, bg="lightgreen")

#starting_screen.grid(row=0, column=0, sticky="nsew")
#deletion_screen.grid(row=0, column=0, sticky="nsew")

#tk.Label(starting_screen, text="Welcome").pack(pady=20)
#tk.Label(deletion_screen, text="Deleting?").pack(pady=20)

#tk.Button(starting_screen, text="Deleteing?", command=deletion_screen.tkraise).pack()
#tk.Button(deletion_screen, text="Deleteing?", command=starting_screen.tkraise).pack()



root.geometry("400x300")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
#weight=1 tells it if theres leftover space, give it to this row / collumn



# ----- Welcome Screen! ----

startingScreen = tk.Frame(root, bg="lightblue") 
startingScreen.grid(row=0, column=0, sticky="nsew") #Sticky tells it to expand north south east west



welcomeMessage = tk.Label(startingScreen, text="Welcome", bg="lightblue", font="50")
welcomeMessage.grid(row=0, column=0, sticky="w")

welcomeMessage = tk.Label(startingScreen, text="View List:", bg="lightblue")
welcomeMessage.grid(row=1, column=0, sticky="w")

welcomeMessage = tk.Label(startingScreen, text="Retrieve Specific Line:", bg="lightblue")
welcomeMessage.grid(row=2, column=0, sticky="w")

welcomeMessage = tk.Label(startingScreen, text="Delete part of the list:", bg="lightblue")
welcomeMessage.grid(row=3, column=0, sticky="w")

welcomeMessage = tk.Label(startingScreen, text="Add new task:", bg="lightblue")
welcomeMessage.grid(row=4, column=0, sticky="w")











deleteScreen = tk.Frame(root, bg="lightgreen") 
deleteScreen.grid(row=0, column=0, sticky="nsew") #Sticky tells it to expand north south east west



startingScreen.tkraise()
root.mainloop()
