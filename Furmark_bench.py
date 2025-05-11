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

download_dir = "C:/Users/npulipat/Downloads/geeks3d_download"



# Set Chrome options
chrome_options = Options()

driver = webdriver.Chrome(options)

download_folder = r"C:\Users\npulipat\Downloads\New folder"


chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,  # specify the download folder
})

driver.get("https://geeks3d.com/dl/show/803")
time.sleep(3)

element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/main[1]/div[1]/p[1]/a[1]/h1[1]/b[1]")
element.click()

time.sleep(20)


#extracting file
# Path to your downloaded ZIP file
zip_file_path = "C:/Users/npulipat/Downloads/FurMark_2.8.0.0_win64.zip"

# Path where you want to extract the contents
extraction_path = "C:/Users/npulipat/Downloads/New folder"

# Extract the contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_path)

print(f"File extracted to: {extraction_path}")
print("file downloaded and installed successfully ")
driver.quit()

exe_path = r"C:\Users\npulipat\Downloads\New folder\FurMark_win64\FurMark_GUI.exe"

# Coordinates where you want to click
x = 1153
y = 251

# Call the function from run_click.py to open the application and click at the specified coordinates
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
exe_path = r"C:\Users\npulipat\Downloads\New folder\FurMark_win64\FurMark_GUI.exe"

# Coordinates where you want to click (you got these from the previous step)
x = 1153
y = 251

# Call the function to run the application and click at the given coordinates
run_application_and_click(exe_path, x, y)

# Directory where logs are saved
log_dir = r"C:\Users\npulipat\Downloads\New folder\FurMark_win64"

# Ensure the log directory exists
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# List files before running benchmark
existing_logs = set(os.listdir(log_dir))
# removing logs if already exists
for file in os.listdir(log_dir):
    if file.startswith("_furmark_log"):
        try:
            os.remove(os.path.join(log_dir, file))
            print(f"Deleted old log file: {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")

# Run FurMark for 60 seconds using CLI arguments
print("Starting FurMark benchmark...")

# Run FurMark for 60 seconds using CLI arguments
subprocess.Popen([
    exe_path,
    "/nogui",
    "/bench",
    "/width=1920",
    "/height=1080",
    "/time=60",
    "/log"
])

print(f"Benchmark started. Waiting 65 seconds... Logs are expected in: {log_dir}")
time.sleep(35)  # Wait a bit more than 60s to ensure benchmark and logging finish

# List files after benchmark
new_logs = set(os.listdir(log_dir)) - existing_logs

# Check if any new log file with '_furmark_log' has been created
log_files = [file for file in new_logs if file.startswith('_furmark_log')]

if log_files:
    print(f"✅ Log file(s) created: {', '.join(log_files)}")
else:
    print("❌ No new '_furmark_log' file found.")
    print(f"Log check location: {log_dir}")

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