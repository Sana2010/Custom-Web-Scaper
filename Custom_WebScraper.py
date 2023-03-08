import csv, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/ajithvijayaraj/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

ORIGIN = "BLR"
DESTINATION = "GAU"
start_date = "31/07/2022"
fields = ['Date', 'Price(INR)']
URL = "https://www.makemytrip.com/flight/search?tripType=O&itinerary=" + ORIGIN + "-" + DESTINATION + "-" + start_date + "&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1653908247075&forwardFlowRequired=true&mpo=&semType=&intl=false"
data_list = []
rows = []

driver.get(URL)
time.sleep(5)

close_popup = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]/div[2]/div/span")
close_popup.click()


next_button = driver.find_element(by=By.CLASS_NAME, value="glider-next")
data = driver.find_elements(by=By.CLASS_NAME, value="weeklyFareItems")
for i in range(20):
    time.sleep(2)
    next_button.click()
    data = driver.find_elements(by=By.CLASS_NAME, value="weeklyFareItems")
    data_list.append([d.text for d in data if d.text != ''])

for i in range(len(data_list)):
    for j in range(len(data_list[i])):
        rows.append([data_list[i][j][5:11].replace("\n", ""), data_list[i][j][-5:]])

final_row = [rows[i] for i in range(len(rows)) if ',' in rows[i][1]]

with open("flight_prices.csv", 'w') as file:
    file_writer = csv.writer(file)
    file_writer.writerow(fields)
    file_writer.writerows(final_row)
