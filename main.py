#make sure you upload in your current repl
#Import all necessary libraries
#PIL (Phyton Imaging Library) provide image editing capbabilites to the phyton interpreter
from thinker import *
from PIL import Image, ImageTk

#create a window with a title bar and set its geometry as well
root = TK()
root.title('image')
root.geometry('400x400')

#Now use Image.open to open abd identify the given image file
upload Image.open("premium_photo-1666672388644-2d99f3feb9f1.jpg")

#convert this image into Tkinter compatible image
Image = ImageTK.Photoimage(upload)

#Add Image to Tkinter Label
label = Label(root, Image=Image, height=300, Width=300 )
label.place(x=50, y=0)
label2 = Label(root, text="This is how to add Image in Tkinter Window ")
label2.place(x=50, y=360)

#Run he application
root.mainloop()