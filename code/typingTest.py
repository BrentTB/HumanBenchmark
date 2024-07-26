from controlWebpage import controlWebpage

# if sign in, it needs a url and a testname, else it needs a url directly to the test
def interact_with_webpage(signIn, url, testName=""):
    textBoxClass = "letters notranslate"

    web = controlWebpage(signIn, url, testName)

    paragraph = web.getDiv(className=textBoxClass).text
    web.getDiv(className=textBoxClass).send_keys(paragraph)

    web.waitForKey("x")  # Wait for the 'x' key to be pressed


if __name__ == "__main__":

    # interact_with_webpage(True, "https://humanbenchmark.com", testName="Typing")
    interact_with_webpage(False, "https://humanbenchmark.com/tests/typing")
