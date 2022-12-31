import random
import time
from selenium import webdriver
# from Venom import generate_random_name, generate_random_email, generate_message

# RickRoll
def generate_message():
    # Rick Astley's "Never Gonna Give You Up"
    lyrics = "We're no strangers to love\nYou know the rules and so do I\nA full commitment's what I'm thinking of\nYou wouldn't get this from any other guy\nI just wanna tell you how I'm feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n"
    return lyrics 

print(generate_message())

# Actual bot to automate form submissions
class Bot():
    def __init__(self):
        # Load chromedriver
        self.driver = webdriver.Chrome()
        # Loading browser and navigate to the desired website
        
    def open_site(self):
        self.driver.get("http://www.abc.xyz/")

        time.sleep(1)

        cont = self.driver.find_element("xpath", "/full-xpath")
        cont.click()
        time.sleep(.6)

    # Insert Stinger
    def inject_venom(self):
        name_field = self.driver.find_element("xpath", "/full-xpath")
        email_field = self.driver.find_element("xpath", "/full-xpath")
        msg_field = self.driver.find_element("xpath", "/full-xpath")
    # Inject Venom
    
        with open("usernames.txt", "r") as f:
            # Determine the total number of lines in the file
            num_lines = sum(1 for line in f)
            # Start at beginning of the file
            f.seek(0)
            # Generate a random line number
            rand_line_num = random.randint(0, num_lines - 1)
            # Go to the specified line number and read the line
            for _ in range(rand_line_num):
                f.readline()
            random_line = f.readline().rstrip()
    
        # Creating random usernames

        def generate_random_name():
            # List of possible usernames
            usernames = [random_line]

            # Random choice from username list
            return random.choice(usernames)

        print(generate_random_name())
        
        def generate_random_email():
            # List of possible domain names
            domain_names = ["gmail.com", "yahoo.com", "outlook.com",
                            "aol.com", "hotmail.com", "protonmail.com", "icloud.com"]

            # Create email username from random_line usernames list
            username = (random_line)
            # Adding realism to the email username with digits
            # Listing the characters for the username
            user_char_list = list(username)
            # Generate a random number between 0 and 999
            rand_nums = str(random.randint(0, 999))
            # Adding the random num to the end of the user char list
            user_char_list.insert(len(username), rand_nums)
            result = ''.join(user_char_list)
            print(True)
        # for random letters\ username = ''.join(random.choices(string.ascii_lowercase, k=8))
            # Return a random email address in the form "username##@domain.com"
            return f"{result}@{random.choice(domain_names)}"


        print(generate_random_email())

    
        name_field.send_keys(generate_random_name())
        time.sleep(0.25)
        email_field.send_keys(generate_random_email())
        time.sleep(0.25)
        msg_field.send_keys(generate_message())
        time.sleep(0.25)
    # Submit
        send_button = self.driver.find_element("xpath", "/full-xpath")
        send_button.click()
        time.sleep(0.25)
    # # Back to original site (Useful if site ):
    #     back_button = self.driver.find_element("xpath", "/full-xpath")
    #     back_button.click()
        
for i in range(1000):
    bot = Bot()
    bot.open_site()
    bot.inject_venom()
    time.sleep(0.25)
    bot.driver.quit()
    i += 1
    print(i)
    
