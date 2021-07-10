from tkinter import *
from tkfilebrowser import askopenfilenames
from tkinter import messagebox
import sqlite3 as sql
import sys
from prettytable import PrettyTable
from subcodes import subcodes
from matplotlib import pyplot
# from cnst import *

# from customwarnings import successful

win = Tk()
win.configure(background = '#191919')
w = win.winfo_screenwidth()
h=win.winfo_screenheight()
win.geometry("{0}x{1}+0+0".format(w,h))
win.overrideredirect(True)
def xxx(event):
	win.overrideredirect(True)
	win.geometry("{0}x{1}+0+0".format(w,h))
	win.overrideredirect(True)

from images import *

tot_mark = 500
sub_total = 100

roll = IntVar()
sex = IntVar()
name = IntVar()
m1 = IntVar()
sc1 = IntVar()
g1 = IntVar()
sc2 = IntVar()
m2 = IntVar()
g2 = IntVar()
sc3 = IntVar()
m3 = IntVar()
g3 = IntVar()
sc4 = IntVar()
m4 = IntVar()
g4 = IntVar()
sc5 = IntVar()
m5 = IntVar()
g5 = IntVar()
gad1 = IntVar()
gad2 = IntVar()
gad3 = IntVar()
res = IntVar()
tot = IntVar()
roll.set(0) 
sex.set(0) 
name.set(0) 
m1.set(0) 
sc1.set(0) 
g1.set(0) 
sc2.set(0) 
m2.set(0) 
g2.set(0) 
sc3.set(0) 
m3.set(0) 
g3.set(0) 
sc4.set(0) 
m4.set(0) 
g4.set(0) 
sc5.set(0) 
m5.set(0) 
g5.set(0) 
gad1.set(0) 
gad2.set(0) 
gad3.set(0) 
res.set(0) 
tot.set(0) 

fieldnames = ['roll','sex','name', 'm1','sc1','g1' ,'sc2' ,'m2','g2','sc3','m3','g3','sc4','m4','g4','sc5','m5','g5','gad1','gad2','gad3','res','tot']


#BUTTON IMAGE DEFINITION,highlightthickness=0S

def successful(msg):
	global Warning,okbutton,warnlabel
	warning = Tk()
	warning.configure(background = '#161616')
	warning.geometry('+650+330')
	warning.overrideredirect('True')
	warning.attributes("-topmost", True)

	warnlabel = Label(warning,text = f'\n{msg}\n', fg = '#40a3ff',font = ('Arial','15'),bg = '#161616',anchor = CENTER,padx = 50,pady = 20)
	warnlabel.pack(fill = BOTH)

	okbutton = Button(warning, text = 'OK!',fg = 'gray',bg = '#161616',bd = 0,padx = 50,pady = 20,command = lambda:warning.destroy(),activebackground = '#40a3ff',highlightthickness=0)
	okbutton.pack(fill = BOTH)
	# warning.mainloop()

active = 'menuframe'

def enteranalyze(event):
	analyzebutton.configure(image = anazyle_img_on)
def leaveanalyze(event):
	analyzebutton.configure(image = anazyle_img_of)

def entergraph(event):
	graph.configure(image = graph_img_on, bg = '#191919')
def leavegraph(event):
	graph.configure(image = graph_img_of, bg = '#40a3ff')

def entersearch(event):
	search.configure(image = search_img_on, bg = '#191919')
def leavesearch(event):
	search.configure(image = search_img_of, bg = '#40a3ff')

def enterdoc(event):
	doc.configure(image = doc_img_on, bg = '#191919')
def leavedoc(event):
	doc.configure(image = doc_img_of, bg = '#40a3ff')

def entermenu(event):
	menu.configure(image = menu_img_on, bg = '#191919')
def leavemenu(event):
	menu.configure(image = menu_img_of, bg = '#40a3ff')

def enteropen(event):
	openbutton.configure(image = openon)
def leaveopen(event):
	openbutton.configure(image = openof)

def enterexit(event):
	exitbutton.configure(image = closeon)
def leaveexit(event):
	exitbutton.configure(image = closeof)

