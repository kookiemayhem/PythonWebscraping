import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Set Variables
TID = "TI1600631-000009"
# GRADE
# SN
# BUSID
# BRAND
# MODEL
# TYPE
# CONDITION
# CPUTYPE
# CPUMODEL
# CPUSPEED
# RAM
# HDDTYPE
# HDDSIZE
# MEMSTOCK
# BATTERY
# DVD
# ISSUES
# RESULTS
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

def login():
	br.get(web_login)
	user = br.find_element_by_id("txt_username")
	submit = br.find_element_by_id("imb_login")
	passwd = br.find_element_by_id("txt_password")
	user.send_keys("username")
	passwd.send_keys("password")
	submit.click()



def adjustment():
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
def enterdata():
#	br.find_element_by_id("txtSN").clear()
	br.find_element_by_xpath("//*[@id='rblFlag_0']").click() # Click on RTC Button
	br.find_element_by_id("txtSN").send_keys("test")
	dropdown = Select(br.find_element_by_id('ddlGrade'))
	dropdown.select_by_value("290")
	dropdown = Select(br.find_element_by_id('ddlManufacturer'))
	dropdown.select_by_value("1570")
	time.sleep( 2 )
	dropdown = Select(br.find_element_by_id('ddlModel'))
	dropdown.select_by_value("13997")

login()
adjustment()
enterdata()