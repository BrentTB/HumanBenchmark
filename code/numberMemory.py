from controlWebpage import controlWebpage
import keyboard

# TODO: Get rid of these
NUMBER_CLASS = "big-number "

# if sign in, it needs a url and a testname, else it needs a url directly to the test
def interact_with_webpage(signIn, url, testName="",scoreToGet=50 ):

    web = controlWebpage(signIn, url, testName)

    # for btn in ["Start", "NEXT"]:
    web.pressButton("Start")

    cont = True
    score = 1

    stopOnE=False

    # TODO: this code can probbaly be simplified
    while score < scoreToGet:
        num = web.elementText(NUMBER_CLASS)
        while web.elementText(NUMBER_CLASS):

            if keyboard.is_pressed("e") and stopOnE:
                cont = False
            continue
        if not cont:
            break
        web.enterInput(num)
        web.pressButton("Submit")

        # check if we have lost, else continue
        if web.buttonExist("Save score"):
            break
        web.pressButton("NEXT")  # next
        print(score)
        score+=1

    # losing the game
    num = web.elementText(NUMBER_CLASS)
    while web.elementText(NUMBER_CLASS):
        continue
    web.enterInput(num + "1")
    web.pressButton("Submit")

    # web.pressButton("Save score")
    web.waitForKey("x")  # Wait for the 'x' key to be pressed

if __name__ == "__main__":

    # interact_with_webpage(True, "https://humanbenchmark.com", testName="Number Memory", scoreToGet=65)
    interact_with_webpage(False, "https://humanbenchmark.com/tests/number-memory", scoreToGet=30)