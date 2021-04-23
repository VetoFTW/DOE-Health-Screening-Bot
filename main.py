import time
import userDB
from selenium import webdriver
# BUG Does Not Select Correct Schoool, But who cares, it does not show anything on the screening about which school
# List of variables needed to complete form

myDateTime = time.localtime() 
timeString = time.strftime("%H:%M:%S", myDateTime)

try:
    while True:
        myDateTime = time.localtime() 
        timeString = time.strftime("%H:%M:%S", myDateTime)

        if timeString == "00:00:00":
            time.sleep(1)

            for user in userDB.users:
                userFirstName = user[0]
                userLastName = user[1]
                userEmailAdd = user[2]
                userSchoolOrBuilding = "aviation"

                healthScreanerURL = "https://healthscreening.schools.nyc/?type=G"

                driver = webdriver.Firefox()
                driver.get(healthScreanerURL)

                # Completing The Form
                # The DOE Health Screener only requires you to enter your name, email, and whether or not you are a student, staff, or visitor.
                firstNameElement = driver.find_element_by_id("guest_first_name")
                firstNameElement.send_keys(userFirstName)

                lastNameElement = driver.find_element_by_id("guest_last_name")
                lastNameElement.send_keys(userLastName)

                emailElement = driver.find_element_by_id("guest_email")
                emailElement.send_keys(userEmailAdd)

                imAstudentElement = driver.find_element_by_css_selector("label[for=guest_isStudent]").click()

                driver.find_element_by_css_selector("span .k-input").click()
                schoolSelectorElement = driver.find_element_by_css_selector(".k-list-filter .k-textbox")
                schoolSelectorElement.send_keys(userSchoolOrBuilding)

                clickOnSchool = driver.find_element_by_css_selector("#Location_listbox .k-item").click()

                # Submit the Form
                fillOutDailyScreeningButton = driver.find_element_by_css_selector("#btnDailyScreeningSubmit button").click()

                # Complete the Questionaire
                for i in range(1, 6):
                    driver.find_element_by_css_selector("label[for=q{}no".format(i)).click()

                # Submit the Questionaire
                SubmitScreeningButton = driver.find_element_by_css_selector("#questions_layout button").click()

                # Close the Driver
                driver.close()

                # Confirmation In Console
                print("Filled out Health Screener for:", user[0], user[1], "to", user[2])
except KeyboardInterrupt:
    pass
