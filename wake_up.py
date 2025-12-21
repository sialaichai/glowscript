import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def wake_streamlit():
    options = Options()
    options.add_argument("--headless") # Run without a window
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    # Replace with your actual Streamlit URL
    url = "https://sialaichai-glowscript.streamlit.app/"
    
    print(f"Visiting {url}...")
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(10)
    
    try:
        # Streamlit's wake-up button usually has specific text or classes
        # This looks for the "Yes, get this app back up!" button
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            if "wake" in btn.text.lower() or "Yes, get this app back up!" in btn.text.lower():
                btn.click()
                print("Clicked the wake-up button!")
                time.sleep(5)
                break
    except Exception as e:
        print(f"App was already awake or button not found: {e}")
    
    driver.quit()

if __name__ == "__main__":
    wake_streamlit()
