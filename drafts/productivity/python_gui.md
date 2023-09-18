
# Creating a Python GUI for image processing

## Library

There are three main libraries, TKinter, PyQT and wxPython. I will use tkinter because it is included by default in Python. See [the python docs](https://docs.python.org/3/library/tkinter.html).

## Learning `tkinter`

### Check 

Try running `python -m tkinter` to check that it works beautifully.

### On the underlying software

Not a single library but many modules: Tcl (programming language), Tk (Tcl package), Ttk (better widgets)
  
> Internally, Tk and Ttk use facilities of the underlying operating system, i.e., Xlib on Unix/X11, Cocoa on macOS, GDI on Windows.
When your Python application uses a class in Tkinter, e.g., to create a widget, the tkinter module first assembles a Tcl/Tk command string. It passes that Tcl command string to an internal _tkinter binary module, which then calls the Tcl interpreter to evaluate it. The Tcl interpreter will then call into the Tk and/or Ttk packages, which will in turn make calls to Xlib, Cocoa, or GDI.

### How to do it
We use frames or widgets that can contain each other in a hierarchical way. Moreover, we should create a main window and then run a loop in order for the program to run.

For instance, take the following app:

```python
import PIL.Image
from PIL import ImageTk
from Tkinter import *    


class ExampleApp(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.x = self.y = 0
        self.canvas = Canvas(self,  cursor="cross")

        self.sbarv=Scrollbar(self,orient=VERTICAL)
        self.sbarh=Scrollbar(self,orient=HORIZONTAL)
        self.sbarv.config(command=self.canvas.yview)
        self.sbarh.config(command=self.canvas.xview)

        self.canvas.config(yscrollcommand=self.sbarv.set)
        self.canvas.config(xscrollcommand=self.sbarh.set)

        self.canvas.grid(row=0,column=0,sticky=N+S+E+W)
        self.sbarv.grid(row=0,column=1,stick=N+S)
        self.sbarh.grid(row=1,column=0,sticky=E+W)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.rect = None

        self.start_x = None
        self.start_y = None

        self.im = PIL.Image.open("logo.png")
        self.wazil,self.lard=self.im.size
        self.canvas.config(scrollregion=(0,0,self.wazil,self.lard))
        self.tk_im = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)   


    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        # create rectangle if not yet exist
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')

    def on_move_press(self, event):
        curX = self.canvas.canvasx(event.x)
        curY = self.canvas.canvasy(event.y)

        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if event.x > 0.9*w:
            self.canvas.xview_scroll(1, 'units') 
        elif event.x < 0.1*w:
            self.canvas.xview_scroll(-1, 'units')
        if event.y > 0.9*h:
            self.canvas.yview_scroll(1, 'units') 
        elif event.y < 0.1*h:
            self.canvas.yview_scroll(-1, 'units')

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)    

    def on_button_release(self, event):
        pass    

if __name__ == "__main__":
    root=Tk()
    app = ExampleApp(root)
    app.pack()
    root.mainloop()
```

This seems overly complicated so I'll explode opencv GUI to the maximum of its capabilities.
 

## My GUI

I want a GUI with the following capabilities (minimum):

- select a polygon mask on the image 
- 






