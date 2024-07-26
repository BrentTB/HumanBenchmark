from controlWebpage import controlWebpage

# if sign in, it needs a url and a testname, else it needs a url directly to the test
def interact_with_webpage(signIn, url, testName=""):

    web = controlWebpage(signIn, url, testName)

    web.wait(3) # improves responsiveness and gets a better score, but not strictly needed
    web.getElementByText("Reaction Time Test").click()

    for i in range(4):
        web.getElementByText("Click!").click()
        web.getElementByText("Click to keep going").click()
    
    web.getElementByText("Click!").click()

    web.waitForKey("x")  # Wait for the 'x' key to be pressed


if __name__ == "__main__":

    interact_with_webpage(True, "https://humanbenchmark.com", testName="Reaction Time")
    # interact_with_webpage(False, "https://humanbenchmark.com/tests/reactiontime")
