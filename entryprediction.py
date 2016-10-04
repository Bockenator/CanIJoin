from gradeprediction import *
from unidatascraper import *
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

final_score = 0
c = 0
for y in y_array:
	if (c > (1-len(lvl_array))):
		c=0
	final_score += convert_to_score(y, lvl_array[c])
	c+=1

print ("Based on these grades and arbitrary other data it might be possible for you to be accepted by the following unis:\n")

c = 0
for name in uni_names:
	if (final_score >= (int(float(uni_entry[c])))):
		print(name+"\n")
	c+=1




