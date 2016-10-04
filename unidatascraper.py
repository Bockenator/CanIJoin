#Imports
import urllib2
from bs4 import BeautifulSoup

#Body
#Open file which we write to and intialise column headings
fo = open("/home/tombock/Desktop/CanIJoin/unidata.txt", "rw+")
string = ["Name","Entry","Statisfaction","RA Q","RA I","GradPros","Student/Staff","Acc Spend","Fac Spend","Good Hon","DegComp","Total"]
line = fo.write(('\t'.join(string)))
line = fo.write('\n')

#Set up scraper using bs4 (we scrape from the table in the link below)
url = "http://www.thecompleteuniversityguide.co.uk/league-tables/rankings?o=Entry+Standards&v=wide"  # change to whatever your url is
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

#Setup arrays for names and entry standards (these are what we use in entryprediction.py)
uni_names = []
uni_entry = []

#NOTE: the reason we write this data to file is for future use of features not yet implemented (not relevant for the entry prediciton)
#For every row get the relevant data (ie we ignore the first 3 columns as they do not contain information we need)
for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    #Needed to ensure system does not crash when the mid league table is reached (as this row has no values so produces IndexOutOfBounds)
    if (tr.get('id') == 'midLeagueTable'):
    	print ''
    #Once we reach the end of the table data we need stop the for loop (as again we crash otherwise)
    elif (((tds[3].text).strip())=="Bedfordshire"):
    	break
    #We take all of the column  data after the 3rd column and strip it of any whitespace before writing it to file (and add the values to the relevant arrays)
    else:
    	string = [(tds[3].text).strip(), (tds[4].text).strip(), (tds[5].text).strip(), (tds[6].text).strip(), (tds[7].text).strip(), (tds[8].text).strip(), (tds[9].text).strip(), (tds[10].text).strip(), (tds[11].text).strip(), (tds[12].text).strip(), (tds[13].text).strip(), (tds[14].text).strip()]
    	line = fo.write(('\t'.join(string)))
    	line = fo.write('\n')
    	uni_names.append((tds[3].text).strip())
    	uni_entry.append((tds[4].text).strip())
