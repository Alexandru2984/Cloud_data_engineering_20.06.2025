from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurare browser
browser = webdriver.Chrome()
browser.get("https://icanhazdadjoke.com/")

# Accept cookie dacă apare
try:
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fc-cta-consent"))
    ).click()
except:
    pass  # dacă nu apare, trece mai departe

# Set pentru glume unice
seen_jokes = set()

# Funcție principală
def get_joke():
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "subtitle"))
    )
    joke = browser.find_element(By.CLASS_NAME, "subtitle").text.strip()
    return joke

# Scriere infinită în fișier
with open("jokes_v2.txt", "w", encoding="utf-8") as f:
    for _ in range(10):
        joke = get_joke()

        # Sari peste placeholder sau glume deja văzute
        if not joke or joke.lower() == "icanhazdadjoke" or joke in seen_jokes:
            browser.refresh()
            time.sleep(1)
            continue

        # Scrie în fișier și în consolă
        seen_jokes.add(joke)
        f.write(joke + "\n")
        f.flush()  # asigură salvarea imediată
        print("😄", joke)

        browser.refresh()
        time.sleep(2)

input()
browser.close()