from controlWebpage import controlWebpage

MAX_SCORE=41

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
def interact_with_webpage(signIn, url, testName="",scoreToGet=MAX_SCORE ):
    web = controlWebpage(signIn, url, testName)
    scoreToGet = min(scoreToGet, MAX_SCORE)

    web.pressButton("Start Test")

    score=4
    while(score < scoreToGet):
        elementsInOrder=getElementsInOrder(web)
        for element in elementsInOrder:
            element.click()
        score+=1
        if score != MAX_SCORE: web.pressButton("Continue")
    
    # lose if we aren't on 41, which is the max score
    if(score != MAX_SCORE):
        for i in range(3):
            elementsInOrder=getElementsInOrder(web)
            
            elementsInOrder[1].click()
            if i != 2: web.pressButton("Continue")

    web.waitForKey("x")  # Wait for the 'x' key to be pressed


if __name__ == "__main__":

    # interact_with_webpage(True, "https://humanbenchmark.com", testName="Chimp Test")
    interact_with_webpage(False, "https://humanbenchmark.com/tests/chimp",scoreToGet=50)

# max score you can get is 41, so if you try get higher, you still get this