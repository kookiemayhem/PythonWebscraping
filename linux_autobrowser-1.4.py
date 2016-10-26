#!/user/bin/python
#	Programmer: Leo Rocha
#	Date Modified: 09-27-2016

###		Edit History	###
#	Version 1.1
# - Combined model_search.py to the main script
# - Set Variables for the model_search functions
# - Needs var file imported for the rest of vars waiting to be set.
#	Version 1.0
# - Added All Variables to Selenium Browser Automation
#	Version 1.2
# - added exceptions for find.by.element handlers
# - added receive function to receive new traveler id's
# - added popup detection in case the traveler id is not found when receiving.
#	Version 1.3
# - changed regex search for better compatibility 
# - added a wait for element for the adjustment page. (before entering data)
#	Version 1.4
# - reverted from using firefox, switched to chrome browser
# - successful run on linux with chrome without additional delays (removed extra delays)
# - correctly closes popup window when traveler id is already received.
# - added usernames and passwords for corresponding Bus Id's for Tech's.
# - logins added for Leo and Sean atm, default login is Leo for Ruben and Matt
# - Bus Id's are now available for initials of lr, mm, rf, sp.
# - added prompt before launching the browser to identify who is running the script.

import time, re, sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By # Alternate method for selecting Traveler ID
# from selenium.webdriver.common.keys import Keys # For simulating enter and other keyboard keys. (not used)
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC # for firefox
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities # for firefox
from vars import *

MODEL = ' '.join(MODEL.split()).split('(')[0].lower()
CPUMODEL = ' '.join(CPUMODEL.split()).lower()
FIX_MODEL = re.search('[\w\d\-\s]+', MODEL)
MODEL = FIX_MODEL.group(0)
FIX_CPU = re.search('\w+-?\d+\w+', CPUMODEL)
CPUMODEL = FIX_CPU.group(0) 
print "CPU Input: %s" % CPUMODEL
print "Model Input: %s" % MODEL
# c = 381
# Create Results File for Operations
with open("results.txt", "w") as r:
	print "Created Results File"
# Inputs Model and CPU Value to find a match
with open("/mnt/test-lab-gil/prc/prc.txt", "r") as database:
	# prc = database.read()
	""" For loop goes through the PRC file 
	and finds possible matches for CPU an PC MODEL
	"""
	for line in database:
		line = ' '.join(line.split()).lower().replace('@', '').replace('/', '#').split('>')[0].strip()
		# print line
		# line = line.split(',')
		# print line[0]
		mdl_search = re.search('^mdl:([\w\d\-\s]+),(\d+),(\d+),(\d+)', line)
		if mdl_search != None:
			# print line
			# print mdl_search.group(1)
			if MODEL == mdl_search.group(1):

				with open("results.txt", "a") as target:
					target.writelines("%s\n" % line)
				mdl_match = mdl_search.group(1,2,3,4)
				# print mdl_match
		cpu_search = re.search('^prc.([a-z]?\s?\d?\w+\d?-?\w+\s?\w+-?[a-z]?\d?\d?[a-z]?),(\d+),(\d+),(\d+)', line)
		if cpu_search != None:
			# print cpu_search.group(1)
			if CPUMODEL == cpu_search.group(1):
				with open("results.txt", "a") as target:
					target.write("%s\n" % line)
				cpu_match = cpu_search.group(1,2,3,4)
# try:
print cpu_match
print mdl_match
# except:
	# print NameError('missing matches')
# Tkinter Login Window
root = Tk()
root.geometry("150x200")
root.title("Technician Login")
opt = IntVar()
bottom = Frame(root, bg='green', width=20)
bottom.pack(side=BOTTOM, anchor=W)
def sel():
	global USR, USRPASSWD, BUSID
	print "Option Selected " + str(opt.get())
	selection = "You selected Technician " + str(opt.get())
	label.config(text = selection)
	Choice = int(opt.get())
	if Choice == 1:					# lr
		USR = "username"
		USRPASSWD = "password"
		BUSID = "TL14081900003"
		print "Tech: %s \nBusID: %s" %(USR, BUSID)
	elif Choice == 2:				# mm
		USR = "username"
		USRPASSWD = "password"
		BUSID = "TL15011600001"
		print "Tech: %s \nBusID: %s" %(USR, BUSID)
	elif Choice == 3:				# sp
		USR = "username3"
		USRPASSWD = "password"
		BUSID = "TL14081900001"
		print "Tech: %s \nBusID: %s" %(USR, BUSID)
	elif Choice == 4:				# rf
		USR = "username"
		USRPASSWD = "password"
		BUSID = "TL14081900007"
		print "Tech: %s \nBusID: %s" %(USR, BUSID)
	else:
		print Choice + " not valid, good bye."
	more = "Tech: %s \nBusID: %s" %(USR, BUSID)
	info.config(text=more, anchor=W, justify=LEFT)
