}

var sortedPeople = [] //array of people sorted by first then last name
for (var person in people) sortedPeople.push(people[person]);

sortedPeople.sort(function(obj1, obj2){ //custom sort function
	if (obj1.name < obj2.name) return -1;
	else if (obj1.name > obj2.name)  return 1;
	else return 0;
});

var allCourses = {}; //set containing all courses
for (var person in people) for (var j = 0; j < 8; j++) allCourses[people[person].courses[j].split(' ')[0]] = true;