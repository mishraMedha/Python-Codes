#Small instalogin funtion to autmate the Instagram Login
def instalogin():
    from selenium import webdriver

    driver= webdriver.Chrome(executable_path ='chromedriver_win32/chromedriver')

    driver.implicitly_wait(10)
    driver.get("https://www.google.co.in")
    driver.maximize_window()
    goggle=driver.find_element_by_name("q")
    goggle.click()
    goggle.clear()
    goggle.send_keys("insta login")
    goggle.submit()
    insta_page=driver.find_element_by_xpath("//div[@class='TbwUpd NJjxre']")
    insta_page.click()
    username=driver.find_element_by_name("username")
    username.click()
    username.clear()
    username.send_keys('mismedha07@gmail.com')
    password=driver.find_element_by_name("password")
    password.click()
    password.clear()
    password.send_keys('Medha@0722')
    signin=driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")  #To find the login button
    signin.click()
    home=driver.find_element_by_class_name('cq2ai')  # Home element
    home.click()
    alert=driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    alert.click()
    while(True):
        pass

instalogin()
