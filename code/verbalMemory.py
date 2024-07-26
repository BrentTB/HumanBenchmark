from controlWebpage import controlWebpage

# if sign in, it needs a url and a testname, else it needs a url directly to the test
def interact_with_webpage(signIn, url, testName="",scoreToGet=50 ):

    web = controlWebpage(signIn, url, testName)

    web.pressButton("Start")

    cont = True
    score = 0
    allWords = []

    # TODO: this code can probably be simplified
    while score < scoreToGet:
        word = web.getDiv(className="word").text

        if(allWords.count(word)==0):
            allWords.append(word)
            web.pressButton("NEW")
        else:
            web.pressButton("SEEN")

        score+=1

    # losing the game, click wrong 3 times
    for i in range(3):
        word = web.getDiv(className="word").text

        if(allWords.count(word)==0):
            allWords.append(word)
            web.pressButton("SEEN")
        else:
            web.pressButton("NEW")

    web.waitForKey("x")  # Wait for the 'x' key to be pressed


if __name__ == "__main__":

    # interact_with_webpage(True, "https://humanbenchmark.com", testName="Verbal Memory", scoreToGet=666)
    interact_with_webpage(False, "https://humanbenchmark.com/tests/verbal-memory", scoreToGet=1000)
