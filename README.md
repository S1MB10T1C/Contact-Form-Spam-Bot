### This program is a contact form spam bot that automatically generates a random username and email,
### then inputs the lyrics to Rick Astley's "Never Gonna Give You Up".
### The bot can be easily repurposed for something more pragmatic, like autonomous email responder bot, autonomous text reply bot, autonomous social media manager, and much more, with just a bit of effort.
    This program takes advantage of the selenium webscraping tool, Google Chrome, and Python. This program will work with any website
    that has a simple UI that allows you to click a contact button and redirects you to a form on the same page.
    If the website redirects you to another window, you can use the "switch_to.window" method.
    
##### Here's how: (scroll down to "how to use" if the simple version works for you)

      First, find the current window handle:
main_window_handle = driver.main_window_handle

      Click the button that opens a new window:
button = driver.find_element("xpath", "/full-xpath")
button.click()

      Let the window load:
time.sleep(1.5)

      Get the handles of all open windows:
window_handles = driver.window_handles

      Find the handle of the new window:
new_window_handle = None
for handle in window_handles:
    if handle != current_window_handle:
        new_window_handle = handle
        break
         
     Switch to the new window:
driver.switch_to.window(new_window_handle)
##
### ⚠ USE AT YOUR OWN RISK. 
### ⚠ IT IS NOT RECOMMENDED TO USE THIS ON OTHERS WITHOUT THEIR PERMISSION. 
### ⚠ YOU ARE RESPONSIBLE FOR YOUR OWN ACTIONS WHEN USING THIS program.

# How to use:

1. Ensure you have the proper packages installed:

    1.1: Ensure you have installed selenium
  
    1.2: Ensure you have installed the correct version of chromedriver for your Chrome browser from the official webpage:
       https://chromedriver.storage.googleapis.com/index.html?path=108.0.5359.71%2F
       
        1.2.1: Follow the instructions carefully and ensure chromedriver is contained within $PATH. If you are having issues,
             you may have to directly specify the chromedriver location, i.e. " self.driver = webdriver.Chrome("C:/chromedriver") "
##
2.  Choose the desired website for the bot to target:
    
    2.1: Find the line of code that says, " self.driver.get('insert_website') " and input your target website as "http(s)://(www.)abc.xyz/"
##
3. Define the steps for the robot to take for each instance of click, find, etc.:

   i.e.
   Instructing the bot to click the contact button:
   
        contact_button = self.driver.find_element("xpath", "/full-xpath")
        contact_button.click()
        time.sleep(.6)
        
    repeat the same process for the form submit/send button

    3.1: You will extract the full-xpath from the website by using the inspect element feature and copying the full-xpath from the browser

    3.2: This will need to be done for each field which is clicked, or selected for typing input:
    
    i.e. Selecting a text field for typing a username:
    
          name_field = self.driver.find_element("xpath", "/full-xpath")
##
4. This program is set to loop for i in range("insert value here"): Define this range to how many times you want to fill out the form
  
