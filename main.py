#!/usr/bin/python3

import time , random
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

#color

class color:
      BOLD = '\033[1m'
      RED = '\33[31m'


desired_capabilities = {
    
    "deviceName":"192.168.1.4:5555" ,

    "platformName":"android" ,

    "appPackage":"com.hiketop.app" ,

    "appActivity":"com.hiketop.app.activities.splash.SplashActivity" ,

    "noReset":"true"

}

try:
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    print(color.BOLD)
    
    print("[+]Connected !")

except Exception as err:
    
    print()
    print(color.RED + "[+]Error while connecting to device")
    option = input("[+]Do you want to print error log? (y/n) ")

    if option == "y":
        print(err)
        exit()

    elif option == "n":
        exit()

    else:
        print("[+]No such option , exiting")
        exit()
    

#seconds (time to wait)

secs = random.uniform(1.5, 2)

#Elements & Action
print()
print("[+]oPeNiNg app ...")
time.sleep(secs)
logo_ppl_button = driver.find_element(By.ID, 'com.hiketop.app:id/left_1_image_button')
logo_ppl_button.click()

print()
print("[+]PeRfOrMiNg, Task")
print()

time.sleep(secs)

user_action = TouchAction(driver)

#hiketop touch action function with unfixed x , y co-ordinate values & can be adjusted

def follow_hiketop(COx, COy):
    user_action.tap(x=COx, y=COy).perform()

#Hiketop touch action function with fixed x , y co-ordinates value of first people on right

#Task 1

def ppl_task1() :
    x1 = 815
    y1 = 916

    follow_hiketop(x1, y1)

ppl_task1()

#Instagram follow button create xpath function

time.sleep(secs)

def follow_ig() :

    global no_such_element

    try:

        no_such_element = "False"

        try:
            
            read_username_id = "com.instagram.android:id/profile_header_full_name"

            read_username = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, read_username_id))
        ).text

            xpath = """//android.widget.Button[@content-desc="Follow """ + read_username + """"]"""
            
            message_xpath = '//android.widget.Button[@text="Message"]'

            check_follow_status = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        ).text

            try:
                check_private_status = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, message_xpath))
        ).text

            except Exception as err:
                check_private_status = "Private account"    

            if check_follow_status == "Following":
                print("[+]aLreadY foLloweD skipping...")

            elif check_private_status == "Private account":
                pass

            else:
                driver.find_element(By.XPATH, xpath).click()

        except Exception as err:
            

            read_fullname_id = 'com.instagram.android:id/action_bar_title'
            
            read_fullname = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, read_fullname_id))
        ).text

            xpath = """//android.widget.Button[@content-desc="Follow """ + read_fullname + """"]"""

            message_xpath = """//android.widget.Button[@text="Message"]"""
            
            check_follow_status = driver.find_element(By.XPATH, xpath).text

            try:
                check_private_status = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, message_xpath))
        ).text

            except Exception as err:
                check_private_status = "Private account"


            if check_follow_status == "Following":
                print("[+]aLreadY foLloweD skipping...")

            elif check_private_status == "Private account":
                pass            

            else:
                driver.find_element(By.XPATH, xpath).click()
    
    except Exception as err:

        no_such_element = "true"

        pass
        

follow_ig()

time.sleep(secs)

#Return to hiketop app after completing the task

def return_to_app() :

    if no_such_element == "true":
        pass

    else:
        driver.press_keycode(82)
        time.sleep(3)
        user_action.tap(x=798, y=1332).perform()
        try :
            pass
        except Exception as err:
            time.sleep(3)
            logo_ppl_button.click()

return_to_app()

#Task 2

time.sleep(secs)

def ppl_task2() :
    
    x2 = 272
    y2 = 1677

    follow_hiketop(x2, y2)

ppl_task2()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 3

time.sleep(secs)

def ppl_task3() :
    x2 = 825
    y2 = 1677

    follow_hiketop(x2, y2)

ppl_task3()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Scroll

def scroll_hiketop() :
    user_action.press(x=530, y=1745).move_to(x=530, y=205).release().perform()

time.sleep(secs)

scroll_hiketop()

#Task 4

def ppl_task4() :
    x2=228
    y2=892

    follow_hiketop(x2, y2)

ppl_task4()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Now, I can repeat the upper code from ppl_task4 to ppl_task3 (kinda messed up on naming variables) , till i reach 30 ppls 
# it's like 4,1,2,3 scroll & then repeat 

#Task 5

time.sleep(secs)

ppl_task1()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 6

time.sleep(secs)

ppl_task2()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 7

time.sleep(secs)

ppl_task3()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Scroll

time.sleep(secs)
scroll_hiketop()

#Task 8

time.sleep(secs)

ppl_task4()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 9

time.sleep(secs)

ppl_task1()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 10

time.sleep(secs)

ppl_task2()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 11

time.sleep(secs)

ppl_task3()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Scroll

time.sleep(secs)
scroll_hiketop()

#Task 12

time.sleep(secs)

ppl_task4()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 13

time.sleep(secs)

ppl_task1()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 14

time.sleep(secs)

ppl_task2()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 15

time.sleep(secs)

ppl_task3()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Scroll

time.sleep(secs)
scroll_hiketop()

#Task 16

time.sleep(secs)

ppl_task4()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 17

time.sleep(secs)

ppl_task1()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 18

time.sleep(secs)

ppl_task2()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 19

time.sleep(secs)

ppl_task3()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Scroll

time.sleep(secs)
scroll_hiketop()

#Task 20

time.sleep(secs)

ppl_task4()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 21

time.sleep(secs)

ppl_task1()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 22

time.sleep(secs)

ppl_task2()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()


#Task 23

time.sleep(secs)

ppl_task3()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()


#Scroll

time.sleep(secs)
scroll_hiketop()


#Task 24

time.sleep(secs)

ppl_task4()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 25

time.sleep(secs)

ppl_task1()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 26

time.sleep(secs)

ppl_task2()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 27

time.sleep(secs)

ppl_task3()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Scroll

time.sleep(secs)
scroll_hiketop()

#Task 28

time.sleep(secs)

ppl_task4()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 29

time.sleep(secs)

ppl_task1()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Task 30

time.sleep(secs)

ppl_task2()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

print("[+]phew!, that was some hardword ;)")
