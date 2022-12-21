def display():
    with open('Storage.txt', 'r') as file:
        data = file.read()
        data = data.replace('_', ' ')
        print(data.rstrip())


def add(course_code, course_title, course_credit, course_prq):
    with open('Storage.txt', 'a') as file:
        file.write(f'{course_code}     {course_title}')
        file.write(' '*(77-len(course_title)))
        file.write(course_credit)
        file.write(' '*(11-len(course_credit)))
        file.write(f'{course_prq}\n')


def update(course_code, old_data, tew_data, new_data):
    with open('Storage.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            line = line.split()
            if course_code == line[0]:
                if old_data == 'ct':
                    if tew_data != 0:
                        line[1] = tew_data
                elif old_data == 'cc':
                    line[2] = new_data
                elif old_data == 'cp':
                    line[3] = new_data
            file.write(f'{line[0]}     {line[1]}')
            file.write(' '*(77-len(line[1])))
            file.write(line[2])
            file.write(' '*(11-len(line[2])))
            file.write(f'{line[3]}\n')


def delete(course):
    with open('Storage.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            line = line.split()
            if course == line[0] or course == line[3]:
                del line
            else:
                file.write(f'{line[0]}     {line[1]}')
                file.write(' '*(77-len(line[1])))
                file.write(line[2])
                file.write(' '*(11-len(line[2])))
                file.write(f'{line[3]}\n')


def details(course):
    with open('Storage.txt', 'r') as file:
        lines = file.readlines()
        n = 1
        for line in lines:
            line = line.split()
            if course == line[0] or course == line[1] or n == 1:
                print(f'{line[0]}     {line[1]}', end='')
                print(' ' * (77 - len(line[1])), end='')
                print(line[2], end='')
                print(' ' * (11 - len(line[2])), end='')
                print(f'{line[3]}',)
                n = 2
            else:
                pass


def search(course):
    with open('Storage.txt', 'r') as file:
        lines = file.readlines()

    n = 1
    for line in lines:
        line = line.replace('_', ' ')
        if n == 1 and course in line:
            print(line.rstrip())
            n = 2
        elif course in line:
            print(line.rstrip())