def gui_end():
	print "\nClosing Login Window..."
	root.quit()

# Gui Objects Start Here
C1 = Radiobutton(root, anchor=W, indicatoron=False, width=20, bg='white', text="Technician: Leo", variable=opt, value=1, command=sel, relief=RAISED)
C1.pack( anchor = W )
C2 = Radiobutton(root, anchor=W, indicatoron=False, width=20, bg='white', text="Technician: Matthew", variable=opt, value=2, command=sel, relief=RAISED)
C2.pack( anchor = W )
C3 = Radiobutton(root, anchor=W, indicatoron=False, width=20, bg='white', text="Technician: Sean", variable=opt, value=3, command=sel, relief=RAISED)
C3.pack( anchor = W )
C4 = Radiobutton(root, anchor=W, indicatoron=False, width=20, bg='white', text="Technician: Ruben", variable=opt, value=4, command=sel, relief=RAISED)
C4.pack( anchor = W )
label = Label()
label.pack(anchor=W)
info = Label()
info.pack(anchor=W)
Submit = Button(bottom, width=20, bg='green', text="Accept Selection", command=gui_end)
Submit.pack(anchor= W )
mainloop()


# Set Variables
# TID = "TI1600631-000009"
# GRADE = "283" # PASS 	"290" - FAIL
# SN

BRAND = mdl_match[2]	# Manufacture of Model
MODEL = mdl_match[1] 	# PC Model
TYPE = 	mdl_match[3]# Technology Type
# CONDITION = "135" # PASS "136" - FAIL
CPUTYPE = cpu_match[1]
CPUMODEL = cpu_match[2]
CPUSPEED = cpu_match[3]
CPUQTY = "2834"
HDDQTY = "2854"
HDDWIPE = "3343"
# RAM
# HDDTYPE
	# no caddy: 3840
	# no hdd: 2853
	# sata: 2792
	# sata ssd: 3327
# HDDSIZE
# MEMSTOCK
# BATTERY
# DVD
# ISSUES
# RESULTS = "3347" # Hardware Diagnostics Pass
# NOTE

# selector ID's
#txtSN
#txtBusID
#ddlGrade
#ddlCondition
#ddlManufacturer
#ddlTechnology
#ddlModel
#dlddlProperty_ctl01_ddlPropertyValue # cpu speed
#dlddlProperty_ctl06_ddlPropertyValue # cpu type
#dlddlProperty_ctl11_ddlPropertyValue # cpu model
#dlddlProperty_ctl07_ddlPropertyValue # Ram size
#dlddlProperty_ctl08_ddlPropertyValue # HDD size
#dlddlProperty_ctl03_ddlPropertyValue # HDD/Ram added or stock?
#dlddlProperty_ctl10_ddlPropertyValue # Optical Drive


# Laptop Selectors
#dlddlProperty_ctl09_ddlPropertyValue # Laptop Battery



# Constant Selector ID's 
#dlddlProperty_ctl00_ddlPropertyValue # cpu qty
#dlddlProperty_ctl02_ddlPropertyValue # hdd type
#dlddlProperty_ctl12_ddlPropertyValue # hdd qty
#dlddlProperty_ctl08_ddlPropertyValue # Data Erasure
#dlddlProperty_ctl05_ddlPropertyValue # Diagnostics Results


# Firefox options
# caps = DesiredCapabilities.FIREFOX
# caps["marionette"] = True
# caps["binary"] = "/home/ubuntu/selenium/firefox-sdk/bin/firefox"
# br = webdriver.Firefox(capabilities=caps)

# Browser
br = webdriver.Chrome() # Linux
# br = webdriver.Chrome('C:\python27\scripts\chromedriver.exe')	# Windows
# br = webdriver.Firefox()	# Linux
# Browser Varriables
web_login = "https://secure2.cyclelution.com/CycleLutionV3/Default.aspx"
web_adjust = "https://secure2.cyclelution.com/CycleLutionV3/Inventory/Adjustment.aspx"
receive_inventory = "https://secure2.cyclelution.com/CycleLutionV3/Inventory/SortingByTravelerID.aspx"

def login():
	try:
		br.get(web_login)
		user = br.find_element_by_id("txt_username")
		submit = br.find_element_by_id("imb_login")
		passwd = br.find_element_by_id("txt_password")
		user.send_keys(USR)
		passwd.send_keys(USRPASSWD)
		submit.click()
		# time.sleep(5)
	except NoSuchElementException:
		print "No element in login"

