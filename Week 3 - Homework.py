import requests
from bs4 import BeautifulSoup

# ==========================================
# Problem 1F: GitHub Repo Link
# ==========================================
print("1F. Link to GitHub Repo: https://github.com/ZainHaider14/DePaul-Cybersecurity-Automation-Test\n")


# ==========================================
# Problem 2: BeautifulSoup Web Scraper
# ==========================================
def get_courses(site_name):
    print("Fetching data from DePaul CDM...\n")
    headers = {'User-Agent': 'Mozilla/5.0'} 
    response = requests.get(site_name, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    courses = soup.find_all('section', class_='Schedule')
    
    if not courses:
        print("No courses found. The page structure might have changed.")
        return

    for course in courses:
        title_tag = course.find('h3')
        if title_tag:
            print(title_tag.text.strip())
        
        sections = course.find_all('section', class_='Schedule-Item')
        
        for section in sections:
            ul = section.find('ul', class_='schedule-item--part')
            if ul:
                list_items = ul.find_all('li')
                if len(list_items) >= 2:
                    time_str = list_items[0].text.strip()
                    loc_str = list_items[1].text.strip().replace('\n', ' ')
                    
                    print(f"    {time_str}")
                    print(f"    {loc_str}")
        print() 

url = 'https://my.cdm.depaul.edu/v2/Public/Schedule?Department=CSEC&CourseNumber=&Quarter=1&Year=2027'
print("Problem 2.2:")
get_courses(url)

# ==========================================
# Problem 3: Selenium Web Automation
# ==========================================
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("\nProblem 3: Selenium Screenshot Automation")

# Run silently in the background with server-safe arguments
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

try:
    print("Starting Chromium WebDriver...")
    driver = webdriver.Chrome(options=options)
    
    target_url = "https://www.wikipedia.org"
    print(f"Navigating to {target_url}...")
    driver.get(target_url)
    
    time.sleep(2)
    
    file_name = "wikipedia_screenshot.png"
    driver.save_screenshot(file_name)
    print(f"Success! Screenshot saved as: {file_name}")
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'driver' in locals():
        driver.quit()
