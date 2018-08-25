from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
import urllib
from bs4 import BeautifulSoup
import datetime
#import warning

#warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
urlis="http://www.moneycontrol.com/sensex/bse/sensex-live"
page=urllib.request.urlopen(urlis)
det_page=BeautifulSoup(page,'html.parser')

def Sensex_today():
	now=datetime.datetime.now()
	name=det_page.find('div',class_="FL r_35")
	name2=det_page.find('div',class_="FL r_20 PT10 MT3")
	nameperc=det_page.find('div',class_="FL r_15 PT10 MT3 PL5")
	tab=det_page.find('div',class_='FL PR10').find('table',class_='tbldtldata b_15')

	s=" Todys Date :"+str(now)+'\n'
	s+="sensex  : "+str(name.text)+'\n'
	s+="sensex change : "+str(name2.text)+"\n"
	s+="Percentage change :"+str(nameperc.text)+" \n"

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
			s+=    "                  "+b[i]+"     "+c[i]+'\n'
		else:	
			s+= a[i]+"    "+b[i]+"      "+c[i]+"\n"


	return s





root = Tk()
root.title('Bombay Stock Exchange')
label = Label(root)
label.pack()

#name = simpledialog.askstring('Movie/Tv-Series' ,"Input the movie/tvseries name?")

s = Sensex_today()
tkinter.messagebox.showinfo("Result :" ,s )