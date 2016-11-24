import Tkinter as tk
import Database as DB
import Widgets as wd

class NewStudent:
    'App for creating a new student in the database'
    #################   CONSTRUCTOR   #################
    def __init__(self, db):
        '''
        Initialize a gui for the insertion of students infomation'
        INPUT: db - the databse
        '''
        #create a root container
        self.root = tk.Tk()
        self.root.title("New Student")

        #Labels: to the left of the window
        idL = wd.LabelWidget(self.root, 0, 0, "ID")
        firstL = wd.LabelWidget(self.root, 0, 1, "First")
        lastL = wd.LabelWidget(self.root, 0, 2, "Last")
        yearL = wd.LabelWidget(self.root, 0, 3, "Year")

        #Entries: to the right of the window
        idE = wd.EntryWidget(self.root, 1, 0, "ID")
        firstE = wd.EntryWidget(self.root, 1, 1, "First")
        lastE = wd.EntryWidget(self.root, 1, 2, "Last")
        yearE = wd.EntryWidget(self.root, 1, 3, "Year")

        #Log display to the gui
        log = wd.LabelWidget(self.root, 0, 5, "Status", 30)
        #having the log display to span 2 columns
        log.grid(columnspan = 2)

        def ins():
            'method to call for the Submit button'
            try:
                #interaction witht the Database object
                db.insStudent(idE.getVal(), firstE.getVal(), lastE.getVal(), int(yearE.getVal()))
                #report that the insertion is success
                log.set("Success")
            except Exception, value:
                #If insertion fail, report to the Log display
                log.set(value)

        #A Submit button
        submit = tk.Button(self.root, text="Submit", command = ins)
        submit.grid(column = 1, row=4)

        #make the window appears
        self.root.mainloop()



if __name__ == "__main__":
    #connecting with the database
    db = DB.Database('database/cup.db')
    new = NewStudent(db)
