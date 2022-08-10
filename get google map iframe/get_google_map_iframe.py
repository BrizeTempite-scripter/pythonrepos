import libraries_downloader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import os
import time


def print_percent(args):
  os.system("cls")
  print(f"%{args} complate")




os.chdir(os.path.dirname(__file__))
dicter={
  "run":False,
  "value":"anitkabir",
  "hiden":True
}

data = {}
with open(os.getcwd()+"/data/data.json", "w") as file:
  json.dump(dicter,file)
print("waiting")
while True:
  with open(os.getcwd()+"/data/data.json", "r") as file:
    try:
      data=json.loads(file.read())
      if(data["run"]==True):
        break
    except:
      pass

    
  time.sleep(1)
valudation=data["value"]
print("runing")
start=time.time()
if(data["hiden"]==True):
  options = Options()
  options.add_argument("--headless")
  driver = webdriver.Chrome("chromedriver", options=options)

else:
  driver=webdriver.Chrome()

print_percent("10")
driver.get("https://www.google.com/maps")
driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]").send_keys(valudation)

print_percent("20")
driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button").click()
time.sleep(1)
print_percent("30")
driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[1]/button").click()
time.sleep(1)
print_percent("40")
driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[25]/div/div[2]/ul/div[5]/li[1]/button").click()
time.sleep(2)
print_percent("70")
driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/button[2]").click()
time.sleep(1)

valuer= driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div[3]/div/div/div/div[3]/div[1]/input").get_attribute('value')

print_percent("100")
print(valuer)
with open(os.getcwd()+ "/data/iframe.txt", "w") as file:
  file.write(valuer)
driver.close()
print("last time :"+ str(time.time()-start)+" sec")