def searchdetails():
	global c
	global x
	global namesearchbar
	srname = namesearchbar.get()
	global res
	global fieldnames
	global fieldvars
	fieldvars = [roll.get(),sex.get(),name.get(), m1.get(),sc1.get(),g1.get(),sc2.get(),m2.get(),g2.get(),sc3.get(),m3.get(),g3.get(),sc4.get(),m4.get(),g4.get(),sc5.get(),m5.get(),g5.get(),gad1.get(),gad2.get(),gad3.get(),res.get(),tot.get()]
	print(fieldvars)
	selectfields = [fieldnames[i] for i in range(len(fieldvars)) if fieldvars[i] == 1]
	selectfields = tuple(selectfields)
	if len(selectfields) == 0:
		fields = tuple(fieldnames)
		selectfields = fields
	elif len(selectfields) == 1:
		fields = selectfields[0]
	else:		
		fields = selectfields
	exstring = f'select {fields} from data where name like "%{srname}%"'.replace('(', '')
	exstring =  exstring.replace(')', '')
	exstring =  exstring.replace('\'', '')
	
	print(exstring)
	c.execute(exstring)
	
	resultstring = ''''''
	table = PrettyTable()
	table.field_names = selectfields
	for i in c:
		table.add_row(i)
		for j in i:
			resultstring+=str(j)+' '
		resultstring+='\n'
	resultwindow = Tk()
	resultwindow.configure(background = '#141414')
	# resultlabel = Label(resultwindow,text = str(table),font = 'Consolas',bg = '#141414',fg = 'white')
	# resultlabel.pack()
	resultlabel = Text(resultwindow, borderwidth=0,bg = '#141414',fg = 'white',width = len(str(table).split('\n')[0]),font = 'Consolas 13',height = len(str(table).split('\n')))
	resultlabel.insert(1.0, str(table))
	resultlabel.configure(state = 'disabled')
	resultlabel.pack()
	print(str(table).split('\n')[0])


def pressdocbutton():
	global active
	exec(active + '.destroy()')
	active = 'docframe'


	global docframe
	docframe = Frame(win)
	docframe.configure(background = '#191919')
	docframe.grid(row = 1,rowspan = 8,column = 2,columnspan = 6)

def pressgraphbutton():
	global active
	exec(active + '.destroy()')
	active = 'graphframe'

	global graphframe
	graphframe = Frame(win,padx = 0,pady = 0)
	graphframe.configure(background = '#191919')
	graphframe.grid(row = 1,rowspan = 8,column = 2,columnspan = 6,ipadx = 650,ipady = 190)

	global searchbar

	searchbar = Entry(graphframe,bd = 0,bg = '#141414',fg = 'white',justify = CENTER,highlightthickness=0,)
	searchbar.pack(expand = True,fill = BOTH)

	drawgraph = Button(graphframe,text = 'Make Graph',command = makegraph)
	drawgraph.pack(expand = True,fill = BOTH)

def makegraph():
	global searchbar
	global subcodes
	global c
	nameorcode = searchbar.get()
	c.execute(f'select name from data where name like "%{nameorcode}%"')
	tempx = c.fetchall()
	x = []
	print(tempx)
	for i in tempx:
		x.append(i[0])
	print(x)
	print(nameorcode)
	for i in x:
		c.execute(f'select m1,sc1,m2,sc2,m3,sc3,m4,sc4,m5,sc5 from data where name like "%{i}%"')
		marks = c.fetchall()
		print(marks)
		scode = [str(i) for i in marks[0][1::2]]
		marks = [int(i) for i in marks[0][0::2]] 
		scode = [subcodes[i] for i in scode]
		print(marks)
		pyplot.bar(scode,marks)
		pyplot.title(i)
		pyplot.yticks([10,20,30,40,50,60,70,80,90,100])
		pyplot.show()
	



