import os
import subprocess
import time
import zipfile
import psutil
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# to keep the browser open below 2 lines are required
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)


# Set Chrome options calling above specifications
chrome_options = Options()

#calling chrome driver to open
driver = webdriver.Chrome(options)

download_folder = r"C:\Users\npulipat\Downloads\New folder"

#below line will must download file in the mentioned directory
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,  # specify the download folder
})


#after opening the browser below line will enter the URL in search
driver.get("https://geeks3d.com/dl/show/803")

#waiting to time to navigate the URL
time.sleep(3)

#after opening the URL navigating to download option and click on it
element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/main[1]/div[1]/p[1]/a[1]/h1[1]/b[1]")
element.click()

time.sleep(20)


#extracting file
# Path to your downloaded ZIP file
zip_file_path = "C:/Users/npulipat/Downloads/FurMark_2.8.0.0_win64.zip"

# Path where you want to extract the contents
extraction_path = "C:/Users/npulipat/Downloads/New folder"

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_path)

print(f"File extracted to: {extraction_path}")
print("file downloaded and installed successfully ")
driver.quit()

exe_path = r"C:\Users\npulipat\Downloads\New folder\FurMark_win64\FurMark_GUI.exe"

#below function is to run the benchmark
def run_application_and_click(exe_path, x, y):
    # Run the .exe file (open the application)
    subprocess.Popen(exe_path, shell=True)

    # Wait for the application to open
    print("Waiting for the application to open...")
    time.sleep(5)  # Wait for 5 seconds (you can adjust this time)

    # Click at the coordinates you provided
    print(f"Clicking at coordinates: ({x}, {y})")
    pyautogui.click(x, y)


# Path to the .exe file you want to run
#exe_path = r"C:\Users\npulipat\Downloads\New folder\FurMark_win64\FurMark_GUI.exe"
exe=r"C:\Users\npulipat\Documents\Batch_script\file\FurMark_win64\FurMark_GUI.exe"

# Coordinates where you want to click (you got these from the previous step)
x = 1153
y = 251

# Call the function to run the application and click at the given coordinates
run_application_and_click(exe, x, y)

# Run FurMark for 60 seconds using CLI arguments
print("Starting FurMark benchmark...")


time.sleep(35)

#closing the all benchmark related tabs
print("Trying to close FurMark window...")
def kill_furmark():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if "FurMark" in proc.info['name']:
                print(f"❗ Terminating process: {proc.info['name']} (PID: {proc.info['pid']})")
                proc.terminate()
                proc.wait(timeout=5)
                print("✅ FurMark terminated.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
kill_furmark()

print("FUR MARK RAN SUCCESSFULLY")