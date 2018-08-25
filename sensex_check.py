import urllib2
import bs4
from bs4 import BeautifulSoup
import datetime
import sys
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

urlis="http://www.moneycontrol.com/sensex/bse/sensex-live"
page=urllib2.urlopen(urlis)
det_page=BeautifulSoup(page,'html.parser')


now=datetime.datetime.now()
name=det_page.find('div',class_="FL r_35")
name2=det_page.find('div',class_="FL r_20 PT10 MT3")
nameperc=det_page.find('div',class_="FL r_15 PT10 MT3 PL5")
#date=det_page.find('div',class_="gL_10_5 PT3")
tab=det_page.find('div',class_='FL PR10').find('table',class_='tbldtldata b_15')

print "Todys Date :"+str(now)
print "sensex  : ",str(name.text)
print "sensex change : "+str(name2.text)
print "Percentage change :"+str(nameperc.text)+" %"

a=[]
b=[]
c=[]
for data in tab.find_all("tr"):
	col=data.find_all("td")
	a.append(col[0].text)
	b.append(col[1].text)
	c.append(col[2].text)

for i in range(len(b)):
	if i==0:
		print    "                      "+b[i]+"       "+c[i]
	else:	
		print a[i],"       "+b[i]+"      "+c[i]