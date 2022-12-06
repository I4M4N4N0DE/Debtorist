import time
import os
import json as js
import tkinter as Tki # hahahahah xdd

# here, put your own path to your file in the quotations
# this path will be the path your PC will use to access and modify that file
# the file's name can be optional, but it has to end with ".json"
path = "C:/Users/tesla/OneDrive/Dokumenty/list.json"

# a class containing all the inner functions of the program - Backend
class Backend:
    
    # a function which creates the data and stores them
    
    def saveInfo():
        
        try:
            
            cashtype = input("Enter your currency: ")
        
            while True:
                name = input("Enter your name: ")
                surname = input("Enter your surname: ")
                try:
                    while True: 
                        age = int(input("Enter your age: "))
                        sex = input("Enter your gender: ")
        
                        while True:
                            try:
                                debt = int(input("How much is your debt?: "))
                                paid = int(input("How much of that debt is paid?: "))
                                print(name)
                                time.sleep(0.5)
                                print(surname)
                                time.sleep(0.5)
                                print("")
                                if age == 1:
                                    print(age, " year old")
                                else:
                                    print(age, " years old")
                                time.sleep(0.5)
                                print(sex)
                                time.sleep(1)
                                print("")
                                if debt <= 0:
                                    print("Well, that can't be a debt.")
                                    print("Again: ")
                                    
                                print("The debt is: " + str(debt) + cashtype)
                                time.sleep(0.5)
                                print("The paid amount is: " + str(paid) + " "  + cashtype)
                                print("Is this info OK? [Y/N]")
                                check = input()
        
                                if check == "Y":
            
                                    try:
                                        
                                        os.remove(path)
                       
                                        template = {"name": name, "surname": surname, "age": age, "sex": sex, "debt": debt, "paid": paid}
            
                                        personfile = js.dumps(template, ensure_ascii=False)
                                        with open(path, "a") as infoSave:
                                            infoSave.write(personfile)
                                            Gui.warningWindow("Data are saved.")
                                            return
                            
                                    except FileNotFoundError:
                       
                                        template = {"name": name, "surname": surname, "age": age, "sex": sex, "debt": debt, "paid": paid}
            
                                        personfile = js.dumps(template, ensure_ascii=False)
                                        with open(path, "a") as infoSave:
                                            infoSave.write(personfile)
                                            Gui.warningWindow("Data are saved.")
                                            return
                                        
                                elif check == "N":
                                    Backend.saveInfo()
                                else:
                                    print("I don't understand - again: ")
                            except ValueError:
                                print("That wasn't a number - again: ")
                            
                            except RecursionError:
                                quit()
                                
                except ValueError:
                        print("That's not an age - again: ")
        
        except RuntimeError:
            lambda:[quit(), Gui.main()]
    
    # a funtion which changes the data in the file
    def changeInfo():
    
        try:
            with open(path, "r") as infoRead:
                declare = js.load(infoRead)
            
            print("Actual debt is: ", declare["debt"]) 
            print("Actual paid amount is: ", declare["paid"]) 
            olddebt = declare["debt"]
            oldpaidstate = declare["paid"]
            
            try:    
                indebt = int(input("Enter a new debt: "))
                
                if indebt != olddebt:
                    declare["debt"] = indebt
                    print("The new debt is: ", declare["debt"])
                
                else:
                    Gui.warningWindow("The debt didn't change.")
            
            except ValueError:
                print("That wasn't a number!")
                Backend.changeInfo()
            
            except RuntimeError:
                Gui.warningWindow("Restart the program.")
                
            try:
                paidstate = int(input("Enter how much you've paid: "))
                
                if paidstate != oldpaidstate:
                    declare["paid"] = paidstate
                    print("The new paid amount is: ", declare["paid"])
                
                else:
                    Gui.warningWindow("The paid amount didn't change.")
                    
            except ValueError:
                print("That wasn't a number!")
                Backend.changeInfo()
            
            except RecursionError:
                Gui.warningWindow("Restart the program.")
                
            with open(path, "w") as updateData:
                donework = js.dumps(declare, ensure_ascii=False)
                updateData.write(donework)
                    
            Gui.warningWindow("Data are updated.")
                    
        except js.decoder.JSONDecodeError:
            Gui.warningWindow("The file is empty, it has to be deleted.")
            Backend.deleteInfo()
                
        except FileNotFoundError:
            Gui.warningWindow("The file doesn't exist, data can't be accessed.")
            
        except RuntimeError:
            lambda:[quit(), Gui.main()]
        
    # a function which deletes data from the file
    def deleteInfo():
    
        try:
            os.remove(path)
            Gui.warningWindow("The file is deleted.")
    
        except FileNotFoundError:
            Gui.warningWindow("There's no file created!")
    
    # a warning function if an existing file is supposed to be erased for a new one      
    def fileWarn():
        
        if os.path.exists(path):
            Gui.fileWindow("A database already exists! Do you really want to create new?")
        else:
            Backend.saveInfo()

