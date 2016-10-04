from lxml import html
import requests
import urllib2
from bs4 import BeautifulSoup

fo = open("/home/tombock/Desktop/CanIJoin/unidata.txt", "rw+")
string = ["Name","Entry","Statisfaction","RA Q","RA I","GradPros","Student/Staff","Acc Spend","Fac Spend","Good Hon","DegComp","Total"]
line = fo.write(('\t'.join(string)))
line = fo.write('\n')
#get page data
page = requests.get("http://www.thecompleteuniversityguide.co.uk/league-tables/rankings?o=Entry+Standards&v=wide")
tree = html.fromstring(page.content)

uni_names = tree.xpath('//table[@class="leagueTable hoverHighlight wide"]/tbody/tr/td[@class="left"]/a/text()')
#uni_data = tree.xpath('//table[@class="leagueTable hoverHighlight wide"]/tbody/tr/td[@class="highlight"]/text()')
#print(uni_data)

url = "http://www.thecompleteuniversityguide.co.uk/league-tables/rankings?o=Entry+Standards&v=wide"  # change to whatever your url is

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)
uni_names = []
uni_entry = []
for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    if (tr.get('id') == 'midLeagueTable'):
    	print ''
    elif (((tds[3].text).strip())=="Bedfordshire"):
    	break
    else:
    #uni_data.append([(tds[3].text).strip(), (tds[4].text).strip(), (tds[5].text).strip(), (tds[6].text).strip(), (tds[7].text).strip(), (tds[8].text).strip(), (tds[9].text).strip(), (tds[10].text).strip(), (tds[11].text).strip(), (tds[12].text).strip(), (tds[13].text).strip(), (tds[14].text).strip()])
    	string = [(tds[3].text).strip(), (tds[4].text).strip(), (tds[5].text).strip(), (tds[6].text).strip(), (tds[7].text).strip(), (tds[8].text).strip(), (tds[9].text).strip(), (tds[10].text).strip(), (tds[11].text).strip(), (tds[12].text).strip(), (tds[13].text).strip(), (tds[14].text).strip()]
    	line = fo.write(('\t'.join(string)))
    	line = fo.write('\n')
    	uni_names.append((tds[3].text).strip())
    	uni_entry.append((tds[4].text).strip())
#print uni_data