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

import time, re, sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from vars import *

MDL = ' '.join(MDL.split()).split('(')[0].lower()
CPU = ' '.join(CPU.split()).lower()
FIX_MDL = re.search('\w+\d+', MDL)
MDL = FIX_MDL.group(0)
FIX_CPU = re.search('\w+-?\d+\w+', CPU)
CPU = "prc:" + FIX_CPU.group(0) 
print CPU
print FIX_CPU
# c = 381
# Create Results File for Operations
with open("results.txt", "w") as r:
	print "Created Results File"
# Inputs Model and CPU Value to find a match
with open("prc.txt", "r") as database:
	# prc = database.read()
	""" For loop goes through the PRC file 
	and finds possible matches for CPU an PC MODEL
	"""
	for line in database:
		line = ' '.join(line.split()).lower().replace('@', '').replace('/', '#').split('>')[0].strip()
		# print line
		line = line.replace('mdl:', '').split(',')
		# print line[0]
		mdl_search = re.search('\w+\d+', line[0])
		if mdl_search != None:
			if MDL == mdl_search.group(0):
				# print line
			# print mdl_search.group(0)
				with open("results.txt", "a") as target:
					target.writelines("%s\n" % line[0])
				mdl_match = line
					# print mdl_match
		cpu_search = re.search('^prc.[a-z]?\s?\d?\w+\d?-?\w+\s?\w+-?[a-z]?\d?\d?[a-z]?', line[0])
		if cpu_search:
			# print cpu_match.group(0)
			if CPU == cpu_search.group(0) != None:
				with open("results.txt", "a") as target:
					target.write("%s\n" % line[0])
				cpu_match = line

print cpu_match
print mdl_match

# Set Variables
# TID = "TI1600631-000009"
# GRADE = "283" # PASS 	"290" - FAIL
# SN
BUSID = "TL14081900003"
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



# Browser
br = webdriver.Chrome('C:\python27\scripts\chromedriver.exe')
# Browser Varriables
web_login = "https://secure2.cyclelution.com/CycleLutionV3/Default.aspx"
web_adjust = "https://secure2.cyclelution.com/CycleLutionV3/Inventory/Adjustment.aspx"
receive_inventory = "https://secure2.cyclelution.com/CycleLutionV3/Inventory/SortingByTravelerID.aspx"

def login():
	br.get(web_login)
	user = br.find_element_by_id("txt_username")
	submit = br.find_element_by_id("imb_login")
	passwd = br.find_element_by_id("txt_password")
	user.send_keys("username")
	passwd.send_keys("password")
	submit.click()

def receive():
	br.get(receive_inventory)
	try:
		traveler_list = br.find_element_by_id('txtScanNumber')
		traveler_list.send_keys(TID)
		busid_assign = br.find_element_by_id('txtNewBusID')
		busid_assign.send_keys(BUSID)
		ready_list = br.find_element_by_id('btnScan')
		ready_list.click()
		receive_list = br.find_element_by_id('imbtnReceive')
		receive_list.click()

	except NoSuchElementException:
		print "No element found"
	except UnexpectedAlertPresentException:
		popup = br.switch_to_alert()
		print "popup message: %s" % popup.text
		sys.exit(1)

def adjustment():
	try:
		br.get(web_adjust)
		SearchType = br.find_element_by_name("Searchbar_Inventory$ddl_condition")
	#	Search = br.find_element_by_xpath("//*[@id='Searchbar_Inventory_txt_value']")
	#	SearchSubmit = br.find_element_by_xpath("//*[@id='Searchbar_Inventory_bt_search']")
		SearchType.send_keys("Traveler ID")
		br.find_element_by_xpath("//*[@id='Searchbar_Inventory_txt_value']").clear()
		br.find_element_by_xpath("//*[@id='Searchbar_Inventory_txt_value']").send_keys(TID)
		print SearchType
		br.find_element_by_xpath("//*[@id='Searchbar_Inventory_bt_search']").click()
		br.find_element_by_xpath("//*[@id='gvInventory']/tbody/tr[2]/td[2]/a").click()
	except NoSuchElementException:
		print "No element found"
def enterdata():
	try:
	#	br.find_element_by_id("txtSN").clear()
		br.find_element_by_xpath("//*[@id='rblFlag_0']").click() # Click on RTC Button
		br.find_element_by_id("txtSN").send_keys(SN)
		dropdown = Select(br.find_element_by_id('ddlGrade'))
		dropdown.select_by_value(GRADE)
		dropdown = Select(br.find_element_by_id('ddlManufacturer'))
		dropdown.select_by_value(BRAND)
		dropdown = Select(br.find_element_by_id('ddlCondition'))
		dropdown.select_by_value(CONDITION)
		time.sleep( 2 )
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
		# dropdown = Select(br.find_element_by_id('dlddlProperty_ctl09_ddlPropertyValue')) # labtop battery
		# dropdown.select_by_value(BATTERY)

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