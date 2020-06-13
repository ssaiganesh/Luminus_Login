from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
import loginfile #save loginfile under same folder as this file to run it

driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://luminus.nus.edu.sg/') 
nus_user_login = driver.find_element_by_xpath('/html/body/main/ng-component/div/div[2]/login/div[1]/div/a[1]') 
driver.execute_script("arguments[0].click()",nus_user_login)
userid = driver.find_element_by_id("userNameInput")
nususerid = loginfile.username 
userid.send_keys(nususerid) 
passwordinput = driver.find_element_by_id('passwordInput')
passwords = loginfile.password  
passwordinput.send_keys(passwords)
signin = driver.find_element_by_id('submitButton')
driver.execute_script("arguments[0].click()", signin)
#crossnotif = driver.find_element_by_xpath('/html/body/main/ng-component/dashboard-news-container/dashboard-news/section')
#driver.find_element_by_xpath('//div[@class="some-class"]/*[name()="svg"][@aria-label="Search"]').click()

#driver.execute_script("arguments[0].click()",crossnotif)

#driver.find_element_by_xpath("//body").click()
#crossnotif  = driver.find_element_by_xpath('/html/body/main/ng-component/dashboard-news-container/dashboard-news/section/aside/header/h2/icon/abbr/svg/path[1]')
#driver.execute_script("arguments[0].click()",crossnotif)

#login done not able to remove news notifications from screen yet. 

