#parses Python list data (data.txt) into JavaScript objects in the site folder

import ast #for safely eval-ing

#0 = Timestamp      1-8 = Courses     9 = First Name   10 = Last Name     #11 = Feedback

with open('table/htmlHeader.js', 'r') as hf, open('table/htmlFooter.js', 'r') as ff, open('data.txt', 'r') as rf, open('../richardyi25.github.io/classes/people.js', 'w') as wf:
    wf.write(hf.read())

    people = [[s.encode('utf-8') for s in ast.literal_eval(line)] for line in rf.read().strip('\n').split('\n')]
    #using eval to convert string to list

    for person in people:
        first = person[9]
        last = person[10]
        courses = str(person[1:9])

        wf.write('    ' + '\'' + first + ' ' + last + '\' : new Person(\'' + first + '\', \'' + last + '\', ' + courses + '),\n')
        #convert each person into JS Object

    wf.write(ff.read())

raw_input('Parsed into HTML table.\nPress any key to continue...')