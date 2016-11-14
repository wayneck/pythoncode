from tkinter import *

root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeigh = root.winfo_screenheight()
screenCanvas=Canvas(root,width=screenWidth, height=screenHeigh)
posizex,posizey=[0,0]
posizexx,posizeyy=[0,0]
cavasStatus=0
root.geometry('100x100+100+100')
captureButton = Button(root)
def mouseCallback(event):    
    global cavasStatus
    screenCanvas.focus_set()
    global posizex,posizey,posizexx,posizeyy
    if cavasStatus == 0 :
        posizex,posizey=[event.x, event.y]
        print ("clicked at start", posizex, posizey)
        cavasStatus=1
    else:
        posizexx,posizeyy=[event.x, event.y]
        print ("clicked at end", posizexx, posizeyy)
        screenCanvas.unbind("<Button-1>")
        root.attributes("-alpha",1.0)      
        screenCanvas.pack(expand= 0)
        cavasStatus = 0
        root.geometry('100x100+100+100')
        captureButton = Button(root,text="Capture",height=5).pack()
        #self.screenCanvas.destroy()
        #captureButton.pack(expand= 1)
    


def captureScreen():
    #frame.geometry('1920x1080+0+0')
    captureButton = Button(root,text="Capture",width=0,height=0).pack()
    root.geometry('1920x1080+0+0')
    #captureButton.pack(expand= 0)
    #captureOkButton.pack(expand= 0)
    root.attributes("-alpha",0.8)
    screenCanvas.bind("<Button-1>", mouseCallback)
    #screenCanvas.bind("<Button-1>", mouseCallback)
    #print ("clicked at end:", endx, endy)
    screenCanvas.pack(expand= 1)
    

#b.geometry('20x20+0+0')
captureButton = Button(root,text="Capture",width=19,command=captureScreen).pack()
#captureOkButton = Button(root,text="ok",width=19,).pack()
#screenCanvas.unpack()
root.mainloop()
