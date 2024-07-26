from controlWebpage import controlWebpage

CLASS_CHOOSE = "active css-lxtdud eut2yre1"
CLASS_DONT_CHOOSE = " css-lxtdud eut2yre1"

def getElementsInOrder(web):
    elementsInOrder=[]
    num=1
    while(True):

        xpath = f'//div[@data-cellnumber="{num}"]'
        if(web.xpathExists(xpath)):
            elementsInOrder.append(web.getElementByXPath(xpath))
        else:
            break
        num=num+1
    return elementsInOrder

# if sign in, it needs a url and a testname, else it needs a url directly to the test
def interact_with_webpage(signIn, url, testName="", scoreToGet=50):
    web = controlWebpage(signIn, url, testName)

    web.pressButton("Start")

    xpath = f'//div[@class="{CLASS_CHOOSE}"]'
    xpathLose = f'//div[@class="{CLASS_DONT_CHOOSE}"]'
    score=1
    lose=False

    while(score < scoreToGet):
        if(web.buttonExist("Save score")):
            lose=True
            break
        web.getDiv(className=CLASS_CHOOSE)
        correctSquares = web.getAllElements(xpath)
        while(web.xpathExists(xpath)):
            continue

        for element in correctSquares:
            element.click()
        while(web.xpathExists(xpath)):
            continue
        score+=1

    # lose
    if not lose:
        for i in range(3):
            if(web.buttonExist("Save score")): break
            web.getDiv(className=CLASS_CHOOSE)
            incorrectSquares = web.getAllElements(xpathLose)
            while(web.xpathExists(xpath)):
                continue

            for j in range(3):
                incorrectSquares[j].click()
            while(web.xpathExists(xpath)):
                continue

    web.waitForKey("x")  # Wait for the 'x' key to be pressed


if __name__ == "__main__":

    interact_with_webpage(True, "https://humanbenchmark.com", testName="Visual Memory", scoreToGet=100)
    # interact_with_webpage(False, "https://humanbenchmark.com/tests/memory", scoreToGet=40)


#TODO: finish this. Maybe add a check for if it hasnt changed in a while, then make it lose this round to continue