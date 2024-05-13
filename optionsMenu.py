import readRecords,addRecord,deleteRecord,report,updateRecord
print("\n Please choose a number from the Options menu below:")
 
#define the menu object
 
def menu():
        print("1. Add a record")
        print("2. Delete a record")
        print("3. Amends a record")
        print("4. Print all records")
        print("5. Report")
        print("6. Exit")
 
def subMenu():
        print("\n 1. Print details of all films")
        print("2. Print all films of a particular genre")
        print("3. Print all films of a particular year")
        print("4. Print all films of a particular rating")
        print("5. Exit Report menu")
       
       
 
#variable to control the while loop
 
bVal = True
 
#create while loop
 
while bVal:
        menu()
        itmChoosen = input("Choose a number")
        if itmChoosen == "1":
                addRecord.addFilmFilm()  # go to addrecord.py
        elif itmChoosen == "2":
                deleteRecord.deleteRecord() # got to deleterecord.py
        elif itmChoosen == "3":
                updateRecord.updateFilm() # go to amendrecord.py
        elif itmChoosen == "4":
                readRecords.readRecords() # go to Print all records
        elif itmChoosen == "5":
               
                reportValue = True
                while reportValue:
                        subMenu()
                        reportChosen = input("Please choose a number from the report menu: ") # go to Report menu
                        if reportChosen == "1":
                                readRecords.readRecords()  # go to addrecord.py
                        elif reportChosen == "2":
                                report.genre() # got to deleterecord.py
                        elif reportChosen == "3":
                                report.year() # go to amendrecord.py
                        elif reportChosen == "4":
                                report.rating() # go to Print all records
 
                        else:
                               reportValue = False
                               print("Please press Enter to return to the main menu")        
 
 
 
 
        else:
 
                bVal = False
                print("Exiting the Options menu")
 