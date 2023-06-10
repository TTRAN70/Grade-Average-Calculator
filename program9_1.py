#Tony Tran | COP1000

#Collaborator Statement: I worked alone

#Pseudocode

'''  
CREATE an empty dictionary
PROMPT user for course code
WHILE the user doesn't hit enter to quit
PROMPT the user for grade percentage
STORE the 2 variables into the dictionary

FOR loop in the dictionary
DISPLAY the course and the grades
ADD up all the grades
CHECK for smallest grade value

DISPLAY the average
DISPLAY the worst course from the smallest grade value
REMOVE the course with the smallest grade value

FOR loop in the updated dictionary
DISPLAY all the courses and grades
ADD up all the grade values

DISPLAY the revised average
'''

def main():

    #Creates an empty dictionary and stores courses + grades, course code is the key, grade is the value
    courses = dict()
    code = input('Input course code or Enter to quit ')
    while code != '':
        grade = int(input('Grade in ' + code + ' as % '))
        courses[code] = grade
        code = input('Input course code or Enter to quit ')

    #Loops through dictionary to display values, also adds up each grade value into average, and
    #finds the worst grade value by checking if a value is less than the number
    average = 0
    num = 100
    worst = ''
    for f in courses:
        print('Grade in ' + f + ' is ' + str(courses[f]) + '%')
        average += courses[f]
        if courses[f] < num:
            num = courses[f]
            worst = f

    #Displays the average and the worst course, also removes the worst course from the dictionary (pop)
    print(f'Current term average is {average/len(courses):.1f}%')
    print('Worst course is ' + worst + ' : ' + str(courses[worst]) + '%')
    courses.pop(worst)
    print('Dropped ' + worst)

    #Loops through the updated dictionary and adds each grade value into the average, displaying after
    average = 0
    print('Here are my revised grades...')
    for g, i in courses.items():
        print('Grade in ' + g + ' is ' + str(i) + '%')
        average += i
    print(f'Revised term average is {average/len(courses):.1f}%')

if __name__ == "__main__":
    main()

