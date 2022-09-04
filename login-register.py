from cgitb import text
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


#TESTING REGISTRASI
class TestRegisterFail(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #Registrasi menggunakan email yang belum terdaftar
    def test_a_success_register(self):
        #steps
        browser = self.browser
        browser.get("https://automationpractice.com/")
        time.sleep(5)
        browser.find_element(By.CLASS_NAME,"login").click()
        time.sleep(3)
        browser.find_element(By.ID,"email_create").send_keys("indrayaza8@gmail.com") #harus menggunakan email baru
        time.sleep(1)
        browser.find_element(By.NAME,"SubmitCreate").click()
        time.sleep(3)
        #Personal Information
        browser.find_element(By.CSS_SELECTOR,"input#id_gender1").click()
        time.sleep(1)
        browser.find_element(By.ID,"customer_firstname").send_keys("Indra")
        time.sleep(1)
        browser.find_element(By.ID, "customer_lastname").send_keys("Yasa")
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[5]/input").send_keys("123456789")
        time.sleep(1)
        browser.find_element(By.ID, "days").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[1]/div/select/option[23]").click()
        time.sleep(1)
        browser.find_element(By.ID, "months").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[2]/div/select/option[8]").click()
        time.sleep(1)
        browser.find_element(By.ID, "years").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[3]/div/select/option[25]").click()
        time.sleep(1)
        #Your Address
        browser.find_element(By.ID, "address1").send_keys("Denpasar Street")
        time.sleep(1)
        browser.find_element(By.ID, "city").send_keys("Denpasar")
        time.sleep(1)
        browser.find_element(By.ID, "id_country").click()
        time.sleep(1)
        browser.find_element(By.ID, "id_state").click()
        time.sleep(1)
        browser.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/form/div[2]/p[7]/div/select/option[12]").click()
        time.sleep(1)
        browser.find_element(By.NAME, "postcode").send_keys("80235")
        time.sleep(1)
        browser.find_element(By.NAME, "phone_mobile").send_keys("08888585")
        time.sleep(1)
        browser.find_element(By.NAME, "alias").clear()
        time.sleep(1)
        browser.find_element(By.NAME, "alias").send_keys("Denpasar, 80235")
        time.sleep(1)
        browser.find_element(By.NAME, "submitAccount").click()
        time.sleep(1)
        
        text_atas = browser.find_element(By.ID, "center_column").text
        text_bawah = browser.find_element(By.CLASS_NAME, "info_account").text

        self.assertEqual(text_atas, 'My Account')
        self.assertIn("Welcome", text_bawah)

    #Registrasi menggunakan email yang sudah terdaftar
    def test_a_failed_register_using_email_registered(self):
        #steps
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email_create").send_keys("indrayaza8@gmail.com")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitCreate").click()
        time.sleep(5)

        #validation
        text_registered = browser.find_element(By.ID, "create_account_error").text

        self.assertIn('registered', text_registered)
    
    
    #Registrasi menggunakan email dengan format salah
    def test_b_failed_format_email_register(self):
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email_create").send_keys("indrayasa")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitCreate").click()
        time.sleep(5)

        text_invalid_email = browser.find_element(By.CSS_SELECTOR, "div#create_account_error.alert.alert-danger").text
        
        self.assertIn("Invalid email", text_invalid_email)
    
    def tearDown(self):
        self.browser.close()

#TESTING LOGIN
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):#Login menggunakan email dan password benar
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email").send_keys("indrayaza8@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID, "passwd").send_keys("123456789")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitLogin").click()
        time.sleep(5)

        text_header = browser.find_element(By.ID, "center_column").text
        text_body = browser.find_element(By.CSS_SELECTOR, "p.info-account").text

        self.assertIn("Welcome", text_body)
        self.assertIn("MY ACCOUNT", text_header)

    #Login menggunakan email salah
    def test_b_failed_login_invalid_email(self):
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email").send_keys("indrayaza@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID, "passwd").send_keys("123456789")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitLogin").click()
        time.sleep(5)

        text_header = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text

        self.assertIn("error", text_header, "not same")
        self.assertIn("Invalid email address.", text_header, "not same")

    #Login menggunakan password salah
    def test_c_failed_login_invalid_password(self):
        browser = self.browser
        browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(5)
        browser.find_element(By.ID, "email").send_keys("indrayaza8@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID, "passwd").send_keys("1111111")
        time.sleep(1)
        browser.find_element(By.NAME, "SubmitLogin").click()
        time.sleep(5)

        text_header = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text

        self.assertIn("error", text_header, "not same")
        self.assertIn("Authentication failed.", text_header, "not same")

    #Login dengan mengosongkan field email dan password
    def test_d_failed_login_email_and_password_blank(self): 
        #steps
        browser = self.browser
        browser.get(
            "http://automationpractice.com/index.php?controller=authentication&back=my-account")
        time.sleep(3)
        browser.find_element(By.ID, "SubmitLogin").click()
        time.sleep(5)

        #validation
        text_registered = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text

        self.assertIn('error', text_registered)
        self.assertIn('required', text_registered)
    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
