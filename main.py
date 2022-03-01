#!/usr/bin/python3

import time , random
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

#color

class color:
      BOLD = '\033[1m'
      RED = '\33[31m'


desired_capabilities = {
    
    "deviceName":"192.168.1.4:5555" ,

    "platformName":"android" ,

#    "appPackage":"com.hiketop.app" ,

#    "appActivity":"com.hiketop.app.activities.splash.SplashActivity" ,

    "noReset":"true"

}

try:
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    print(color.BOLD)
    
    print("[+]Connected !")

except Exception as err:
    
    print(color.RED + "[+]Error while connecting to device")
    print()
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

secs = random.uniform(4.1, 5.3)

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

    try:
        
        read_username = driver.find_element(By.ID, 'com.instagram.android:id/profile_header_full_name').text
        xpath = """//android.widget.Button[@content-desc="Follow """ + read_username + """"]"""

        check_follow_status = driver.find_element(By.XPATH, xpath).text

        if check_follow_status == "Following":
            print("[+]aLreadY foLloweD skipping...")

        else:
            driver.find_element(By.XPATH, xpath).click()

    except Exception as err:
        
        print()
        print("[+]xpath not found , trying 2nd method")
        read_username1 = driver.find_element(By.ID, 'com.instagram.android:id/action_bar_title').text
        xpath = """//android.widget.Button[@content-desc="Follow """ + read_username1 + """"]"""
        
        check_follow_status = driver.find_element(By.XPATH, xpath).text

        if check_follow_status == "Following":
            print("[+]aLreadY foLloweD skipping...")

        else:
            driver.find_element(By.XPATH, xpath).click()

follow_ig()

time.sleep(secs)

#Return to hiketop app after completing the task

def return_to_app() :
    driver.press_keycode(82)
    time.sleep(secs)
    user_action.tap(x=798, y=1332).perform()
    try :
        time.sleep(1)
        logo_ppl_button.click()
    except Exception as err:
        print()

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
