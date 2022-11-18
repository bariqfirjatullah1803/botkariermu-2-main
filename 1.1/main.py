from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

print("01. XD")
print("02. AutoCAD")
print("03. Website")
print("04. AEANIMATOR")
print("05. AEMultimedia")
print("06. AdobeFlash")
print("07. 3DSMax")
print("08. Photoshop")
lang = input("Choose : ")

match lang:
    case "1":
        linkpelatihan = "https://admin.sekolah.mu/admin/program/student/20130"
    case "2":
        linkpelatihan = "https://admin.sekolah.mu/admin/program/student/20429"
    case "3":
        linkpelatihan = "https://admin.sekolah.mu/admin/program/student/26553"
    case "4":
        linkpelatihan = "https://admin.sekolah.mu/admin/program/student/27310"
    case "5":
        linkpelatihan = "https://admin.sekolah.mu/admin/program/student/26617"
    case "6":
        linkpelatihan = "https://admin.sekolah.mu/admin/program/student/27605"
    case "7":
        linkpelatihan = "https://admin.sekolah.mu/admin/program/student/26480"
    case "8":
        linkpelatihan = "https://admin.sekolah.mu/admin/program/student/26482"
    case _:
        print("Pelatihan tidak ada")

chrome_options = Options()
chrome_prefs = {
    "profile.default_content_setting_values": {
        "images": 2,
        "javascript": 1
    }
}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_options.headless = False
chrome_options.add_argument("--log-level=3")

url_login = "https://admin.sekolah.mu/login"
email_login = "101digimind@gmail.com"
password_login = "Mitra.Karisma22"

xpath_input = '//*[@id="__BVID__57"]'
xpath_tanggal = '//*[@id="__BVID__61"]/tbody/tr/td[1]/div'
xpath_nama = '//*[@id="__BVID__61"]/tbody/tr/td[2]/div'
xpath_persen = '//*[@id="__BVID__61"]/tbody/tr/td[6]/div'


driver = webdriver.Chrome(executable_path=r'driver\chromedriver.exe',chrome_options=chrome_options)
driver.get(url_login)
print("load login")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@type='text']"))
)
e = driver.find_element(By.XPATH,"//input[@type='text']")
e.send_keys(email_login)
print("input email")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@type='text']"))
)
e = driver.find_element(By.XPATH,"//input[@type='password']")
e.send_keys(password_login)
print("input password")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID,"login-button"))
)
e = driver.find_element(By.ID,"login-button")
e.click()
print("button klik")
sleep(5)
# sleep(20)
driver.get(linkpelatihan)
file1 = open('email.txt', 'r')
Lines = file1.readlines()
sleep(5)

count = 0
for line in Lines:
    count += 1
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH,xpath_input))
    )
    print(line.strip())
    e = driver.find_element(By.XPATH,xpath_input)
    e.send_keys(line.strip())
    sleep(3)
    try:
        tanggal = driver.find_element(By.XPATH,xpath_tanggal).get_attribute("innerText")
        nama = driver.find_element(By.XPATH,xpath_nama).get_attribute("innerText")
        partisipasi = driver.find_element(By.XPATH,xpath_persen).get_attribute("innerText")
        with open('result.txt', 'a') as f:
            f.write("Valid")
            f.write('\t')
            f.write(line.strip())
            f.write('\t')
            f.write(tanggal)
            f.write('\t')
            f.write(nama)
            f.write('\t')
            f.write(partisipasi)
            f.write('\n')
        e.clear()
    except:
        with open('result.txt', 'a') as f:
            f.write("Invalid")
            f.write('\t')
            f.write(line.strip())
            f.write('\n')
            e.clear()




