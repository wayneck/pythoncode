# -*- coding:gb2312 -*-
from tkinter import *
root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeigh = root.winfo_screenheight()
screenCanvas=Canvas(root,width=screenWidth, height=screenHeigh,bg="blue")

mainFrame =LabelFrame(root,text="主frame",width=120)
mainFrame.pack(fill="both", expand="yes")



pointFrame = LabelFrame(mainFrame,text="坐标",)
pointFrame.pack(side=LEFT)
currentMode = Entry(pointFrame,width=5)
startpointx = Entry(pointFrame,width=5)
startpointy = Entry(pointFrame,width=5)
endpointx = Entry(pointFrame,width=5)
endpointy = Entry(pointFrame,width=5)

posizex,posizey=[0,0]
posizexx,posizeyy=[0,0]
cavasStatus=0
root.geometry('200x100+100+100')
captureButton = Button(root)

def modeValue(mvalue):
    print (mvalue)
    currentMode.insert(0,mvalue)
def mouseCallback(event):    
    global cavasStatus
    screenCanvas.focus_set()
    global posizex,posizey,posizexx,posizeyy
    if cavasStatus == 0 :
        posizex,posizey=[event.x, event.y]
        print ("clicked at start", posizex, posizey)
        startpointx.insert(0,posizex)
        startpointy.insert(0,posizey)
        cavasStatus=1
    else:
        posizexx,posizeyy=[event.x, event.y]
        print ("clicked at end", posizexx, posizeyy)
        endpointx.insert(0,posizexx)
        endpointy.insert(0,posizeyy)
        screenCanvas.unbind("<Button-1>")
        root.attributes("-alpha",1.0)      
        screenCanvas.pack(expand= 0)
        cavasStatus = 0
        root.geometry('200x100+100+100')
        captureButton = Button(root,text="Capture",height=5).pack()
        #self.screenCanvas.destroy()
        #captureButton.pack(expand= 1)
    


def captureScreen():
    #frame.geometry('1920x1080+0+0')
    #captureButton = Button(root,text="Capture",width=0,height=0).pack()
    root.geometry('1920x1080+0+0')
    #captureButton.pack(expand= 0)
    #captureOkButton.pack(expand= 0)
    root.attributes("-alpha",0.8)
    screenCanvas.bind("<Button-1>", mouseCallback)
    #screenCanvas.bind("<Button-1>", mouseCallback)
    #print ("clicked at end:", endx, endy)
    screenCanvas.pack(expand= 1)
    

#b.geometry('20x20+0+0')
v = IntVar()
r1 = Radiobutton(mainFrame, text="同学/同事介绍", variable=v, value=1,command = modeValue(1)).pack(anchor=W)
r2 = Radiobutton(mainFrame, text="老婆大人介绍", variable=v, value=2,command = modeValue(2)).pack(anchor=W)
r3 = Radiobutton(mainFrame, text="老师/学长介绍", variable=v, value=3,command = modeValue(3)).pack(anchor=W)

captureButton = Button(mainFrame,text="Capture",command=captureScreen)
captureButton.pack(side=LEFT)

currentMode.pack(side=LEFT)
startpointx.pack(side=LEFT)
startpointy.pack(side=LEFT)
endpointx.pack(side=LEFT)
endpointy.pack(side=LEFT)
#captureOkButton = Button(root,text="ok",width=19,).pack()
#screenCanvas.unpack()
root.mainloop()
