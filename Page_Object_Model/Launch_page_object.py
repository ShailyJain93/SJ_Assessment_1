from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select
from datetime import datetime, timedelta
import pytest
import time
from Locators import orange_hrm



class SJOrangeHRM:

    def __init__(self, driver):
        self.driver = driver

    def launch_the_app(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Application is launched Successfully")

        #Validate the URL
        get_url = self.driver.current_url 
        if get_url == url:
            print ("user navigated successfully")
        else:
            print ("User is not navigated properly")

        #Validate the Title
        get_driver = self.driver.title
        if get_driver == "OrangeHRM":
            print ("Title is displayed")

        else:
            print ("Title is not displaying")

        #Read Username
        Username_element = self.driver.find_element(By.XPATH, orange_hrm.Username_xpath()).text
        Username = Username_element.split(":")[-1].strip()

        #Read Password
        Password_element = self.driver.find_element(By.XPATH, orange_hrm.Password_xpath()).text
        Password = Password_element.split(":")[-1].strip()
        
        #Login
        self.driver.find_element(By.XPATH, orange_hrm.username_textbox()).send_keys(Username)
        self.driver.find_element(By.XPATH, orange_hrm.password_textbox()).send_keys(Password)
        self.driver.find_element(By.XPATH, orange_hrm.submit_button()).click()

        print("User Logged In Successfully")

    def update_info(self):

        #Click on My Info
        self.driver.find_element(By.XPATH, orange_hrm.my_info()).click()
        time.sleep(10)
        print ("User is on MyInfo page")

        #Update personal details (middle name)
        self.driver.find_element(By.XPATH, orange_hrm.middle_name()).send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        self.driver.find_element(By.XPATH, orange_hrm.middle_name()).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element(By.XPATH, orange_hrm.middle_name()).send_keys("Jain")
        time.sleep(5)
        self.driver.find_element(By.XPATH, orange_hrm.Save_PD()).click()

        print ("Details updated")

        #Logout
        self.driver.find_element(By.XPATH, orange_hrm.logout_1()).click()
        self.driver.find_element(By.XPATH, orange_hrm.logout_2()).click()
        time.sleep (5)
        print ("User logged out successfully")

        #Relogin
        Username_element = self.driver.find_element(By.XPATH, orange_hrm.Username_xpath()).text
        Username = Username_element.split(":")[-1].strip()

        Password_element = self.driver.find_element(By.XPATH, orange_hrm.Password_xpath()).text
        Password = Password_element.split(":")[-1].strip()
        
        self.driver.find_element(By.XPATH, orange_hrm.username_textbox()).send_keys(Username)
        self.driver.find_element(By.XPATH, orange_hrm.password_textbox()).send_keys(Password)
        self.driver.find_element(By.XPATH, orange_hrm.submit_button()).click()
        print("User Re-Logged In Successfully")

        #Validate Edited personal details.
        self.driver.find_element(By.XPATH, orange_hrm.my_info()).click()
        time.sleep(10)
        print ("User is on MyInfo page and validating the updated data")

        Current_details = self.driver.find_element(By.XPATH, orange_hrm.middle_name()).text
        if Current_details == "Jain":
            print ("Details are update")

        else:
            print ("Details is not updated")

    def Leave_flow(self):
        self.driver.find_element(By.XPATH, orange_hrm.Leave_button()).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, orange_hrm.Apply_button()).click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, orange_hrm.Leave_type_drop_down()).click()
        self.driver.find_element(By.XPATH, orange_hrm.Leave_type_CAN_F()).click()
        print("Selected Leave Type successfully")

        # Get today's date
        today = datetime.now().date()
        print("Clicked on leave type CAN successfully" + str(today))
        # Add one day
        next_day = today + timedelta(days=1)

        # Convert the next day to 'YYYY-MM-DD' format
        next_day_str = next_day.strftime("%Y-%m-%d")
        self.driver.find_element(By.XPATH, orange_hrm.fromDate()).send_keys(next_day_str)
        print("Entered date successfully" + str(next_day))
        time.sleep(1)
        
        self.driver.find_element(By.XPATH, orange_hrm.comment()).send_keys("Travelling")
        self.driver.find_element(By.XPATH, orange_hrm.applyButton()).click()

        print ("Leave Applied")


        #Go to "My Leave"
        self.driver.find_element(By.XPATH, orange_hrm.My_Leave()).click()
        time.sleep(2)

        #Cancel leave
        #self.driver.find_element(By.XPATH, orange_hrm.Canel_leave()).click()

    def Recruitment_flow(self):
        self.driver.find_element(By.XPATH, orange_hrm.Recruitment()).click()

        #Click on Vacancies
        self.driver.find_element(By.XPATH, orange_hrm.Vacancies()).click()

        #read the reocrd
        Total_record = self.driver.find_element(By.XPATH, orange_hrm.Total_record_count()).text
        Record_Count = Total_record.split("(")[1].split(")")[0]
        print (Record_Count)

        # Locate the Table Body
        table_body = self.driver.find_element(By.XPATH, orange_hrm.Table_xpath())

        # Locate all rows inside the table body
        rows = table_body.find_elements(By.XPATH, orange_hrm.Row_xpath())

        # Iterate through rows and capture column data
        table_data = []  # To store all table rows' data
        for row in rows:
        # Locate all cells (columns) within the row
            columns = row.find_elements(By.XPATH, orange_hrm.Column_xpath())
            row_data = [col.text.strip() for col in columns]  # Extract and clean text from each cell
            table_data.append(row_data)

        # Print the captured table data
        for idx, row in enumerate(table_data, start=1):
            print(f"Row {idx}: {row}")





