from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

class controlWebpage:
    """
    A class used to open and control a website using Selenium
    While this class can be used for other websites, it was designed with https://humanbenchmark.com/ in mind
    """
    def __init__(self, signIn, url, testName="", agreePrivacy=False):
        global _driver
        self._load_env()
 
        try:
            _driver = webdriver.Firefox()
            _driver.get(url)

            # get rid of annoying privacy popup
            if agreePrivacy: self._agreePrivacy()

            if signIn:
                self._logIn()
                self._chooseTest(testName)

        except Exception as error:

            # see if the error is a stale element not found
            if("stale element not found" in str(error)):
                _driver.quit()
                self.__init__(signIn, url, testName) # retry again. Can happen a few times before it runs properly
            else:
                print("ERROR opening driver: ",error)
                exit(1)

    def getElementWhenExists(self, xpath):
        """
        waits for an element to exist and then returns that element. If an invalid element was given, this will loop forever

        @param xpath: the xpath of the html element to be returned
        """
        while True:
            try:
                return _driver.find_element(By.XPATH, xpath)
            except:
                continue


    def buttonExist(self, text):
        return self.xpathExists(f'//button[text()="{text}"]')
        
    def xpathExists(self, xpath):
        try:
            _driver.find_element(By.XPATH, xpath)
            return True
        except:
            return False

    def getDiv(self, className="", text=""):
        return self.getElementWhenExists(f'//div[text()="{text}"]|//div[@class="{className}"]')
    

    def getElementByText(self, text,element="*"):
        return self.getElementWhenExists(f'//{element}[text()="{text}"]')
    
    def getElementByXPath(self, xpath):
        return self.getElementWhenExists(xpath)
    
    def getAllElements(self,xpath):
        return _driver.find_elements(By.XPATH, xpath)

    def pressButton(self, text, type=""):
        if(type):
            self.getElementWhenExists(f'//button[text()="{text}" and @type="{type}"]|//span[text()="{text}" and @type="{type}"]|//input[text()="{text}" and @type="{type}"]').click()
        else:
            self.getElementWhenExists(f'//button[text()="{text}"]|//span[text()="{text}"]|//input[text()="{text}"]').click()

    def elementText(self, className):
        try:
            return _driver.find_element(By.CLASS_NAME, className).text
        except:
            return ""

    def enterInput(self, answer, type=""):
        if(type):
            _driver.find_element(By.XPATH, f'//input[@type="{type}"]').send_keys(answer)
        else:
            _driver.find_element(By.TAG_NAME, "input").send_keys(answer)

    def moveElementToElement(self, element1, element2):
        ActionChains(_driver).drag_and_drop(element1, element2).perform()

    def rightClick(self, element):
        ActionChains(_driver).context_click(element).perform()

    def wait(self, length):
        time.sleep(length)

    def waitForKey(self, key):
        # keyboard.wait(key)  
        self.wait(10)
        self.wait(0.1)

    def getenv(self, key):
        return os.getenv(key)
    
    def _agreePrivacy(self):
        """
        Waits for the privacy popup, and then presses the 'agree' button on the privacy popup

        If there is no privacy popup, this function could stop the program's running
        """
        self.pressButton("AGREE")

    def _load_env(self, file_path=".env"):
        """
        Load environment variables from the .env file
        """
        try:
            with open(file_path, "r") as file:
                for line in file:
                    # Skip comments and empty lines
                    if line.startswith("#") or not line.strip():
                        continue
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value
        except:
            return
    
    def _logIn(self):
        """
        Log the user into their account
        """
        logInPage = self.getElementWhenExists('//*/a[contains(text(), "LOGIN")]').get_attribute("href")
        _driver.get(logInPage)

        self.getElementWhenExists('//input[@name="username"]').send_keys(self.getenv("USERNAME"))
        self.getElementWhenExists('//input[@name="password"]').send_keys(self.getenv("PASSWORD"))
        self.getElementWhenExists('//input[@type="submit" and @value="Login"]').click()


    def _chooseTest(self, testName):
        """
        Click and choose the specified test

        @param testName: the name of the test as seen in the human benchmark dashboard
        """
        curPath = f'//div[contains(text(), "{testName}")]'
        self.getElementWhenExists(curPath)

        extension = self.getElementWhenExists(curPath + "/parent::td/parent::tr/td[2]/div/a").get_attribute("href")
        _driver.get(extension)

    def __del__(self):
        _driver.quit()

    _driver = ""