from people import Faculty, Student

students = []
faculty = []

while True:
    inp1 = input('''
      *** TUFFY TITAN CONTACT MAIN MENU

     1. Add faculty
     2. Print faculty
     3. Add student
     4. Print student
     9. Exit the program

Enter menu choice: ''')
    
    if (inp1 == '1'):
        first = input("Enter first name: ")
        last = input('Enter last name: ')
        dep = input('Enter department: ')
        fac = Faculty(firstname=first, lastname=last, department=dep)
        faculty.append(fac)

    if (inp1 == '2'):
        print('''
======================= FACLUTY =======================
Record  Name                  Department
======  ====================  =========================''')
        advisor_count = 0        
        for x, fac in enumerate(faculty):
            print(f"{advisor_count:<7} {fac.firstname:<1} {fac.lastname:<14} {fac.department}")
            advisor_count += 1
        

    if (inp1 == '3'):
        first = input("Enter first name: ")
        last = input('Enter last name: ')
        clas = input('Enter class year: ')
        major = input('Enter major: ')  
        advis = input('Enter faculty advisor: ')
        student = Student(firstname= first, lastname= last)       
        student.set_class(classyear=clas)
        student.set_major(major=major)
        student.set_advisor(advisor=advis)
        students.append(student)

    if (inp1 == '4'):
        print('''
===================================== STUDENTS ======================================
Name                  Class      Major                      Advisor
====================  =========  =========================  =========================''')
        for x, student in enumerate(students):
            print(f"{student.firstname:<1} {student.lastname:<15} {student.classyear:<10} {student.major:<26} {str(faculty[int(student.advisor)])}")

    if (inp1 == '9'):
        break