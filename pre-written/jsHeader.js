function Person(firstName, lastName, courses){ //init class and class constructor
	this.firstName = firstName;
	this.lastName = lastName;
	this.courses = courses;
	
	this.name = firstName + ' ' + lastName;	
}

/*Object init template:
	'First Last': new Person('First', 'Last', ['course1' ... 'course8']),
*/
var people = { //make dictionary/hash table of people
