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
print()

#Instagram follow button create xpath function

time.sleep(secs)

def follow_ig() :

    global NO_SUCH_ELEMENT

try:

    try:

        NO_SUCH_ELEMENT = "False"
            
        FOLLOW_XPATH = '//android.widget.Button[@text="Follow"]'
            
        MESSAGE_XPATH = '//android.widget.Button[@text="Message"]'

        FOLLOWING_XPATH = '//android.widget.Button[@text="Following"]'

        try:

            CHECK_PRIVATE_STATUS = driver.find_element(By.XPATH, MESSAGE_XPATH).text

        except Exception as err:

            CHECK_PRIVATE_STATUS = "Private account"

        try:

            CHECK_FOLLOWING_STATUS = driver.find_element(By.XPATH, FOLLOWING_XPATH).text
            
        except Exception as err:

            CHECK_FOLLOWING_STATUS = "Not followed"

            
        if CHECK_FOLLOWING_STATUS == "Following":

            print("[+] NOT OK , FOLLOWED ACC ...")
            pass


        elif CHECK_PRIVATE_STATUS == "Private account":

            print("[+] NOT OK , PRIVATE ACC ...")
            pass

        else:

            driver.find_element(By.XPATH, FOLLOW_XPATH).click()
            print("[+] OK")
    
    except Exception as err:

        print(mistake not defined) # Doing mistake consciously

except Exception as err:
    
    NO_SUCH_ELEMENT = "true"
        

follow_ig()

time.sleep(secs)

#Return to hiketop app after completing the task

def return_to_app() :

    if NO_SUCH_ELEMENT == "true":
        pass

    else:
        driver.press_keycode(82)
        time.sleep(3)
        user_action.tap(x=798, y=1332).perform()

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
    x3 = 825
    y3 = 1677

    follow_hiketop(x3, y3)

ppl_task3()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Scroll

def scroll_hiketop() :
    time.sleep(2)
    user_action.press(x=530, y=1745).move_to(x=530, y=205).release().perform()

time.sleep(secs)

scroll_hiketop()

#Task 4

def ppl_task4() :
    x4=228
    y4=892

    follow_hiketop(x4, y4)

ppl_task4()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Now, I can repeat the upper code from ppl_task4 to ppl_task3 (kinda messed up on naming variables) , till i reach 30 ppls 
# it's like 4,1,2,3 scroll & then repeat ik should have used loop but whatever ...

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

# Additional tasks [ better to do some extra work :) ]

# Task 31

time.sleep(secs)

ppl_task3()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

#Scroll

time.sleep(secs)
scroll_hiketop()

# Task 32

time.sleep(secs)

ppl_task4()

time.sleep(secs)

follow_ig()

time.sleep(secs)

return_to_app()

print(color.BOLD)
print("[+] All tasks completed !!")
print()
print("[+] phew! , that was some hardwork ;)")
print()
