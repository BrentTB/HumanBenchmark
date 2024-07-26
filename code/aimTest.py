from controlWebpage import controlWebpage

# 28 ms time
def interact_with_webpage(signIn, url, testName=""):

    web = controlWebpage(signIn, url, testName)

    web.wait(2) # needed for optimal performance on my computer

    for i in range(31):
        web.getElementByXPath('//div[@data-aim-target="true"]/div[6]').click() # has to be the 6th child, any others wont work

    web.waitForKey('x') # Wait for the 'x' key to be pressed
    


if __name__ == "__main__":

    # interact_with_webpage(True, "https://humanbenchmark.com", testName="Aim Trainer")
    interact_with_webpage(False, "https://humanbenchmark.com/tests/aim")