# a graphic class named Gui
class Gui:
    
    # a function which asks you if the file will be really deleted
    def fileWindow(warn):
        
        warning = Tki.Tk()
        warning.geometry("250x100")
        warning.title("WARNING")
    
        te = Tki.Text(warning, height = 30, width=30)
        cont = warn
    
        te.pack()
        te.insert(Tki.END, cont)

        Tki.Button(warning, text="Yes", command=Backend.deleteInfo).place(x=70, y=70)
        Tki.Button(warning, text="No", command=warning.destroy).place(x=130, y=70)
        warning.mainloop()
    
    # a function with graphical warning
    def warningWindow(text):
        
        warning = Tki.Tk()
        warning.geometry("250x100")
        warning.title("WARNING")
    
        te = Tki.Text(warning, height = 30, width=30)
        te.insert(Tki.END, text)
        Tki.Button(warning, text="OK", command=warning.destroy).place(x=100, y=70)
        te.pack()
        warning.attributes('-topmost', True)
    
    # a function which lets you confirm deleting the file
    def deleteInfoGui():
    
        warning = Tki.Tk()
        warning.geometry("250x100")
        warning.title("WARNING")
    
        te = Tki.Text(warning, height=30, width=30)
        cont = "By clicking you'll delete the file and lose all data!"
    
        te.pack()
        te.insert(Tki.END, cont)

        Tki.Button(warning, text="Confirm", command=Backend.deleteInfo).place(x=100, y=70)
        
        warning.mainloop()
    
    def listGui():
        
        try:
            listwin = Tki.Tk()
            listwin.geometry("300x130")
            listwin.title("INFO")
            
            with open(path, "r") as getList:
                gotlist = js.load(getList)
            
            lte = Tki.Text(listwin, height=30, width=30)
            lte.pack()
            lte.insert(Tki.END, "Name: " + gotlist["name"] + "\n" + "Surname: " + gotlist["surname"] + "\n" + "Age: " + str(gotlist["age"]) + "\n" + "Gender: " + gotlist["sex"] + "\n" + "Debt: " + str(gotlist["debt"]) + "\n" + "Paid: " + str(gotlist["paid"]))
            Tki.Button(listwin, text="OK", command=listwin.destroy).place(x=140, y=100)
            listwin.attributes('-topmost', True)
        
        except FileNotFoundError:
            listwin.destroy()
            Gui.warningWindow("The file doesn't exist," + "\n" + "data can't be displayed!")
            
            
    # the main function which opens the opening window at the start of the program
    # it lets you choose what you want to do
    def main():
        
        try:
            
            if os.path.exists(path):
                Gui.warningWindow("Database was found.")
            else:
                Gui.warningWindow("Database wasn't found.")
            
            window = Tki.Tk()
            window.geometry("300x150")
            window.title("DEBTORIST")
        
            Tki.Button(window, text="Create a record", command=Backend.fileWarn).place(x=20, y=10)
            Tki.Button(window, text="Change record data", command=Backend.changeInfo).place(x=20, y=40)
            Tki.Button(window, text="Delete the record", command=Gui.deleteInfoGui).place(x=20, y=70)
            Tki.Button(window, text="Display the data", command=Gui.listGui).place(x=20, y=100)
            Tki.Button(window, text="Refresh", command=lambda:[window.destroy(), Gui.main()]).place(x=210, y=115)
    
            with open(path, "r") as getDebt:
                infoSet = js.load(getDebt)
        
            debtstate = infoSet["debt"]
            paidstate = infoSet["paid"]
        
            percont = (paidstate / debtstate) * 100
            
            roundedpercont = round(percont)
        
            info = Tki.Text(window, height=4, width=15)
            info.pack(side=Tki.RIGHT)
            info.insert(Tki.END, "Debt: " + str(debtstate) + "\n" + "Paid: ", "\n", str(roundedpercont) + "%")
            window.mainloop()
        
        except FileNotFoundError:
            
            window.destroy()
            
            window = Tki.Tk()
            window.geometry("300x150")
            window.title("DEBTORIST")
        
            Tki.Button(window, text="Create a record", command=Backend.fileWarn).place(x=20, y=10)
            Tki.Button(window, text="Change record data", command=Backend.changeInfo).place(x=20, y=40)
            Tki.Button(window, text="Delete the record", command=Gui.deleteInfoGui).place(x=20, y=70)
            Tki.Button(window, text="Display the data", command=Gui.listGui).place(x=20, y=100)
            Tki.Button(window, text="Refresh", command=lambda:[window.destroy(), Gui.main()]).place(x=210, y=115)
        
            cont = "Debt: "
            cont2 = "Paid: "
        
            text = Tki.Text(window, height=4, width=15)
            text.pack(side=Tki.RIGHT)
            text.insert(Tki.END, cont + "\n" + cont2)
            window.mainloop()
        
        except js.JSONDecodeError:
            
            window.destroy()
            
            window = Tki.Tk()
            window.geometry("300x150")
            window.title("DEBTORIST")
        
            Tki.Button(window, text="Create a record", command=Backend.fileWarn).place(x=20, y=10)
            Tki.Button(window, text="Change record data", command=Backend.changeInfo).place(x=20, y=40)
            Tki.Button(window, text="Delete the record", command=Gui.deleteInfoGui).place(x=20, y=70)
            Tki.Button(window, text="Display the data", command=Gui.listGui).place(x=20, y=100)
            Tki.Button(window, text="Refresh", command=lambda:[window.destroy(), Gui.main()]).place(x=210, y=115)
        
            cont = "Debt: "
            cont2 = "Paid: "
        
            text = Tki.Text(window, height=4, width=15)
            text.pack(side=Tki.RIGHT)
            text.insert(Tki.END, cont + "\n" + cont2)
            window.mainloop()

Gui.main()    
