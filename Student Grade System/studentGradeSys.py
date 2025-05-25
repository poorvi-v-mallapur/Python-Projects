
    
student_details = {}

def add_student():
    name = input('Enter the name of the student:')
    marks = input('Enter the marks of the student:')
    student_details[name] = marks
    print(f'Student {name} with {marks} is added')

def update_student():
    if student_details:
        name = input('Enter the name of the student:')
        if name in student_details:
            marks = input('Enter the updated marks: ')
            student_details[name] = marks
            print(f'{name}\'s marks is updated to {marks}')
        else:
            print(f'Student details for {name} doesnt exist')
    else:
        print('No student details exist')

def del_student():
    if student_details:
        name = input('Enter the name of the student you would like to delete:')
        if name in student_details:
            student_details.pop(name)
            print(f'Student details for {name} is deleted')
        else:
            print(f'Student details for {name} doesnt exist')
    else:
        print('No student details exist')

def display_all():
    if student_details:
        for name, marks in student_details.items():
            print(f'name:{name}, marks:{marks}')
    else:
        print('No student details exist')


def main():
    while True:
        print('''
        Welcome to Student Management Dashboard!
        1. Add a student
        2. Update a student
        3. Delete a student
        4. Display all students details
        5. Exit
        ''')
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print('Invalid input! Please enter a number.')
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            update_student()
        elif choice == 3:
            del_student()
        elif choice == 4:
            display_all()
        elif choice == 5:
            print('Exiting the Student Management Dashboard. Goodbye!')
            break
        else:
            print('Enter a valid choice.')

if __name__ == '__main__':
    main()