def presssearchbutton():
	global active
	exec(active + '.destroy()')
	active = 'searchframe'
	global namesearchbar
	global searchframe
	searchframe = Frame(win,padx = 0,pady = 0)
	searchframe.grid(row = 0,rowspan = 8,column = 2,columnspan = 6,ipadx = 575,ipady = 190)
	searchframe.configure(background = '#FFFFFF')
	
	try:
		codeviewer = Text(searchframe, borderwidth=0,bg = '#141414',fg = 'white',font = 'Consolas 13',width = 25)
		global schoolsubs
		global subcodes
		availcodes = ''''''
		print(schoolsubs)
		for i in schoolsubs:
			availcodes += i + ':' + subcodes[i] + '\n'

		availcodes += 'M   : MARK\nSSC  : SUBJECT CODES\nG   : GRADES\nGAD : ADDITIONAL GRADES\nRES : RESULT\nTOT : TOTAL'

		print('avail codes : ',availcodes)

		codeviewer.insert(END,availcodes)
		codeviewer.pack(side = LEFT,expand = False,fill = Y)
	except:
		pass
	# searchframe.pack()
	for i in fieldnames:
		print(i + f'_button = Checkbutton(searchframe,text = "{i.upper()}",bg = "#141414",fg = "gray",bd = 0,relief = FLAT,var = {i},padx = ])')
		exec(i + f'_button = Checkbutton(searchframe,text = "{i.upper()}",bg = "#141414",fg = "gray",bd = 0,relief = FLAT,var = {i},highlightthickness=0,anchor = "w")')
	for i in range(1,24):
		# exec(fieldnames[i-1]+f"_button.grid(row = 1, column = {i},ipadx = 9,ipady = 15)")
		exec(fieldnames[i-1]+f"_button.pack(fill = BOTH,expand = True,)")
	blanklabel = Label(searchframe,bd = 0,relief = FLAT,bg = '#191919',text = 'Use the below box to search students using name!',fg = '#40a3ff')
	# blanklabel.grid(row = 2,column = 1,columnspan = 23,ipady = 10,)
	blanklabel.pack(fill = BOTH,expand = True)
	namesearchbar = Entry(searchframe,bd = 0,bg = '#141414',fg = 'white',justify = CENTER,highlightthickness=0,)
	# namesearchbar.grid(row = 3,column = 1,columnspan = 21,ipady = 10,ipadx = 605)
	namesearchbar.pack(fill = BOTH,expand = True)
	searchbutton = Button(searchframe,fg = '#161616',bg = '#40a3ff',text = 'Search!',bd = 0,command = searchdetails,highlightthickness=0)
	# searchbutton.grid(row = 3,column = 22,columnspan = 2,ipady = 9,ipadx = 40)
	searchbutton.pack(fill = BOTH,expand = True)

	

def pressmenubutton():
	global active
	try:
		exec(active + '.destroy()')
	except:
		pass
	active = 'menuframe'


	global menuframe
	global openbutton
	global exitbutton
	global emptylabel5
	global emptylabel6
	global analyzebutton
	menuframe = Frame(win)
	

	emptylabel5 = Label(menuframe,bg = '#191919',bd = 0)
	openbutton = Button(menuframe,bg = '#191919',activebackground = '#191919',fg = 'white',bd = 0,command = openfile,font = 'Consolas',image = openof,highlightthickness=0)
	emptylabel6 = Label(menuframe,bg = '#191919',bd = 0)
	exitbutton = Button(menuframe,text = '  Quit !  ',bg = '#191919',fg = 'white',bd = 0,activebackground = '#191919', command = exit,font = 'Consolas',image = closeof,highlightthickness=0)

	openbutton.bind('<Enter>', enteropen)
	openbutton.bind('<Leave>', leaveopen)

	exitbutton.bind('<Enter>', enterexit)
	exitbutton.bind('<Leave>', leaveexit)
	analyzebutton = Button(menuframe,bg = '#191919',activebackground = '#191919',fg = 'white',bd = 0,command = process,image = anazyle_img_of,highlightthickness=0)
	

	emptylabel5.grid(row = 1,column = 1, ipadx = 100,columnspan = 2)

	openbutton.grid(row=1,column = 3,rowspan = 3,columnspan = 4)

	emptylabel6.grid(row = 1,column = 8, ipadx = 100,columnspan = 2)

	exitbutton.grid(row=1,column = 10,rowspan = 3)

	menuframe.configure(background = '#191919')
	menuframe.grid(row = 1,rowspan = 8,column = 2,columnspan = 6)

def exit():

	global win
	win.destroy()
	sys.modules[__name__].__dict__.clear()
	quit()
fname = ''
def openfile():
	rep = askopenfilenames(parent=win, initialdir='/', initialfile='tmp',
	                       filetypes=[("Text", "*.txt|*.TXT"), ("All files", "*")])
	print(rep)
	global analyzebutton
	global fname
	global menuframe
	print(rep[0])

	fname = rep[0]


	analyzebutton.grid(row = 5,column = 1,columnspan = 4)
	analyzebutton.bind('<Enter>',enteranalyze)
	analyzebutton.bind('<Leave>',leaveanalyze)
	print('ohh yeah')
	successful('File Opened Successfully!\nPress the Analyze Button and Continue',highlightthickness=0)
	

