import time
import os
import json as js
import tkinter as Tki # hahahahah xdd

# zde si do uvozovek vložte vlastní cestu k souboru, jméno může být libovolné
# tato cesta bude místo, kde se bude ukládat soubor s daty
# soubor musí být zakončen ".json"
path = "C:/Users/tesla/OneDrive/Dokumenty/list.json"

# třída obsahující funkční kostru programu - Backend
class Backend:
    
    # funkce pracující s vložením dat
    
    def saveInfo():
        
        try:
            
            cashtype = input("Zadej symbol/zkratku měny, se kterou se bude pracovat: ")
        
            while True:
                name = input("Zadej křestní jméno: ")
                surname = input("Zadej příjmení: ")
                try:
                    while True: 
                        age = int(input("Zadej věk: "))
                        sex = input("Zadej pohlaví: ")
        
                        while True:
                            try:
                                debt = int(input("Zadej dlužnou částku: "))
                                paid = int(input("Zadej kolik máš splaceno: "))
                                print(name)
                                time.sleep(0.5)
                                print(surname)
                                time.sleep(0.5)
                                print("")
                                if age <= 4:
                                    print(age, " roky")
                                elif age == 1:
                                        print(age, " rok")
                                else:
                                    print(age, " let")
                                time.sleep(0.5)
                                print(sex)
                                time.sleep(1)
                                print("")
                                if debt <= 0:
                                    print("Tak to není dluh.")
                                    
                                print("Dlužná částka je: " + str(debt) + cashtype)
                                time.sleep(0.5)
                                print("Splacená částka z dlužné je: " + str(paid) + " "  + cashtype)
                                print("Jsou údaje správné? [A/N]")
                                check = input()
        
                                if check == "A":
            
                                    try:
                                        
                                        os.remove(path)
                       
                                        template = {"name": name, "surname": surname, "age": age, "sex": sex, "debt": debt, "paid": paid}
            
                                        personfile = js.dumps(template, ensure_ascii=False)
                                        with open(path, "a") as infoSave:
                                            infoSave.write(personfile)
                                            Gui.warningWindow("Údaje zapsány.")
                                            return
                            
                                    except FileNotFoundError:
                       
                                        template = {"name": name, "surname": surname, "age": age, "sex": sex, "debt": debt, "paid": paid}
            
                                        personfile = js.dumps(template, ensure_ascii=False)
                                        with open(path, "a") as infoSave:
                                            infoSave.write(personfile)
                                            Gui.warningWindow("Údaje zapsány.")
                                            return
                                        
                                elif check == "N":
                                    Backend.saveInfo()
                                else:
                                    print("Nerozumím - znovu: ")
                            except ValueError:
                                print("To nebyla částka - znovu: ")
                            
                            except RecursionError:
                                quit()
                                
                except ValueError:
                        print("To není věk - znovu: ")
        
        except RuntimeError:
            lambda:[quit(), Gui.main()]
    
    # funkce pracující se změnou dlužné částky
    def changeInfo():
    
        try:
            with open(path, "r") as infoRead:
                declare = js.load(infoRead)
            
            print("Aktuální dlužná částka je: ", declare["debt"]) 
            print("Aktuální splacená částka je: ", declare["paid"]) 
            olddebt = declare["debt"]
            oldpaidstate = declare["paid"]
            
            try:    
                indebt = int(input("Zadejte novou dlužnou částku: "))
                
                if indebt != olddebt:
                    declare["debt"] = indebt
                    print("Dlužná částka po změně je: ", declare["debt"])
                
                else:
                    Gui.warningWindow("Dlužná částka se nezměnila.")
            
            except ValueError:
                print("To nebylo číslo!")
                Backend.changeInfo()
            
            except RuntimeError:
                Gui.warningWindow("Restartujte program.")
                
            try:
                paidstate = int(input("Zadejte kolik máte splaceno: "))
                
                if paidstate != oldpaidstate:
                    declare["paid"] = paidstate
                    print("Splacená částka po změně je: ", declare["paid"])
                
                else:
                    Gui.warningWindow("Splacená částka se nezměnila.")
                    
            except ValueError:
                print("To nebylo číslo!")
                Backend.changeInfo()
            
            except RecursionError:
                Gui.warningWindow("Restartujte program.")
                
            with open(path, "w") as updateData:
                donework = js.dumps(declare, ensure_ascii=False)
                updateData.write(donework)
                    
            Gui.warningWindow("Databáze aktualizována.")
                    
        except js.decoder.JSONDecodeError:
            Gui.warningWindow("Soubor je prázdný, nutno smazat.")
            Backend.deleteInfo()
                
        except FileNotFoundError:
            Gui.warningWindow("Soubor neexistuje, nelze načíst data.")
            
        except RuntimeError:
            lambda:[quit(), Gui.main()]
        
    # funkce na smazání souboru s daty
    def deleteInfo():
    
        try:
            os.remove(path)
            Gui.warningWindow("Soubor byl smazán.")
    
        except FileNotFoundError:
            Gui.warningWindow("Soubor neexistuje.")
    
    # varovná funkce při přemazání databáze        
    def fileWarn():
        
        if os.path.exists(path):
            Gui.fileWindow("Databáze již existuje! Chcete opravdu vytvořit novou?")
        else:
            Backend.saveInfo()

