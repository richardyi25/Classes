#requests data from Google Sheet and asks for approval to add into database (data.txt)
import requests

class Person(object):
    def __init__(self, ID, firstName, lastName, courses):
        self.id = ID
        self.firstName = firstName
        self.lastName = lastName
        self.courses = courses

    def __str__(self):
        return self.firstName + ' ' + self.lastName

def load(fileName): #load people from a file
    with open(fileName, 'r') as f:
        s = f.read().strip('\n').split('\n')
        data = [eval(line) for line in s if line != '']

    return data

def save(fileName, data): #save people to a file
    with open(fileName, 'a') as f:
        f.write(str(person) + '\n')

def checkForNew(person): #check if someone has an "Other" course
    for i in xrange(1, 9):
        with open('courses/%i.txt' % i, 'r') as f:
            courses = f.read().strip('\n ').split('\n')
            if person[i] not in courses:
                print person[9], person[10], 'has a new course:', person[i], 'during Semester %i Period %i!' % ((i - 1)/4 + 1, (i - 1) % 4 + 1)

with open('../../API_KEYS/google.txt') as f:
    API_KEY = f.read() #API key is stored outside of repo (for security)

#request data from Google Sheet
r = requests.get('https://sheets.googleapis.com/v4/spreadsheets/1_CaYDWmPBOMHbCrnJJN4hno9y4B6s4uaJ9LoDrX5c9o/values/Sheet1!A2:L99999', {'key': API_KEY})

#0 = Timestamp      1-8 = Courses     9 = First Name   10 = Last Name     #11 = Feedback

data = r.json()['values']
data = [person for person in data if person != []]
old = load('data.txt')
rejected = load('rejected.txt')
new = []

for person in data: #check if each person is already in data.txt
    if person not in old:
        new.append(person)

for person in new: #if anyone new, ask for approval, and either save to data.txt or rejected.txt
    if person not in rejected:
        print person[9], person[10]
        print '\nCourses:'
        print '\n'.join(person[1:9])
        if person[11] != 'No':
            print 'Feedback:   ', person[11]
        while True:
            s = raw_input('\nApprove? (y/n)   ')
            if s.lower() == 'y':
                save('data.txt', person)
                checkForNew(person)
                break
            elif s.lower() == 'n':
                save('rejected.txt', person)
                break

print 'All people have been approved/rejected.'