sci = ['301','041','302','042','043','044','083']
com = ['301','302','030','041','030','054','055']
hum = []
#DB Config
db = sql.connect('my_db.db')
c = db.cursor()

#Functions
def science(c,db):
    c.execute('drop table if exists science')
    c.execute('create table science as select * from data where sc1 like "{}" and (sc2 like "{}" or sc2 like "{}") and sc3 like "{}" and sc4 like "{}" and (sc5 like "{}" or sc5 like "{}")'.format(*sci))
    db.commit()

def commerce(c,db):
    c.execute('drop table if exists commerce')
    c.execute('create table commerce as select * from data where sc1 like "{}" and (sc2 like "{}" or sc2 like "{}") and (sc3 like "{}" or sc3 like "{}") and sc4 like "{}" and sc5 like "{}"'.format(*com))
    db.commit()

def remove_spaces(raw_data):
  for i in raw_data:
    raw_data[raw_data.index(i)] = i[:-1]
  popper = []
  for i in range(len(raw_data)):
    if raw_data[i] == '' or raw_data[i] == '\n' or raw_data[i] == ' ':
      popper.append(i)
  

  for i in popper[::-1]:
    raw_data.pop(i)
  return raw_data
     
def school(raw_data):
  for i in raw_data:
    if 'SCHOOL : -' in i:
      schl = i
      break
  schl = schl.split()
  sclnm = ''
  for i in schl[4:]:
    sclnm += i+' '
  print(sclnm)
  # sclname = Label(win,text = sclnm,justify = CENTER,bg ='#232332',fg = 'white',font = ('Helvetica', 14, 'bold'))
  # sclname.grid(column = 0,columnspan = 10)
  return sclnm

def data(raw_data):
  popper = []
  for i in range(len(raw_data)):
    if (len(raw_data[i].split()) == 0) or (not raw_data[i].split()[0].isnumeric()):
      popper.append(i)
    #print(popper)
  for i in popper[::-1]:
    raw_data.pop(i)
  return raw_data

def arrange_names(raw_data):
  final_data = []
  for i in raw_data:
    s = ''
    lis = i.split()[2:]
    for j in lis:
      if j.isalpha():
        #print(j)
        s += j+' '
      else:
        break
    final_data.append(i.split()[:2]+[s[:-1]]+lis[-19:])

  return final_data

def int_marks(final_data):
  for i in range(len(final_data)):
    tmp = final_data[i]
    for j in range(len(tmp)):
      if j in [4,7,10,13,16]:
        tmp[j] = int(tmp[j])
    final_data[i] = tmp
  for i in range(len(final_data)):
    final_data[i] = final_data[i]+[(final_data[i][4]+final_data[i][7]+final_data[i][10]+final_data[i][13]+final_data[i][16])]

def insert(final_data):
  global db
  global c
  c.executemany('insert into data values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',final_data)

def db_setup():
  global db
  global c
  
  c.execute('drop table if exists data')
  c.execute('''create table data(roll text,sex text,name text,sc1 text,m1 integer,g1 text,sc2 text,m2 integer,g2 text,sc3 text,m3 integer,g3 text,sc4 text,m4 integer,g4 text,sc5 text,m5 integer,g5 text,gad1 text,gad2 text,gad3 text,res text,tot integer)''')
  db.commit()

def schoolsubextracter():
	global schoolsubs
	schoolsubs = []
	global subcodefetch
	for i in subcodefetch:
		for j in i:
			if j not in schoolsubs:
				schoolsubs.append(j)

def submarksextracter():
	global c,db,submarks,teachermarkdata,teachermarklist
	submarks = []
	teachermarkdata = {}
	teachermarklist = {}
	teacheraverages = {}
	c.execute('select sc1,m1,sc2,m2,sc3,m3,sc4,m4,sc5,m5 from data')
	rawmarks = c.fetchall()
	for i in rawmarks:
		for j in range(0,len(i),2):
			submarks.append([i[j],i[j+1]])
	for i in submarks:
		if i[0] in teachermarkdata:
			teachermarkdata[i[0]] += i[1]
			teachermarklist[i[0]].append(i[1])
			
		else:
			teachermarkdata[i[0]] = i[1]
			teachermarklist[i[0]] = [i[1]]
	for i in teachermarklist:
		teacheraverages[i] = round(sum(teachermarklist[i])/len(teachermarklist[i]),3)

	print(submarks)
	print(teachermarkdata)
	print(teachermarklist)
	print(teacheraverages)

	for i in teacheraverages:
		print(subcodes[i],teacheraverages[i])

