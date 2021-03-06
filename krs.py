from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import tkinter
import time

def KRSAN(username, password, kode_matkul_kelas = {}):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://simaster.ugm.ac.id/ugmfw/signin_simaster/signin_proses")
    
    user = driver.find_element_by_id("username")
    user.clear()
    user.send_keys(username)
    
    passw = driver.find_element_by_id("password")
    passw.clear()
    passw.send_keys(password)

    driver.find_element_by_name("submit").click()

    driver.get("https://simaster.ugm.ac.id/sia_krs/input_krs/")
    driver.find_element_by_class_name("btn-warning").click()

    time.sleep(2)
    for matkul in kode_matkul_kelas:
        if kode_matkul_kelas[matkul].upper() == 'A':
            kelas = 1
        elif kode_matkul_kelas[matkul].upper() == 'B':
            kelas = 2
        elif kode_matkul_kelas[matkul].upper() == 'C':
            kelas = 3
        matkul.strip()
        driver.find_element_by_xpath(f'//*[@id="1_{matkul}"]/table/tbody/tr[{kelas}]/td[1]/input').click()