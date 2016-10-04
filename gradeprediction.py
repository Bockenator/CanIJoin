#Imports
import numpy as np
import random as random
from sklearn.naive_bayes import GaussianNB

#Methods
#Needed for working out the mean grade (as letters don't add/divide particularly well)
#so the better the grade the higher the number. Also used in the entry prediction to
#help evaluate the final score
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

#Used for conversion of mean grade from number back into a grade
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

#Ensures we only add valid grades to our grade array
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

#Ensures we only add valid grade levels to our list of the corresponding levels to the grades
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


#Body
#Initialise arrays and variables
x_array = []
y_array = []
lvl_array = []
x_coor = 0
y_coor = 0
#We intially set these to blank so we go through the "while" below at least once
grade = ''
level = ''

#As long as we are not given the terminating letter we ask for grades
while (grade != 'Q'):
	grade = raw_input('Please enter your achieved grades (or Q to finish): ')
	#Only add valid grades otherwise ask again in next pass of while loop (after warning given)
	if verify_valid_grade(grade):
		y_array.append(grade)
		#If we're given the terminating character we don't unneccesarily ask for the level
		if (grade != 'Q'):
			level = raw_input('At what level did you get this grade (AdvHigher, Higher, A, AS): ')
			#As above we only add valid levels otherwise we ask again
			if (verify_valid_level(level)):
				lvl_array.append(level)
			else:
				while (not verify_valid_level(level)):
					level = raw_input('WARNING: Please enter a valid level (AdvHigher, Higher, A, AS): ')
				lvl_array.append(level)
	else:
		if (grade != 'Q'):
			print 'WARNING: Please enter a valid grade'

#We sort the array of grades to make the grade clusters for gaussian classification nicer
y_sorted = sorted(y_array)
y_array = y_sorted

#We set up the x_array in such a way that we get a nice line ([1,1],[2,2],[3,3],etc.)
for grade in y_array:
	x_array.append([x_coor,y_coor])
	x_coor += 1
	y_coor += 1

#Actual gaussian classifcation using the given grades as training data
x = np.array(x_array)
y = np.array(y_array)
clf = GaussianNB()
clf.fit(x, y)

#We ask how many grades the user wants predicted
no_of_grades = input('Please enter the number of grades you want predicted: ')
grades_needed = []

#To predict the grades we randomly generate a point somewhere in the region spanned
#by our line of training grades. The idea is that the more of one grade you have the
#more likely the point is to land in that grade region
for i in range(0, no_of_grades):
	x_pl = random.randrange(0, len(x_array),1)
	y_pl = random.randrange(0, len(x_array),1)
	grades_needed.append([x_pl, y_pl])

#Predict the grades 
gradelist = clf.predict(grades_needed)

total = 0;
for grade in gradelist:
	total += grade_to_number(grade)
mean = (float(total)/float(len(gradelist)))
print('All grades : ')
print(gradelist)
print('Mean grade: ')
print(number_to_grade(mean))
