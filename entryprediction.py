#Imports
from gradeprediction import *
from unidatascraper import *

#Allows conversion of grades into a score to measure against the entry standards of a university
#NOTE: These scores are more or less arbitrary based on personal opinion and SHOULD NOT be used
#as an actual indication of the value of these grades
def convert_to_score(grade, level):
	if (level.lower() == "higher"):
		return (15*grade_to_number(grade))
	elif (level.lower() == "a"):
		return (17*grade_to_number(grade))
	elif (level.lower() == "advhigher"):
		return (23*grade_to_number(grade))
	elif (level.lower() == "as"):
		return (25*grade_to_number(grade))
	return 0

#Intialise a final score and counter (c)
final_score = 0
c = 0

#Add the scores of individual grades together
for y in y_array:
	if (c > (1-len(lvl_array))):
		c=0
	final_score += convert_to_score(y, lvl_array[c])
	c+=1

#I feel like this is self-explantory
print ("Based on these grades and arbitrary other data it might be possible for you to be accepted by the following unis:\n")

#Reset counter
c = 0

#Print the names of universities which grades allow (ie the unis with entry requirements matching or lower than our grades)
for name in uni_names:
	if (final_score >= (int(float(uni_entry[c])))):
		print(name+"\n")
	c+=1




