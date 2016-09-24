}

var sortedPeople = [] //array of people sorted by first then last name
for (var person in people) sortedPeople.push(people[person]);

sortedPeople.sort(function(obj1, obj2){ //custom sort function
	if (obj1.name < obj2.name) return -1;
	else if (obj1.name > obj2.name)  return 1;
	else return 0;
});