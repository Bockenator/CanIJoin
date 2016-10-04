import numpy as np
import random as random
from sklearn.naive_bayes import GaussianNB

#Methods
def grade_to_number(grade):
	if (grade == 'A'):
		return 4
	elif (grade == 'B'):
		return 3
	elif (grade == 'C'):
		return 2
	elif (grade == 'D'):
		return 1
	else:
		return 0

def number_to_grade(number):
	if (number > 3.5):
		return 'A'
	elif (number > 2.5):
		return 'B'
	elif (number > 1.5):
		return 'C'
	elif (number > 0.5):
		return 'D'
	else:
		return 'F'

def verify_valid_grade(grade):
	if (grade == 'A'):
		return True
	elif (grade == 'B'):
		return True
	elif (grade == 'C'):
		return True
	elif (grade == 'D'):
		return True
	elif (grade == 'F'):
		return True
	else:
		return False

def verify_valid_level(level):
	if (level.lower() == 'advhigher'):
		return True
	elif ( level.lower() == 'higher'):
		return True
	elif (level.lower() == 'a'):
		return True
	elif (level.lower() == 'as'):
		return True
	else:
		return False

#train using high school higher and above data
x_array = []
y_array = []
lvl_array = []
x_coor = 0
y_coor = 0

grade = ''
level = ''


while (grade != 'Q'):
	grade = raw_input('Please enter your achieved grades (or Q to finish): ')
	if verify_valid_grade(grade):
		y_array.append(grade)
		if (grade != 'Q'):
			level = raw_input('At what level did you get this grade (AdvHigher, Higher, A, AS): ')
			if (verify_valid_level(level)):
				lvl_array.append(level)
			else:
				while (not verify_valid_level(level)):
					level = raw_input('At what level did you get this grade (AdvHigher, Higher, A, AS): ')
				lvl_array.append(level)
	else:
		if (grade != 'Q'):
			print 'Please enter a valid grade'

y_sorted = sorted(y_array)
y_array = y_sorted
for grade in y_array:
	x_array.append([x_coor,y_coor])
	x_coor += 1
	y_coor += 1

x = np.array(x_array)
y = np.array(y_array)
clf = GaussianNB()
clf.fit(x, y)

no_of_grades = input('Please enter the number of grades you want predicted: ')
#number of grades needed
grades_needed = []
for i in range(0, no_of_grades):
	x_pl = random.randrange(0, len(x_array),1)
	y_pl = random.randrange(0, len(x_array),1)
	grades_needed.append([x_pl, y_pl])

gradelist = clf.predict(grades_needed)

total = 0;
for grade in gradelist:
	total += grade_to_number(grade)
mean = (float(total)/float(len(gradelist)))
print('All grades : ')
print(gradelist)
print('Mean grade: ')
print(number_to_grade(mean))
