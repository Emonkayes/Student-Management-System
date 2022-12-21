import Function2 as Fc
wv = True
st = '''1. List of Course
2. Add new course
3. Update course
4. Delete course
5. Course details
6. Search course'''
print(st)
x = input("Choose your function at number: ")
while wv:
    if x == '1':
        Fc.display()
    elif x == '2' or x == 'add':
        Course_Code = input("Enter course code(*It is unchangeable and unique): ")
        Course_Title = input("Enter course title(*unique): ")
        Course_Title = Course_Title.upper()
        Course_Title = Course_Title.replace(' ', '_')
        Course_Credit = input("Enter course credit: ")
        Course_Prq = input("Enter course prerequisites (course code or -): ")
        with open('Storage.txt', 'r') as file:
            data = file.read()
            if Course_Code in data or Course_Title in data:
                print('The course is already added.')
            elif Course_Prq in data or Course_Prq == '-':
                Fc.add(Course_Code, Course_Title, Course_Credit, Course_Prq)
                print('Course added successfully.')
            else:
                print('The prerequisites is not listed in the course list. Please add the prerequisites course first.')
                x = input("To add the course enter 'add' or quit: ")
                if x == 'add':
                    continue
                elif x == 'quit':
                    break
    elif x == '3':
        Fc.display()
        Course_Code = input("Enter the course id you want to change: ")
        old_data = input("Enter which value you want to change,\n"
                         "Course title = ct\n"
                         "Course Credit = cc\n"
                         "Prerequisites = cp : ")
        tew_data = '$'
        new_data = 0
        if old_data == 'ct':
            tew_data = input("Enter your new course title: ")
            tew_data = tew_data.upper()
            tew_data = tew_data.replace(' ', '_')
        elif old_data == 'cc':
            new_data = input("Enter your new course credit: ")
        elif old_data == 'cp':
            new_data = input("Enter your new course prerequisites: ")
        else:
            print("You enter an invalid value.")
        with open('Storage.txt', 'r') as file:
            data = file.read()
            if tew_data in data:
                print('course is already added')
            elif new_data == 0 or new_data in data:
                Fc.update(Course_Code, old_data, tew_data, new_data)
                print('Updated successfully.')
            else:
                print('The prerequisites is not listed in the course list. Please add the prerequisites course first.')
                x = input("To add the course enter 'add' or quit: ")
                if x == 'add':
                    continue
                elif x == 'quit':
                    break
    elif x == '4':
        Fc.display()
        course = input("Enter the course code you want to delete: ")
        Fc.delete(course)
    elif x == '5':
        course = input('Enter course code or title:')
        course = course.upper()
        course = course.replace(' ', '_')
        Fc.details(course)
    elif x == '6':
        course = input('Enter what you want to search: ')
        course = course.upper()
        Fc.search(course)
    elif x == 'quit':
        break
    else:
        print('Invalid function')
    x = input("Enter quit to finish the program or continue entering function number: ")