def receive():
	try:
		br.get(receive_inventory)
		# time.sleep(10)
		traveler_list = br.find_element_by_id('txtScanNumber')
		traveler_list.send_keys(TID)
		busid_assign = br.find_element_by_id('txtNewBusID')
		busid_assign.send_keys(BUSID)
		ready_list = br.find_element_by_id('btnScan')
		ready_list.click()
		# time.sleep(12)
		receive_list = br.find_element_by_id('imbtnReceive')
		receive_list.click()
		# time.sleep(20)

	except NoSuchElementException:
		print "No element found in receive"
	except UnexpectedAlertPresentException:
		popup = br.switch_to_alert()
		print "popup message: %s" % popup.text
		already_received = re.search("Traveler ID not in inventory", popup.text)
		if already_received != None:
			popup.dismiss()
			print "closed popup"
		else:
			print "did not catch popups"
		# sys.exit(1)

def adjustment():
	try:
		br.get(web_adjust)
		# time.sleep(5)
		SearchType = br.find_element_by_name("Searchbar_Inventory$ddl_condition")
	#	Search = br.find_element_by_xpath("//*[@id='Searchbar_Inventory_txt_value']")
	#	SearchSubmit = br.find_element_by_xpath("//*[@id='Searchbar_Inventory_bt_search']")
		SearchType.send_keys("Traveler ID")
		# time.sleep(1)
		# br.find_element_by_xpath("//*[@id='Searchbar_Inventory_txt_value']").clear()
		br.find_element_by_xpath("//*[@id='Searchbar_Inventory_txt_value']").send_keys(TID)
		# time.sleep(2)
		# SearchBar = br.find_element_by_id('Searchbar_Inventory_bt_search')
		br.find_element_by_id('Searchbar_Inventory_bt_search').click()
		# SearchBar.submit()
		# SearchBar.send_keys(Keys.RETURN)
		# SearchWait = WebDriverWait(br, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='gvInventory']/tbody/tr[2]/td[2]/a")))
		# time.sleep(10)
		br.find_element_by_xpath("//*[@id='gvInventory']/tbody/tr[2]/td[2]/a").click()
		# time.sleep(20)
	except NoSuchElementException:
		print "No element found in adjustment"
def enterdata():
	try:
		br.find_element_by_id("txtSN").clear()
		br.find_element_by_xpath("//*[@id='rblFlag_0']").click() # Click on RTC Button
		# time.sleep(5)
		br.find_element_by_id("txtSN").send_keys(SN)
		dropdown = Select(br.find_element_by_id('ddlGrade'))
		dropdown.select_by_value(GRADE)
		dropdown = Select(br.find_element_by_id('ddlManufacturer'))
		dropdown.select_by_value(BRAND)
		# time.sleep(2)
		dropdown = Select(br.find_element_by_id('ddlCondition'))
		dropdown.select_by_value(CONDITION)
		time.sleep( 3 )
		dropdown = Select(br.find_element_by_id('ddlModel'))
		dropdown.select_by_value(MODEL)

	# Defined elements
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl00_ddlPropertyValue')) # cpu qty
		dropdown.select_by_value(CPUQTY)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl06_ddlPropertyValue')) # cpu type
		dropdown.select_by_value(CPUTYPE)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl11_ddlPropertyValue')) # cpu model
		dropdown.select_by_value(CPUMODEL)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl01_ddlPropertyValue')) # cpu speed
		dropdown.select_by_value(CPUSPEED)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl07_ddlPropertyValue')) # ram size
		dropdown.select_by_value(RAM)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl02_ddlPropertyValue')) # hdd type
		dropdown.select_by_value(HDDTYPE)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl08_ddlPropertyValue')) # hdd size
		dropdown.select_by_value(HDDSIZE)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl03_ddlPropertyValue')) # hdd/ram added or stock?
		dropdown.select_by_value(MEMSTOCK)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl10_ddlPropertyValue')) # optical drive
		dropdown.select_by_value(DVD)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl09_ddlPropertyValue')) # labtop battery
		dropdown.select_by_value(BATTERY)

	# Constant Values

		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl12_ddlPropertyValue')) # hdd qty
		dropdown.select_by_value(HDDQTY)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl13_ddlPropertyValue')) # data erasure
		dropdown.select_by_value(HDDWIPE)
		dropdown = Select(br.find_element_by_id('dlddlProperty_ctl05_ddlPropertyValue')) # results
		dropdown.select_by_value(RESULTS)
	except NoSuchElementException:
		print "No element found"



login()
receive()
adjustment()
enterdata()