__author__ = 'zhangcheng'

from Tkinter import *


def write_info(*args):
    f = open('objinfo.cfg','w')
    #f.writelines((bb,lb,bl,ll))
    f.writelines(','.join(args))
    print args
    f.close()


class MyDialog:
    def __init__(self, parent):

        diag = self.diag = Toplevel(parent)

        Label(diag, text="B").pack()
        self.bb = Entry(diag)
        self.bb.pack()

        Label(diag, text="b").pack()
        self.lb = Entry(diag)
        self.lb.pack()

        Label(diag, text="L").pack()
        self.bl = Entry(diag)
        self.bl.pack()

        Label(diag, text="l").pack()
        self.ll = Entry(diag)
        self.ll.pack()

        b = Button(diag, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        write_info(self.bb.get(),self.lb.get(),
                   self.bl.get(),self.ll.get())

        self.diag.destroy()

if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    d = MyDialog(root)

    root.wait_window(d.diag)