# vzhledová třída Gui
class Gui:
    
    # funkce grafické volby smazání dat ze souboru
    def fileWindow(warn):
        
        warning = Tki.Tk()
        warning.geometry("250x100")
        warning.title("UPOZORNĚNÍ")
    
        te = Tki.Text(warning, height = 30, width=30)
        cont = warn
    
        te.pack()
        te.insert(Tki.END, cont)

        Tki.Button(warning, text="Ano", command=Backend.deleteInfo).place(x=70, y=70)
        Tki.Button(warning, text="Ne", command=warning.destroy).place(x=130, y=70)
        warning.mainloop()
    
    # funkce grafického upozornění
    def warningWindow(text):
        
        warning = Tki.Tk()
        warning.geometry("250x100")
        warning.title("UPOZORNĚNÍ")
    
        te = Tki.Text(warning, height = 30, width=30)
        cont = text
        te.insert(Tki.END, cont)
        Tki.Button(warning, text="OK", command=warning.destroy).place(x=100, y=70)
        te.pack()
        warning.attributes('-topmost', True)
        
        warning.mainloop()
    
    # funkce potvrzení smazání souboru  
    def deleteInfoGui():
    
        warning = Tki.Tk()
        warning.geometry("250x100")
        warning.title("UPOZORNĚNÍ")
    
        te = Tki.Text(warning, height=30, width=30)
        cont = "Kliknutím níže smažete soubor a přijdete o veškerá data!"
    
        te.pack()
        te.insert(Tki.END, cont)

        Tki.Button(warning, text="Potvrdit", command=Backend.deleteInfo).place(x=100, y=70)
        
        warning.mainloop()
    
    def listGui():
        
        try:
            listwin = Tki.Tk()
            listwin.geometry("300x130")
            listwin.title("ÚDAJE")
            
            with open(path, "r") as getList:
                gotlist = js.load(getList)
            
            lte = Tki.Text(listwin, height=30, width=30)
            lte.pack()
            lte.insert(Tki.END, "Jméno: " + gotlist["name"] + "\n" + "Příjmení: " + gotlist["surname"] + "\n" + "Věk: " + str(gotlist["age"]) + "\n" + "Pohlaví: " + gotlist["sex"] + "\n" + "Dluh: " + str(gotlist["debt"]) + "\n" + "Splaceno: " + str(gotlist["paid"]))
            Tki.Button(listwin, text="OK", command=listwin.destroy).place(x=140, y=100)
            listwin.attributes('-topmost', True)
        
        except FileNotFoundError:
            listwin.destroy()
            Gui.warningWindow("Soubor neexistuje," + "\n" + "data nemohou být vypsána.")
            
            
    # hlavní spouštěcí okno programu s volbou činností a zobrazením stavu
    def main():
        
        try:
            
            window = Tki.Tk()
            window.geometry("300x150")
            window.title("DLUHAŘ")
        
            Tki.Button(window, text="Vytvořit záznam", command=Backend.fileWarn).place(x=20, y=10)
            Tki.Button(window, text="Změnit data záznamu", command=Backend.changeInfo).place(x=20, y=40)
            Tki.Button(window, text="Ostranit databázi", command=Gui.deleteInfoGui).place(x=20, y=70)
            Tki.Button(window, text="Zobrazit dlužníka", command=Gui.listGui).place(x=20, y=100)
            Tki.Button(window, text="Obnovit", command=lambda:[window.destroy(), Gui.main()]).place(x=210, y=115)
    
            with open(path, "r") as getDebt:
                infoSet = js.load(getDebt)
        
            debtstate = infoSet["debt"]
            paidstate = infoSet["paid"]
        
            percont = (paidstate / debtstate) * 100
            
            roundedpercont = round(percont)
        
            info = Tki.Text(window, height=4, width=15)
            info.pack(side=Tki.RIGHT)
            info.insert(Tki.END, "Dluh: " + str(debtstate) + "\n" + "Splaceno: " + str(roundedpercont) + "%")
            window.mainloop()
        
        except FileNotFoundError:
            
            window.destroy()
            
            window = Tki.Tk()
            window.geometry("300x150")
            window.title("DLUHAŘ")
        
            Tki.Button(window, text="Vytvořit záznam", command=Backend.fileWarn).place(x=20, y=10)
            Tki.Button(window, text="Změnit data záznamu", command=Backend.changeInfo).place(x=20, y=40)
            Tki.Button(window, text="Ostranit databázi", command=Gui.deleteInfoGui).place(x=20, y=70)
            Tki.Button(window, text="Zobrazit dlužníka", command=Gui.listGui).place(x=20, y=100)
            Tki.Button(window, text="Obnovit", command=lambda:[window.destroy(), Gui.main()]).place(x=210, y=115)
        
            text = Tki.Text(window, height=4, width=15)
            text.pack(side=Tki.RIGHT)
            text.insert(Tki.END, "Dluh: " + "\n" + "Splaceno: ")
            window.mainloop()
        
        except js.JSONDecodeError:
            
            window.destroy()
            
            window = Tki.Tk()
            window.geometry("300x150")
            window.title("DLUHAŘ")
        
            Tki.Button(window, text="Vytvořit záznam", command=Backend.fileWarn).place(x=20, y=10)
            Tki.Button(window, text="Změnit data záznamu", command=Backend.changeInfo).place(x=20, y=40)
            Tki.Button(window, text="Ostranit databázi", command=Gui.deleteInfoGui).place(x=20, y=70)
            Tki.Button(window, text="Zobrazit dlužníka", command=Gui.listGui).place(x=20, y=100)
            Tki.Button(window, text="Obnovit", command=lambda:[window.destroy(), Gui.main()]).place(x=210, y=115)
        
            text = Tki.Text(window, height=4, width=15)
            text.pack(side=Tki.RIGHT)
            text.insert(Tki.END, "Dluh: " + "\n" + "Splaceno: ")
            window.mainloop()

Gui.main()    
