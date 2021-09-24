import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
import datetime
from time import sleep
import pyautogui

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:/Users/YOUR_USERNAME/AppData/Local/Google/Chrome/User Data") #Get profile from Chrome (To know wher is your profile data go read the README file)
options.add_argument(r'--profile-directory=Profile 3') #Set profile for ChromeDrive (Replace with yours, in this case "Profile 3")
web = webdriver.Chrome(executable_path=r'C:/Users/YOUR_USERNAME/AppData/Local/Programs/Python/Python39/Lib/site-packages/chromedriver_py/chromedriver_win32.exe', chrome_options=options) (Loading options)
web.get("https://opensea.io/asset/create") #This open opensea.io on your browser (Sign In in your wallet when you hear the 3 bells, if you face some troubles, just refresh the page, nothing bad is gonna happen, and press "Sign In" again, that should work.)

time.sleep(5) #Just relaxing a while, you would thank me later, when things become heavier

web.maximize_window() #Maximizing window, to avoid troubles

web.find_element_by_link_text("Create").click() #Make sure we are in the correct window


#This are the three bells that say, GO SIGN YOUR WALLET BEAUTY!
print('\a');print("##### This was the first Bell #####")
time.sleep(1)
print('\a')
print("##### This was the second Bell #####")
time.sleep(1)
print('\a')
print("##### This was the third Bell #####")
time.sleep(1)
print('\n')
print("#################################################################" + "\n" + "# YOU HAVE 30 SECONDS TO SIGN IN YOUR WALLET BEAUTIFUL PERSON #" + "\n" + "#################################################################")

#Python will rest while you manually Sign in your Metamask or other wallet (Why are you like that? It is manual for security, it is preferable to log in once manually, and eventually automatically upload the NFT's while still are you signed.)
time.sleep(30)
print('\a') #Im just a line break, why are you starring at me?
print("##### Hope you're ready, cause we gonna begin #####")
time.sleep(1)

def goUpOpenSea(): #I'm the pure uploader to make the loop(It is likely that I will stumble when uploading your NFTs after some time, you know, the page was ticked a little while it was refreshing and my sleep function did not perform enough, and you will have to start again manually. But what can I tell you, nobody is perfect.)
    while True:
        time.sleep(6) 
        pyautogui.press("esc") #This make that the confirmation upload window was gone, to star over. You may ask, why you dont put it on the final of the function? Well smart boy, today, the smartboy its me, give me a break. 

        web.find_element_by_link_text("Create").click() #I click on create tab, i think its time to you to read the function, or i have to comment all, JESUS!

        web.find_element_by_id("media").send_keys("C:/NFTS/YOUR_NFT.png) #Put here the path of your NFT, you can put whatever you want, except you singing, Please dont do that to people!
                                                  
        web.find_element_by_id("name").send_keys("NFT Example Item") #Here goes the name of your NFT
                                                  
        web.find_element_by_id("external_link").send_keys("unirvana.live/nft") #Here goes the external link of your collectibles. (Replace unirvana.live with your link.)

        web.find_element_by_id("description").send_keys("Hello, im the descrption of your NFT") #Some description here.

        print("##### Selecting Collection section #####");print('\n')

        pyautogui.press("tab") #This first TAB will navegate to the collection section
        pyautogui.press("tab") #This second TAB will select the first collection, sorry boy, if you have more than one collection, you should copy and paste this line the times you need.
        pyautogui.press("enter") #This will confirm your selection.

        time.sleep(3)

        print("##### Active content only for owner section #####");print('\n')

        pyautogui.press("tab") #It is not necesary to explain that now im navigatng to the section i need, but here I am doin it again.
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")

        pyautogui.press("tab")
        pyautogui.write("Hello, im the special content that only the owners will see")

        print("##### PRESSING CREATE; SO EXCITED! #####");print('\n')

        pyautogui.press("tab") #Navigating to the CREATE button.
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")

        time.sleep(10) #You think 10 second its too much? change it, owner of the quantum computer!

        print("##### Now we gonnna close this window #####");print('\n')

        pyautogui.press("esc")

        time.sleep(5)

        pyautogui.press("esc") #Too much escapes? I wanna make sure that works, just leave me alone. 
        pyautogui.press("esc") #(0x87C35820fe988e73c54f71fB69da61Ac05474d26) Oh look! a ETH wallet address, you should send some.
        pyautogui.press("esc")
        pyautogui.press("esc")

        print("##### Ok, lets star over. #####");print('\n')
        time.sleep(1)
                                                  
goUpOpenSea() #This should do the loop.
