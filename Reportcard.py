import csv 
import os

def repeat() :
    while True :
        asked = input("Do you want to run this programme again ? (y/n)").strip().lower()
        if asked == "y" :
            execute()
            break
        elif asked == "n" :
            print("Thanks for using this programme")
        
        else :
            print("Please select a valid character")
            continue
        break




class ReportCard :
    def __init__(self) :
        file_name = "Grades.csv"
        self.grades = []
        self.loadgrades()



    def savegrades(self) :
        with open("Grades.csv","w",newline = "") as file :
            fieldnames = ["Name","Class","Roll Number","Maths","English","Science","Total","Percentage","Grades"]
            writer = csv.DictWriter(file,fieldnames = fieldnames , delimiter = "|")
            writer.writeheader()
            writer.writerows(self.grades)

    def loadgrades(self) :
        try :
            with open("Grades.csv","r") as file :
                reader = csv.DictReader(file,delimiter = "|")
                self.grades = list(reader)
        except FileNotFoundError :
            print("No grades of students exist please enter some first")
            self.record()

    def record(self) :
        #while True :
            student = input("Enter the name of the student : ")
            Class = input("Enter the student's class : ")
            roll_no = input("Enter the student's roll number : ")
            grades = "o"
            while True :
                Maths = float(input("Enter the student's Marks in Maths : "))
                if Maths > 100 :
                    print("Please enter valid Marks ")
                    continue
                English = float(input("Enter the student's marks in English : "))
                if English > 100 :
                    print("Please enter valid Marks ")
                    continue
                Science = float(input("Enter the student's marks in Science : "))
                if Science > 100 :
                    print("Please enter valid Marks ")
                    continue
                break
            sum = Maths + English + Science
            total = sum
            Percentage = (total/3) 
            if float(Percentage) >= 90 :
                grades = "A"
            elif float(Percentage) >= 80 :
                grades = "B"
            elif float(Percentage) > 33 :
                grades = "C"
            else :
                grades = "Fail"

            students_dict = {
                "Name" : student,
                "Class" : Class,
                "Roll Number" : roll_no,
                "Maths" : Maths,
                "English" : English,
                "Science" : Science,
                "Total" : total,
                "Percentage" : Percentage,
                "Grades" : grades

            }
            self.grades.append(students_dict)
            self.savegrades()
            print("The new student report card has now been saved to th student records ")

    def viewstudents(self) :
        for student in self.grades :
            print("\n----Student Reports----\n")
            print(student)

    def searchroll(self) :
        try :
        
            while True :
                found = False
                new_roll = input("Enter the student's Roll Number : ").strip()
                for student in self.grades :
                    if student["Roll Number"] == new_roll :
                        print("Roll Number found!! ")
                        print("--Student Report--")
                        print(f"Name : {student["Name"]}")
                        print(f"Class : {student["Class"]}")
                        print(f"Roll Number : {student["Roll Number"]}")
                        print(f"Maths : {student["Maths"]}")
                        print(f"English : {student["English"]}")
                        print(f"Science : {student["Science"]}")
                        print(f"Total : {student["Total"]}")
                        print(f"Percentage : {student["Percentage"]}")
                        print(f"Grades : {student["Grades"]}")
                        found = True
                        break
                if not found :
                    print("Please Enter a valid Roll Number")
                    continue
                break
        except FileNotFoundError :
            print("No students have been registered please register first")
            self.record()

    def update(self) :
        try :
            
            while True : 
                found = False
                new_roll = input("Enter the Student's roll number : ").strip()
                if any(st["Roll Number"] == new_roll for st in self.grades) :
                    print("Student report found!!")
                    self.newgrades()
                    found = True
                    break
                if not found :
                    print("Please enter a valid Roll Number ")
                    continue
                break
        except FileNotFoundError :
            print("No records found Please enter some grades first")
            self.record()
                    
    def newgrades(self) :
                    while True :
                        found1 = False 
                        new_grade = input("Enter the subject for which you want to upgrade the grades : ").strip()
                        for grade in self.grades :
                            if new_grade == "Maths" : 
                                updated = float(input("Enter the new grades for Maths : "))
                                grade["Maths"] = updated
                                found1 = True
                                self.ask()
                                break
                            elif new_grade == "English" :
                                updated1 = float(input("Enter the new grades for English : "))
                                grade["English"] = updated1
                                found1 = True
                                self.ask()
                                break

                            elif new_grade == "Science" :
                                updated2 = float(input("Enter the new grade for Science : "))
                                grade["Science"] = updated2
                                found1 = True
                                self.ask()
                                break
                        if not found1 :
                            print("Please Enter a valid subject")
                            continue
                        break
                    
                
    def ask(self) :
        while True :
            ask = input("Do you want to update other grades ? (y/n)").strip().lower()
            if ask == "y" :
                self.newgrades()
                break
            elif ask == "n" :
                print("Thanks for using this programme")
                repeat()
                break
            else :
                print("Please select a valid input")
                continue
    
    def deletestudent(self) :
        try :
            while True :
                found = False
                delgrades = input("Enter the Roll Number you want to delete : ").strip()
                for grade in self.grades :
                    if grade["Roll Number"] == delgrades :
                        self.grades.remove(grade)
                        found = True
                        break
                    
                if not found :
                    print("Please enter a valid Roll Number")
                    continue
                break
        except FileNotFoundError :
            print("No records exist Enter some details first")
            self.record()

student = ReportCard()

def execute() :
    print("Welcome to This Programme")
    opt = int(input("""Please select from the following operations :
                        1.Add a Student
                        2.View All Students
                        3.Search Student by Roll Number
                        4.Update the grades of a student
                        5.Exit"""))
    if opt == 1 :
        student.record()
        repeat()

    elif opt == 2 :
        student.viewstudents()
        repeat()

    elif opt == 3:
        student.searchroll()
        repeat()

    elif opt == 4:
        student.update()
        repeat()

    elif opt == 5:
        exit()

    else :
        print("Please select a valid number")
        execute()

execute()


                                





            
