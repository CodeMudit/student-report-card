
import os
import json

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
        file_name = "Grades.json"
        self.grades = []
        self.loadgrades()



    def savegrades(self) :
        with open("Grades.json","w") as file :
            #fieldnames = ["Name","Class","Roll Number","Maths","English","Science","Total","Percentage","Grades"]
            # writer = csv.DictWriter(file,fieldnames = fieldnames , delimiter = "|")
            json.dump(self.grades,file,indent = 4)
            

    def loadgrades(self) :
        try :
            with open("Grades.json","r") as file :
                reader = json.load(file)
                self.grades = (reader)
        except FileNotFoundError :
            print("No grades of students exist please enter some first")
            self.record()

        except json.JSONDecodeError :
            print("Grades file is corrupt empty")
            self.grades = []
            self.record()

          


    def record(self) :
        #while True :
            student = input("Enter the name of the student : ")
            Class = input("Enter the student's class : ")
            while True :
                try :
                    roll_no = int(input("Enter the student's roll number : "))
                    if any(user["Roll Number"] == roll_no for user in self.grades) :
                        print("This roll number has already been registered please enter a valid roll number")
                        continue
                    else :
                        break
                        
                    
                except ValueError :
                    print("Please enter a valid roll number")
                break

                    
            grades = "o"
            while True :
                Maths = self.valid_marks("Maths")
                
                English = self.valid_marks("English")
                
                Science = self.valid_marks("Science")
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
                for st in self.grades :
                    if str(st["Roll Number"]) == str(new_roll) :
                        print("Student report found!!")
                        self.newgrades()
                        self.savegrades()
                        found = True
                        break
                if not found :
                    print("Please enter a valid Roll Number ")
                    continue
                else :
                    break
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
                                updated = (input("Enter the new grades for Maths : "))
                                grade["Maths"] = updated
                                found1 = True
                                self.ask()
                                break
                            elif new_grade == "English" :
                                updated1 = (input("Enter the new grades for English : "))
                                grade["English"] = updated1
                                found1 = True
                                self.ask()
                                break

                            elif new_grade == "Science" :
                                updated2 = (input("Enter the new grade for Science : "))
                                grade["Science"] = updated2
                                found1 = True
                                self.ask()
                                break
                        if not found1 :
                            print("Please Enter a valid subject")
                            continue
                        break
                    for grade in self.grades :
                        grade["Total"] = round(float(grade["English"]) + float(grade["Maths"]) + float(grade["Science"]))
                        grade["Percentage"] = (grade["Total"]/3) 
                        if grade["Percentage"] >= 90 :
                            grade["Grades"] = "A"
                        elif grade["Percentage"] >=  80 :
                            grade["Grades"] = "B"
                        elif 33 <= grade["Percentage"] < 80 :
                            grade["Grades"] = "C"
                        else :
                            grade["Grades"] = "Fail"

                    

                    

    

                    
                
    def ask(self) :
        while True :
            ask = input("Do you want to update other grades ? (y/n)").strip().lower()
            if ask == "y" :
                self.newgrades()
                break
            elif ask == "n" :
                print("Thanks for using this programme")
                
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

    def valid_marks(self,subject) :
        while True :
            try :
                marks = float(input(f"Please enter the marks of {subject} (0-100) : "))
                if 0 <= marks <= 100 :
                    return marks
                
                else : 
                    print("Marks must be between 0 and 100")
                    

            except ValueError :
                print("Please enter a valid value")

    def grade_distribution(self) :
        distribution = {"A" : 0,"B" : 0,"C" : 0}
        for student in self.grades :
            grade = student["Grades"]
        if grade in distribution :
            distribution[grade] += 1
        for grade , count in distribution.items() :
            print(f"{grade} : {count} student(s)")


student = ReportCard()

def execute() :
    print("Welcome to This Programme")
    opt = int(input("""Please select from the following operations :
                        1.Add a Student
                        2.View All Students
                        3.Search Student by Roll Number
                        4.Update the grades of a student
                        5.Grade Distribution
                        6.Exit
                            """))
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
        student.grade_distribution()
        repeat()

    elif opt == 6:
        exit()

    else :
        print("Please select a valid number")
        execute()

execute()
