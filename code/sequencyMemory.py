from controlWebpage import controlWebpage

CLASS_DEFAULT = "square"
CLASS_ACTIVE = "square active"


def getNextElement(web, elementsInOrder):
    assert isinstance(web, controlWebpage)
    assert isinstance(elementsInOrder, list)

    # wait for a block to highlight, and then wait until no blocks highlight
    web.getDiv(className=CLASS_ACTIVE)

    allPrev = []
    all = web.getAllElements(xpath=f'//div[@class="{CLASS_ACTIVE}"]')
    while(len(all) != 0):
        allPrev = all
        all = web.getAllElements(xpath=f'//div[@class="{CLASS_ACTIVE}"]')
    elementsInOrder.append(allPrev[0])

    # wait for it to not be active so I can click
    # while(web.xpathExists(f'//div[@class="{CLASS_ACTIVE}"]')):
    #         continue
    return elementsInOrder
 
# if sign in, it needs a url and a testname, else it needs a url directly to the test
def interact_with_webpage(signIn, url, testName="", scoreToGet=50):
    web = controlWebpage(signIn, url, testName)

    web.pressButton("Start")

    score=1

    elementsInOrder=[]

    while(score < scoreToGet):
        elementsInOrder = getNextElement(web, elementsInOrder)
        
        for element in elementsInOrder:
            element.click()
        score+=1


    #lose by choosing the next element tht isnt the same as the first element
    elementsInOrder = getNextElement(web, elementsInOrder)
    for element in elementsInOrder:
        if element != elementsInOrder[0]: 
            element.click()
            break

    web.waitForKey("x")  # Wait for the 'x' key to be pressed


if __name__ == "__main__":

    # interact_with_webpage(True, "https://humanbenchmark.com", testName="Sequence Memory", scoreToGet=66)
    interact_with_webpage(False, "https://humanbenchmark.com/tests/sequence", scoreToGet=30)

# max score you can get is 41, so if you try get higher, you still get this