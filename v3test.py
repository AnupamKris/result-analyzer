from tkinter import *
from tkfilebrowser import askopenfilenames
from tkinter import messagebox
import sqlite3 as sql
import sys
from subcodes import subcodes
# from customwarnings import successful

win = Tk()
w=win.winfo_screenwidth()
h=win.winfo_screenheight()
win.configure(background = '#191919')
win.geometry("{0}x{1}+0+0".format(w,h))
win.overrideredirect(True)
from images import *



#BUTTON IMAGE DEFINITIONS

def successful(msg):
	global Warning,okbutton,warnlabel
	warning = Tk()
	warning.configure(background = '#161616')
	warning.geometry('400x160+650+300')
	warning.overrideredirect('True')
	warning.attributes("-topmost", True)

	warnlabel = Label(warning,text = f'\n{msg}\n', fg = '#03fcc2',font = ('Arial','15'),bg = '#161616',anchor = CENTER,padx = 50,pady = 20)
	warnlabel.pack(fill = BOTH)

	okbutton = Button(warning, text = 'OK!',fg = 'gray',bg = '#161616',bd = 0,padx = 50,pady = 20,command = lambda:warning.destroy(),activebackground = '#03fcc2')
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
	graphframe = Frame(win)
	graphframe.configure(background = '#191919')
	graphframe.grid(row = 1,rowspan = 8,column = 2,columnspan = 6)

def presssearchbutton():
	global active
	exec(active + '.destroy()')
	active = 'searchframe'

	global searchframe
	searchframe = Frame(win)
	searchframe.configure(background = '#191919')
	searchframe.grid(row = 1,rowspan = 8,column = 2,columnspan = 6)

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
	openbutton = Button(menuframe,bg = '#191919',activebackground = '#191919',fg = 'white',bd = 0,command = openfile,font = 'Consolas',image = openof)
	emptylabel6 = Label(menuframe,bg = '#191919',bd = 0)
	exitbutton = Button(menuframe,text = '  Quit !  ',bg = '#191919',fg = 'white',bd = 0,activebackground = '#191919', command = exit,font = 'Consolas',image = closeof)

	openbutton.bind('<Enter>', enteropen)
	openbutton.bind('<Leave>', leaveopen)

	exitbutton.bind('<Enter>', enterexit)
	exitbutton.bind('<Leave>', leaveexit)
	analyzebutton = Button(menuframe,bg = '#191919',activebackground = '#191919',fg = 'white',bd = 0,command = process,image = anazyle_img_of,)
	

	emptylabel5.grid(row = 1,column = 1, ipadx = 100,columnspan = 2)

	openbutton.grid(row=1,column = 3,rowspan = 3,columnspan = 4)

	emptylabel6.grid(row = 1,column = 8, ipadx = 100,columnspan = 2)

	exitbutton.grid(row=1,column = 10,rowspan = 3)

	menuframe.configure(background = '#191919')
	menuframe.grid(row = 1,rowspan = 8,column = 2,columnspan = 6)

def exit():

	global win
	win.destroy()
	#sys.modules[__name__].__dict__.clear()
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
	successful('File Opened Successfully!')
	

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

def process():
	global f
	global c
	global db
	# try:
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
	global schoolsubextracter
	schoolsubextracter()
	global schoolsubs
	for i in schoolsubs:
		print(i)	
	global submarksextracter	
	submarksextracter()
	successful('Analyze Successful')
	
	c.execute('select * from data')
	for i in c:
		print(i)
	global pressmenubutton
	pressmenubutton()

	# except:
	# 	global analyzeerror,okbutton,warnlabel
	# 	analyzeerror = Tk()
	# 	analyzeerror.configure(background = '#161616')
	# 	analyzeerror.geometry('400x160+650+300')
	# 	analyzeerror.overrideredirect('True')
	# 	analyzeerror.attributes("-topmost", True)

	# 	warnlabel = Label(analyzeerror,text = '\nThis File Can\'t Be Analyzed!\n', fg = 'red',font = ('Arial','15'),bg = '#161616',anchor = CENTER,padx = 50,pady = 20)
	# 	warnlabel.pack(fill = BOTH)

	# 	okbutton = Button(analyzeerror, text = 'OK!',fg = 'gray',bg = '#161616',bd = 0,padx = 50,pady = 20,command = lambda:analyzeerror.destroy(),activebackground = 'red')
	# 	okbutton.pack(fill = BOTH)




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

doc = Button(win,image = doc_img_of,border = 0,highlightthickness = 0, bg = '#40a3ff', activebackground = '#191919', command = pressdocbutton)
doc.grid(row = 5, ipadx = 10, ipady = 52)

menu = Button(win,image = menu_img_of,border = 0,highlightthickness = 0, bg = '#40a3ff', activebackground = '#191919',command = pressmenubutton)
menu.grid(row = 7, ipadx = 10, ipady = 52)

# subcode fetch

def schoolsubextracter():
	global schoolsubs
	schoolsubs = []
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
# def PICalculator():
# 	global c,db,
# 	c.execute('select sc1,g1 from data')




# win.config(menu = menubar)

#BUTTON BINDINGS
graph.bind('<Enter>', entergraph)
graph.bind('<Leave>', leavegraph)

doc.bind('<Enter>', enterdoc)
doc.bind('<Leave>', leavedoc)

search.bind('<Enter>', entersearch)
search.bind('<Leave>', leavesearch)

menu.bind('<Enter>', entermenu)
menu.bind('<Leave>', leavemenu)

pressmenubutton()
win.mainloop()