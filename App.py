import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog


arr = ["Adam.png", "Alex.png", "Ali.png", "Jim.png"]
arrName = ["Adam", "Alex", "Ali", "Jim"]
root = None  # Declare root as a global variable
frameImages = None
count = -1 # used as flag variable for clear function to work properly. Meaning clear will happen only when there are images
count1 = -1 # used as flag variable for clear function to work properly. Meaning clear will happen only when there are images
countI = -1 # used as flag variable to add and show friends correctly. Meaning when showFriends is called first and addFriend after, images should appear order wise and vice versa


def quitApplication():
    # function to quit the app
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
    if confirm:
        root.quit()


def showSelectedImage(imagePath):
    # function to show the selected image in the Big label
    global frameImages
    name = imagePath.split(".")  # name = ["adam","png"]
    name = name[0] # name = adam 
    selectedImage = Image.open(imagePath)
    selectedImage = selectedImage.resize((200, 200))  # Setting the desired size of the selected image

    # Creating a PhotoImage object from the selected image
    selectedPhoto = ImageTk.PhotoImage(selectedImage)

    # Creating a label inside the frame to display the selected image
    selectedLabel = tk.Label(frameImages, image=selectedPhoto, text= name, compound="top")
    selectedLabel.image = selectedPhoto  # Storing the image object as an attribute
    selectedLabel.config(highlightthickness=1, highlightbackground="black")
    selectedLabel.grid(row=3, column=3, columnspan=4, padx=0, pady=10, sticky="nswe")  


def showFriends():
    # function is displaying all the friends in image property of button
    global count, countI
    if  count >= 0:
        messagebox.showinfo("Gallery Status", "Gallery is on, please choose another action.")
    else:
        for i in range(len(arr)):
            img = Image.open(arr[i])
            img = img.resize((50, 50))
            photo = ImageTk.PhotoImage(img)
            friendButton = tk.Button(frameImages, text=arrName[i], image=photo, compound="top",
                                    width=60, height=60, command=lambda imagePath=arr[i]: showSelectedImage(imagePath))
            friendButton.image = photo
            friendButton.grid(row=0, column=countI + 1, padx=0, pady=10, sticky="w")
            count += 1
            countI += 1
            i += 1
            
def clear():
    global count, frameImages, count1
    if(count == -1 and count1 == -1):
        messagebox.showinfo("Gallery is off", "No need to clear as nothing is displayed!")
    else:
        for widget in frameImages.winfo_children(): #winfo_children() returns all the child widgets
            widget.destroy()
        count = -1
        count1 = -1

def addNewFriend():
    global countI, count1
    # Opening the file dialog to select an image file
    filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    name = os.path.splitext(os.path.basename( filePath))[0] # getting base name. removing c:/users:download: ...
    nameWithExtension = os.path.basename( filePath) # name = adam.png

    if  filePath:
        # Displaying a confirmation message
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to add a new friend?")
        if confirm:
            img = Image.open( filePath)
            img = img.resize((50, 50))
            photo = ImageTk.PhotoImage(img)
            friendButton = tk.Button(frameImages, text=name, image=photo, compound="top",
                                    width=60, height=60, command=lambda imagePath=nameWithExtension: showSelectedImage(imagePath))
            friendButton.image = photo
            friendButton.grid(row=0, column=countI+1, padx=0, pady=10, sticky="w")
            countI += 1
            count1 += 1
            
def deleteFriend():
    global frameImages

    filePath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    name = os.path.splitext(os.path.basename( filePath))[0]

    if  filePath:
        # Displaying a confirmation message
        confirm = messagebox.askyesno("Confirmation", f"Are you sure you want to delete {name}?")
        if confirm:
            for widget in frameImages.winfo_children():
                if isinstance(widget, tk.Button):     # getting only button widget
                    # Check if the button image matches the deleted image
                    if widget["text"] == name:
                        widget.destroy()
                elif isinstance(widget, tk.Label):
                    if widget["text"] == name:
                        widget.destroy()



        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("My Friends Gallery")
    root.geometry("600x450")
    root.configure(bg="#FFFF01")

    # Creating the frame here of color #067b00
    frame = tk.Frame(root, bg="#067b00", width=600, height=100)
    frame.pack(side="top", fill="x")

    # Creating the label inside the frame with text "Friends gallery menu"
    label = tk.Label(frame, text="Friends gallery menu", bg="#067b00", fg="white")
    label.pack(side="top", padx=10, pady=5, anchor="nw")

    # Creating 5 buttons inside the frame
    btnShowFriends = tk.Button(frame, text="Show Friends", bg="#b2dfee", fg="black", command=showFriends)
    btnClearAll = tk.Button(frame, text="Clear All", bg="#b2dfee", fg="black", command=clear)
    btnDeleteFriend = tk.Button(frame, text="Delete a Friend", bg="#b2dfee", fg="black", command=deleteFriend)
    btnAddNewFriend = tk.Button(frame, text="Add new Friend", bg="#b2dfee", fg="black", command=addNewFriend)
    btnQuit = tk.Button(frame, text="Quit", bg="#b2dfee", fg="black", command=quitApplication)

    # Packing 5 buttons in a horizontal line
    btnShowFriends.pack(side="left", expand=True, fill="both")
    btnClearAll.pack(side="left", expand=True, fill="both")
    btnDeleteFriend.pack(side="left", expand=True, fill="both")
    btnAddNewFriend.pack(side="left", expand=True, fill="both")
    btnQuit.pack(side="left", expand=True, fill="both")

    frame = tk.Frame(root, bg="#067b00", width=600, height=15)
    frame.pack(side="top", fill="x")

    # Creating a new frame for the image buttons with colour #FFFF01
    frameImages = tk.Frame(root, bg="#FFFF01")
    frameImages.pack(side="top", padx=10, pady=5, fill="x")  # Align the frame to the left

    root.mainloop()