def process():
	global f
	global c
	global db
	try:
		global fname
		f = open(fname)
		raw_data = f.readlines()
		f.close()
		raw_data = remove_spaces(raw_data)
		scl  = school(raw_data)
		raw_data = data(raw_data)
		final_data = arrange_names(raw_data)
		int_marks(final_data)
		db_setup()
		insert(final_data)
		science(c,db)
		commerce(c,db)
		print('Sucess!')

		global subcodefetch
		c.execute('select sc1,sc2,sc3,sc4,sc5 from data')
		subcodefetch = c.fetchall()
		for i in subcodefetch:
			print(i)
		
		schoolsubextracter()
		global schoolsubs
		for i in schoolsubs:
			print(i)	
		global submarksextracter	
		submarksextracter()

		c.execute('select * from data')
		for i in c:
			print(i)
		successful('Analyze Successful!')
		global pressmenubutton	
		pressmenubutton()

	except:
		global analyzeerror,okbutton,warnlabel
		analyzeerror = Tk()
		analyzeerror.configure(background = '#161616')
		analyzeerror.geometry('400x160+650+300')
		analyzeerror.overrideredirect('True')
		analyzeerror.attributes("-topmost", True)

		warnlabel = Label(analyzeerror,text = '\nThis File Can\'t Be Analyzed!\n', fg = 'red',font = ('Arial','15'),bg = '#161616',anchor = CENTER,padx = 50,pady = 20)
		warnlabel.pack(fill = BOTH)

		okbutton = Button(analyzeerror, text = 'OK!',fg = 'gray',bg = '#161616',bd = 0,padx = 50,pady = 20,command = lambda:analyzeerror.destroy(),activebackground = 'red',highlightthickness=0)
		okbutton.pack(fill = BOTH)
		# analyzeerror.mainloop()

# emptylabel1 = Label(win, bg = '#40a3ff')
# emptylabel2 = Label(win, bg = '#40a3ff')
# emptylabel3 = Label(win, bg = '#40a3ff')
# emptylabel4 = Label(win, bg = '#40a3ff')
# emptylabel1.grid(row = 2,ipadx = 68.5,ipady = 30)
# emptylabel2.grid(row = 4,ipadx = 68.5,ipady = 30)
# emptylabel3.grid(row = 6,ipadx = 68.5,ipady = 30)
# emptylabel4.grid(row = 8,ipadx = 68.5,ipady = 10)


graph = Button(win,image = graph_img_of,border = 0,highlightthickness = 0, bg = '#40a3ff', activebackground = '#191919',command = pressgraphbutton)
graph.grid(row = 1, ipadx = 10, ipady = 52)

search = Button(win,image = search_img_of,border = 0,highlightthickness = 0, bg = '#40a3ff', activebackground = '#191919',command = presssearchbutton)
search.grid(row = 3, ipadx = 10, ipady = 52)

doc = Button(win,image = doc_img_of,border = 0,highlightthickness = 0, bg = '#40a3ff', activebackground = '#191919', command = pressdocbutton,)
doc.grid(row = 5, ipadx = 10, ipady = 52)

menu = Button(win,image = menu_img_of,border = 0,highlightthickness = 0, bg = '#40a3ff', activebackground = '#191919',command = pressmenubutton,)
menu.grid(row = 7, ipadx = 10, ipady = 52)



# win.config(menu = menubar)

#BUTTON BINDING,S
graph.bind('<Enter>', entergraph)
graph.bind('<Leave>', leavegraph)

doc.bind('<Enter>', enterdoc)
doc.bind('<Leave>', leavedoc)

search.bind('<Enter>', entersearch)
search.bind('<Leave>', leavesearch)

menu.bind('<Enter>', entermenu)
menu.bind('<Leave>', leavemenu)

win.bind('f', xxx)


pressmenubutton()
win.mainloop()