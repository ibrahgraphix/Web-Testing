from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

#Error handling code
def safe_click(driver, by, value, description="", wait_time=5):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
        element.click()
        time.sleep(wait_time)
    except Exception as e:
        print(f"[ERROR] Failed to click {description or value}: {e}")

def safe_type(driver, by, value, text, description="", wait_time=5):
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)
        time.sleep(wait_time)
    except Exception as e:
        print(f"[ERROR] Failed to type in {description or value}: {e}")

def safe_select_by_text(driver, by, value, visible_text, description="", wait_time=5):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))
        select = Select(element)
        select.select_by_visible_text(visible_text)
        time.sleep(wait_time)
    except Exception as e:
        print(f"[ERROR] Failed to select {description or value}: {e}")
        

#Main Code start here..

# Set up download directory
download_dir = os.path.abspath("downloads")  # Create 'downloads' folder in your project

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": download_dir,
    "plugins.always_open_pdf_externally": True,  # Auto-download PDFs
    "download.prompt_for_download": False,
    "profile.default_content_settings.popups": 0,
})

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://cybersmart.wnscaresfoundation.org/Students")

#Locaters
country_list= driver.find_element(By.XPATH, "//option[@value='1']").click()
time.sleep(5)
language_list= driver.find_element(By.XPATH, "//option[@value='English']").click()
time.sleep(5)
next_button= driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

#Text area
wait = WebDriverWait(driver, 10)
textarea = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='Name']")))
textarea.clear()
textarea.send_keys("Shlok")
time.sleep(5)

#Grade/ Class dropdown
class_dropdown= driver.find_element(By.ID, "SelectedClassName")
select= Select(class_dropdown)
select.select_by_visible_text("8 and above")
time.sleep(5)

#State dropdown
state_dropdown= driver.find_element(By.CSS_SELECTOR, "option[value='Maharashtra']").click()
time.sleep(5)

#Channel Partner
channel_dropdown= driver.find_element(By.CSS_SELECTOR, "option[value='BVF']").click()
time.sleep(5)
next= driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(5)

#Enter
take_course= driver.find_element(By.XPATH, "//a[@href='/Students/JourneyOverview']").click()
time.sleep(5)

#Course 
course= driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

#Video
wait = WebDriverWait(driver, 15)
video = wait.until(EC.presence_of_element_located((By.XPATH, "//video[@class='video shadow']")))
driver.execute_script("arguments[0].play();", video)
time.sleep(130)

#Take quiz
wait = WebDriverWait(driver, 20)
take_quiz_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Take Quiz']")))
take_quiz_button.click()
time.sleep(2)


# Questions
q1= driver.find_element(By.LINK_TEXT, "True")
q1.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click() 
time.sleep(3)

q2= driver.find_element(By.XPATH, "//section[@class='main-conrainer scrolly']//li[1]//a[1]") 
q2.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

q3= driver.find_element(By.LINK_TEXT, "False")
q3.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

q4= driver.find_element(By.XPATH, "//section[@class='main-conrainer scrolly']//li[2]//a[1]")
q4.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

q5= driver.find_element(By.XPATH, "//section[@class='main-conrainer scrolly']//li[3]//a[1]")
q5.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

#Cyber Bullying Section
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

#Video
wait = WebDriverWait(driver, 15)
video = wait.until(EC.presence_of_element_located((By.XPATH, "//video[@class='video shadow']")))
driver.execute_script("arguments[0].play();", video)
time.sleep(130)

#Take quiz
wait = WebDriverWait(driver, 20)
take_quiz_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Take Quiz']")))
take_quiz_button.click()
time.sleep(2)

# Questions
qst1= driver.find_element(By.LINK_TEXT, "True")
qst1.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click() 
time.sleep(3)

qst2= driver.find_element(By.XPATH, "//section[@class='main-conrainer scrolly']//li[2]//a[1]") 
qst2.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

qst3= driver.find_element(By.LINK_TEXT, "All of the Above")
qst3.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

qst4= driver.find_element(By.XPATH, "//span[normalize-space()='Report the post as abuse']")
qst4.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

qst5= driver.find_element(By.XPATH, "//section[@class='main-conrainer scrolly']//li[1]//a[1]")
qst5.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

#Financial Security Section
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

#Video
wait = WebDriverWait(driver, 15)
video = wait.until(EC.presence_of_element_located((By.XPATH, "//video[@class='video shadow']")))
driver.execute_script("arguments[0].play();", video)
time.sleep(98)

#Take quiz
wait = WebDriverWait(driver, 20)
take_quiz_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Take Quiz']")))
take_quiz_button.click()
time.sleep(2)

# Questions
Qst1= driver.find_element(By.LINK_TEXT, "False")
Qst1.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click() 
time.sleep(3)

Qst2= driver.find_element(By.XPATH, "//section[@class='main-conrainer scrolly']//li[1]//a[1]") 
Qst2.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

Qst3= driver.find_element(By.LINK_TEXT, "False")
Qst3.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

Qst4= driver.find_element(By.XPATH, "//span[normalize-space()='False']")
Qst4.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

Qst5= driver.find_element(By.XPATH, "//span[normalize-space()='Parents']")
Qst5.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)


# Public Internet Section
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

#Video
wait = WebDriverWait(driver, 15)
video = wait.until(EC.presence_of_element_located((By.XPATH, "//video[@class='video shadow']")))
driver.execute_script("arguments[0].play();", video)
time.sleep(60)

#Take quiz
wait = WebDriverWait(driver, 20)
take_quiz_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Take Quiz']")))
take_quiz_button.click()
time.sleep(2)

# Questions
Qst1= driver.find_element(By.LINK_TEXT, "Both")
Qst1.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click() 
time.sleep(3)

Qst2= driver.find_element(By.XPATH, "//section[@class='main-conrainer scrolly']//li[1]//a[1]") 
Qst2.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

Qst3= driver.find_element(By.LINK_TEXT, "True")
Qst3.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

Qst4= driver.find_element(By.XPATH, "//section[@class='main-conrainer scrolly']//li[2]//a[1]")
Qst4.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

Qst5= driver.find_element(By.XPATH, "//span[normalize-space()='False']")
Qst5.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

# Cybergrooming Section
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

#Video
wait = WebDriverWait(driver, 15)
video = wait.until(EC.presence_of_element_located((By.XPATH, "//video[@class='video shadow']")))
driver.execute_script("arguments[0].play();", video)
time.sleep(110)

#Take quiz
wait = WebDriverWait(driver, 20)
take_quiz_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Take Quiz']")))
take_quiz_button.click()
time.sleep(2)

# Questions
Q1= driver.find_element(By.LINK_TEXT, "True")
Q1.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click() 
time.sleep(3)

Q2= driver.find_element(By.XPATH, "//section[@class='main-conrainer scrolly']//li[1]//a[1]") 
Q2.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

Q3= driver.find_element(By.LINK_TEXT, "False")
Q3.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

Q4= driver.find_element(By.XPATH, "//span[normalize-space()='All of the above']")
Q4.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
time.sleep(3)

Q5= driver.find_element(By.XPATH, "//span[normalize-space()='Inform parents/elders']")
Q5.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

loader = WebDriverWait(driver, 20)
take_quiz_button = loader.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']")))
take_quiz_button.click()
time.sleep(2)

checker = WebDriverWait(driver, 20)
take_quiz_button = checker.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Download']")))
take_quiz_button.click()
time.sleep(2)

try:
    pdf_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, ".pdf")]'))
    )
    pdf_link.click()
    print("✅ PDF link clicked successfully.")
except:
    print("⚠️ PDF link not found or not clickable.")

