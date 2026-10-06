import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("1F. Link to GitHub Repo: https://github.com/ZainHaider14/DePaul-Cybersecurity-Automation-Test")

def hello_world():
    return "Hello World!"

def get_courses(site_name):
    r = requests.get(site_name)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    schedule = soup.find('section', class_='Schedule')
    if schedule:
        for course in schedule.find_all('h3'):
            print(course.text.strip())
            details = course.find_next_sibling('ul')
            if details:
                for li in details.find_all('li'):
                    print("   ", li.text.strip())
            print()

print("\nProblem 2.2:")
get_courses('https://my.cdm.depaul.edu/v2/Public/Schedule?Department=CSEC&CourseNumber=&Quarter=1&Year=2027')

def capture(url):
    top_ten = []
    r = requests.get(url)
    
    # parse the text file for the first 10 domains
    for line in r.text.strip().split('\n')[:10]:
        domain = line.split(',')[-1].strip()
        top_ten.append(domain)
        
    # setup headless chromium for ubuntu server
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    
    for site in top_ten:
        try:
            driver.get(f"http://{site}")
            time.sleep(2)
            
            # format the filename to just the name (e.g. google.png)
            filename = f"{site.split('.')[0]}.png"
            driver.save_screenshot(filename)
        except Exception as e:
            print(f"Error capturing {site}: {e}")
            
    driver.quit()
    return top_ten

url = 'https://raw.githubusercontent.com/bensooter/URLchecker/master/top-1000-websites.txt'
print(f"\nProblem 3: {capture(url)}")
