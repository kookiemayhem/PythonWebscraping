import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Set Variables
TID = "TI1600631-000009"
GRADE = "283" # PASS 	"290" - FAIL
# SN
BUSID = "TL14081900003"
# BRAND
# MODEL
# TYPE
CONDITION = "135" # PASS "136" - FAIL
# CPUTYPE
# CPUMODEL
# CPUSPEED
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
RESULTS = "3347" # Hardware Diagnostics Pass
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
	dropdown.select_by_value(GRADE)
	dropdown = Select(br.find_element_by_id('ddlManufacturer'))
	dropdown.select_by_value(BRAND)
	time.sleep( 2 )
	dropdown = Select(br.find_element_by_id('ddlModel'))
	dropdown.select_by_value(MODEL)

# Defined elements
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl01_ddlPropertyValue')) # cpu speed
	dropdown.select_by_value(CPUSPEED)
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl06_ddlPropertyValue')) # cpu type
	dropdown.select_by_value(CPUTYPE)
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl11_ddlPropertyValue')) # cpu model
	dropdown.select_by_value(CPUMODEL)
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl07_ddlPropertyValue')) # ram size
	dropdown.select_by_value(RAM)
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl02_ddlPropertyValue')) # hdd type
	dropdown.select_by_value(HDDTYPE)
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl08_ddlPropertyValue')) # hdd size
	dropdown.select_by_value(HDDSIZE)
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl03_ddlPropertyValue')) # hdd/ram added or stock?
	dropdown.select_by_value(MEMSTOCK)
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl0_ddlPropertyValue')) # optical drive
	dropdown.select_by_value(DVD)
	# dropdown = Select(br.find_element_by_id('dlddlProperty_ctl09_ddlPropertyValue')) # labtop battery
	# dropdown.select_by_value(BATTERY)

# Constant Values
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl00_ddlPropertyValue')) # cpu qty
	dropdown.select_by_value("2834")
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl12_ddlPropertyValue')) # hdd qty
	dropdown.select_by_value("2854")
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl08_ddlPropertyValue')) # data erasure
	dropdown.select_by_value("3343")
	dropdown = Select(br.find_element_by_id('dlddlProperty_ctl05_ddlPropertyValue')) # results
	dropdown.select_by_value(RESULTS)



login()
adjustment()
enterdata()