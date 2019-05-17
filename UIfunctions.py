import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
# OpenKeynote
# Copyright Mathias Sønderskov Nielsen 2019


class UIfunctions():
    """
    Handles all the UI functions. called by UI.py
    """

    def open_file_dialog(self,button=""):
        path = filedialog.askopenfilename(
            initialdir=self._filehandler._folder,
            title="Open File",
            filetypes=(("text files", "*.txt"), ("All files", "*.*")))
        if path == "" or path == None:
            #print("Canceled file open")
            self._filehandler.setstatus("Cancelled file open")
            return False
        else:
            self.open_file(path = path)

    def open_file(self, path):
        self._filehandler.setstatus(f"Opening {path}")
        self._filehandler.itemlist = []
        self.itemlist = []
        self._filehandler.path = path
        self._filehandler.read_file(path = path)
        self.e1.delete("1.0", END)
        self.e2.delete("1.0", END)
        self.updateTree()

    def save_file_dialog(self, button=""):
        path = filedialog.asksaveasfilename(
            initialdir=self._filehandler._folder,
            title="Save File",
            filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if path != None and path != "":
            self._filehandler.path = path
            self.save_file(path=path)

    def about(self):
        newframe = Tk()
        newlabel = Label(newframe, text="OpenKeynote by Mathias Sønderskov "\
        "Nielsen.\nFor more info check out www.github.com/sonderwoods")
        newlabel.pack(fill=BOTH,padx = 40, pady=15)
        newframe.title("About OpenKeynote")
        bt1 = Button(newframe, text="Ok", command=newframe.destroy)
        bt1.pack(fill=BOTH,padx = 40, pady=10)
        width = 500
        height = 120
        x = (newframe.winfo_screenwidth() // 2) - (width // 2)
        y = (newframe.winfo_screenheight() // 2) - (height // 2)
        newframe.geometry(f"{width}x{height}+{x}+{y}")

    def new_file(self, button=""):
        self._filehandler.setstatus("Missing New file function")

    def add_item(self, button="", parent=""):
        x = self.root.winfo_pointerx()
        y = self.root.winfo_pointery()
        absx = self.root.winfo_pointerx() - self.root.winfo_rootx()
        absy = self.root.winfo_pointery() - self.root.winfo_rooty()
        self.newframe = Tk()
        self.newframe.title("Add an item")
        self.newframe.geometry(f"400x400+{x+50}+{y-20}")
        catlabel = Label(self.newframe, text="Parent (category):")
        catlabel.grid(row=1, column=0)
        namelabel = Label(self.newframe, text="Name:")
        namelabel.grid(row=2, column=0)
        contentlabel = Label(self.newframe, text="Content")
        contentlabel.grid(row=3, column=0)
        self.cattext = Text(self.newframe, font=("Courier", 13),
                       padx=10, pady=10, highlightthickness=1,
                       borderwidth=1, relief="solid", height=1)
        self.cattext.grid(row=1, column=1, sticky=E+W)
        self.nametext = Text(self.newframe, font=("Courier", 13),
                       padx=10, pady=10, highlightthickness=1,
                       borderwidth=1, relief="solid", height=1)
        self.nametext.grid(row=2, column=1, sticky=E+W)
        self.contenttext = Text(self.newframe, font=("Courier", 13),
                       padx=10, pady=10, highlightthickness=1,
                       borderwidth=1, relief="solid")
        self.contenttext.grid(row=3, column=1, sticky=N+S+E+W)
        self.newframe.columnconfigure(1, weight=1)
        self.newframe.rowconfigure(3, weight=1)
        self.okbtn = ttk.Button(self.newframe, text="OK", width=10)
        self.okbtn.grid(row=4, column=0, sticky=N+W, padx=5, pady=10)
        self.okbtn.config(command=self.submit_item)
        self.cattext.insert(END, parent)
        self.cancelbtn = ttk.Button(self.newframe, text="Cancel",
            command=self.newframe.destroy)
        self.cancelbtn.grid(row=4, column=1, sticky=N+W+E, padx=5, pady=10)
        self.newframe.bind("<Escape>", lambda a: self.newframe.destroy())
        self.nametext.focus()

        #Tried this using lists without luck.
        self.nametext.bind("<Tab>", lambda a:self.focus_on(target=self.contenttext))
        self.nametext.bind("<Shift-Tab>", lambda a:self.focus_on(target=self.cattext))

        self.cattext.bind("<Tab>", lambda a:self.focus_on(target=self.nametext))
        self.cattext.bind("<Shift-Tab>", lambda a:self.focus_on(target=self.cancelbtn))

        self.contenttext.bind("<Tab>", lambda a:self.focus_on(target=self.okbtn))
        self.contenttext.bind("<Shift-Tab>", lambda a:self.focus_on(target=self.nametext))

        self.okbtn.bind("<Tab>", lambda a:self.focus_on(target=self.cancelbtn))
        self.okbtn.bind("<Shift-Tab>", lambda a:self.focus_on(target=self.contenttext))

        self.cancelbtn.bind("<Tab>", lambda a:self.focus_on(target=self.cattext))
        self.cancelbtn.bind("<Shift-Tab>", lambda a:self.focus_on(target=self.okbtn))


    def submit_item(self, button=""):
        name = self.nametext.get("1.0", END).strip()
        parent = self.cattext.get("1.0", END).strip()
        content = self.contenttext.get("1.0", END).replace("\n\r", "\n").strip()
        self._filehandler.add_item(name, parent, content)
        #print(len(self._filehandler.itemlist))
        self.updateTree(selection = name, parent = parent)
        self.newframe.destroy()


    def focus_next(self, event=""):
        event.tk_focusNext().focus()
        return("break")

    def focus_prev(self, event):
        event.tk_focusPrev().focus()
        return("break")
    def focus_on(self, target=""):
        target.focus()
        return("break")



    def add_subitem(self, button=""):
        self._filehandler.setstatus("TODO: Add sub item")



    def rename_item(self, event=None):
        label = "XX"
        self._filehandler.setstatus("TODO: Rename item")
        x = self.root.winfo_pointerx()
        y = self.root.winfo_pointery()
        absx = self.root.winfo_pointerx() - self.root.winfo_rootx()
        absy = self.root.winfo_pointery() - self.root.winfo_rooty()
        self.rnframe = Tk()
        self.rnframe.title(f"OpenKeyote - Renaming {label}")
        self.rnframe.geometry(f"400x100+{x+50}+{y-20}")
        namelabel = Label(self.rnframe, text=f"Renaming : {label}")
        namelabel.grid(row=2, column=0, padx=10, pady=10)
        self.rnname = Entry(self.rnframe, font=("Courier", 13),
                       highlightthickness=1,
                       borderwidth=1, relief="solid")
        self.rnname.grid(row=2, column=1, sticky=E+W, padx=10, pady=10)

        self.rnframe.columnconfigure(1, weight=1)
        self.rnframe.rowconfigure(1, weight=1)
        self.rnokbtn = ttk.Button(self.rnframe, text="OK", width=10)
        self.rnokbtn.grid(row=4, column=0, sticky=N+W, padx=5, pady=10)
        self.rnokbtn.config(command=self.submit_remame)
        self.rncancelbtn = ttk.Button(self.rnframe, text="Cancel",
            command=self.rnframe.destroy)
        self.rncancelbtn.grid(row=4, column=1, sticky=N+W+E, padx=5, pady=10)
        self.rnframe.bind("<Escape>", lambda a: self.rnframe.destroy())
        self.rnname.focus()

        #Tried this using lists without luck.
        self.rnname.bind("<Tab>", lambda a:self.focus_on(target=self.self.rnokbtn))
        self.rnname.bind("<Shift-Tab>", lambda a:self.focus_on(target=self.rncancelbtn))

        self.rnokbtn.bind("<Tab>", lambda a:self.focus_on(target=self.rncancelbtn))
        self.rnokbtn.bind("<Shift-Tab>", lambda a:self.focus_on(target=self.rnname))

        self.rncancelbtn.bind("<Tab>", lambda a:self.focus_on(target=self.rnname))
        self.rncancelbtn.bind("<Shift-Tab>", lambda a:self.focus_on(target=self.rnokbtn))

    def submit_rename(self, event=None):
        pass


    def change_parent(self, button=""):
        self._filehandler.setstatus("TODO: Change parent")

    def save_file(self, button="", path=""):
        if path != "":
            self._filehandler.write_file(path)
        else:
            if self._filehandler.path != "" and self._filehandler.path != None:
                self._filehandler.write_file(self._filehandler.path)
            else:
                self._filehandler.setstatus("tried to save unknown path")

    def changeselection(self, button):
        """
        what happens when changing selection in the treeview..
        """
        itemlist = self._filehandler.itemlist
        itemname = self.l1.focus()
        if len(itemlist) == 0:
            return

        self.previeweditem = self.l1.focus()
        try:
            parentname = [i["parent"]
                          for i in itemlist if i["name"] == itemname][0]
            index = [i for i, j in enumerate(
                itemlist) if j["name"] == itemname][0]
        except IndexError:
            parentname = itemlist[0]["name"]
            index = 0
        if len(parentname) > 1:
            self.tx1.config(text="previewing: {} ( parent: {} )".format(
                itemname, parentname))
        else:
            self.tx1.config(text="previewing: {}".format(itemname))

        self.e1.delete("1.0", END)
        self.e1.insert(END, itemlist[index]["content"])
        self.parentname = parentname
        if len(self.parentname) > 0:
            self.vbs[0].config(text=f"New Item ({self.parentname})")
            self.vbs[1].config(state=DISABLED)
        else:
            self.vbs[0].config(text=f"New Item")
        if len(self.get_all_children(self.l1, self.previeweditem)) > 0:
            self.vbs[2].config(text=f"Delete {self.previeweditem} and subs")
        else:
            self.vbs[2].config(text=f"Delete {self.previeweditem}")
        if len(self.previeweditem) > 0:
            self.vbs[1].config(state=NORMAL)
            self.vbs[1].config(text=f"New Subitem ({self.previeweditem})")
        else:
            self.vbs[1].config(state=DISABLED)
            self.vbs[1].config(text=f"New Subitem")

    def select_all(self, event=None):
        self.root.focus_get().tag_add('sel', '1.0', 'end-1c')

    # def copy_text(self, event=None):
    #     print("x")
    #     self.root.focus_get().event_generate("<<Copy>>")
    #     cb = self.root.clipboard_get()
    #     self.root.clipboard_clear()
    #     self.root.clipboard_append(cb[:-2])



    def edititem(self, button=""):
        """
        copies text from e1 to e2
        """
        itemlist = self._filehandler.itemlist
        self.e2.delete("1.0", END)
        self.e2.insert(END, self.e1.get("1.0", "end-1c"))

        self.editeditem = self.previeweditem
        name = self.editeditem
        self.parentname = [i["parent"] for i in itemlist if i["name"] == name]
        index = [i for i, j in enumerate(itemlist) if j["name"] == name]
        # TODO eventualt [0] after name] above 2 lines.
        if len(self.parentname) > 1:
            self.tx2.config(text="Editing: {} ( parent: {} )".format(
                name, parentname))
        else:
            self.tx2.config(text="Editing: {}".format(name))

    def treeview_sort_column(self, tv, col, reverse):
        object = self.l1
        l = [(object.set(k, col), k) for k in object.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            object.move(k, '', index)

        # reverse sort next time
        #TODO
        object.heading(col, command=lambda: \
                   self.treeview_sort_column(tv, col, not reverse))

    def saveitem(self, button=""):
        """
        saves text from gui back into main dictionary
        and redraws tree, and selects where we were.
        1) resave Dictionary
        2) update "edit field"
        """

        newcontent = self.e2.get("1.0", "end-1c")
        for i, k in enumerate(self.itemlist):    # update Dictionary
            if k["name"] == self.editeditem:
                self._filehandler.itemlist[i]["content"] = newcontent
        if self.previeweditem == self.editeditem:
            self.e1.delete("1.0", END)
            self.e1.insert(END, newcontent)

    def __str__(self):
        text = ["First five lines:"]
        for i in self.itemlist[0:5]:
            text.append(f"name: {i['name']}, \tcontent: {i['content']}, \
                \tparent: {i['parent']}")
        return "\n".join(text)

    def fixUI(self, win=None):
        """
        Resizes with 1 pixel to avoid mainUI bugs in mojave
        """
        if os.name != "nt":
            if win == None:
                win = self.root

            a = win.winfo_geometry().split('+')[0]
            b = a.split('x')
            w = int(b[0])
            h = int(b[1])
            win.geometry('{}x{}'.format(w+1, h+1))

    def get_all_children(self,tree,item=""):
        children = tree.get_children(item)
        for child in children:
            children += self.get_all_children(tree, child)
        return children

    def delete_item(self, button=""):
        mytree = self.get_all_children(self.l1, self.previeweditem)
        for i in mytree:
           self._filehandler.delete_item(i)
        self._filehandler.delete_item(self.previeweditem)
        self.updateTree()

    def updateTree(self, selection=None, parent=None, op=""):
        if selection == None:
            selection = self.l1.focus()

        self.itemlist = self._filehandler.itemlist  # gets from FileHandler
        itemlist = self.itemlist[:]   # temp list that we can delete from
        uniquenames = set()
        print(len(itemlist))
        on_off_dict = {}
        previous_tree = self.get_all_children(self.l1)
        for item in previous_tree:
            name = self.l1.item(item)['text']
            open = self.l1.item(item)['open']
            if open == 1:
                open = True
            else:
                open = False
            on_off_dict[name] = open


        self.l1.delete(*self.l1.get_children())
        while len(itemlist) > 0:
            for i, item in enumerate(itemlist):
                if item["name"] not in uniquenames:
                    if item["parent"] == "":
                        try:
                            self.l1.insert(
                                '', 'end', item["name"], text=item["name"])
                            if op == "Expand":
                                self.l1.item(item["name"], open=True)
                            elif op == "Collapse":
                                self.l1.item(item["name"], open=False)
                            else:
                                if item["name"] in on_off_dict.keys():
                                    if on_off_dict[item["name"]]:
                                        self.l1.item(item["name"], open=True)
                                    else:
                                        self.l1.item(item["name"], open=False)
                        except TclError:
                            self._filehandler.setstatus(f'Error: Tried to add item\
                             {item["name"]}, but it was already in the list')
                        del itemlist[i]
                        uniquenames.add(item["name"])
                    elif item["parent"] in uniquenames:  # it exists, so lets add to it.
                        self.l1.insert(item["parent"], 'end',
                                       item["name"], text=item["name"])
                        del itemlist[i]
                        uniquenames.add(item["name"])
                else:
                    del itemlist[i]
        if parent != None and parent != "":
            self.l1.item(parent, open=True)
        self.l1.selection_clear()
        self.l1.selection_set(selection)
        self.l1.focus(selection)


        #self.l1.focus_set

    def close_file(self):
        self.e1.delete("1.0", END)
        self.e2.delete("1.0", END)
        self._filehandler.clear_memory()
        self.l1.delete(*self.l1.get_children())

if __name__ == '__main__':
    from main import main
    main()
