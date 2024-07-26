# Human Benchmark completed by a robot

Inspired by the Youtuber [Codebullet](https://www.youtube.com/@codebulletsdayoff582), this project completes all tasks of the [Human Benchmark website](https://humanbenchmark.com) using Python.

As compared to taking a screenshot and processing it, these scripts use Selenium to open the website and interact with it directly. This allows for a higher performance, resulting in getting the 100% percentile for each test, and means that the browser can be left in the background and ignored.

## Code Explanation

9 python scripts are included. 8 Correspond to the different tests, while the last is a class that allows control of the website

For each test, it can be called with

```
interact_with_webpage(True, "https://humanbenchmark.com", testName="Sequence Memory", scoreToGet=66)
```

or

```
interact_with_webpage(False, "https://humanbenchmark.com/tests/sequence", scoreToGet=5)
```

The first parameter is true if you want to sign in to your account when running the test

If true, the second parameter is the URL of the human benchmark website, 'testName' is the name of the test, as shown on the dashboard

If false, the second parameter is the URL of the specific test in question

'scoreToGet' is a parameter that exists for tests that have no obvious upper limit. ie: while [Reaction Time](#reaction-time) has a defined end, [Verbal Memory](#verbal-memory) can continue as long as the user would like

## Default Behaviour

By default, each program will either do its best, or go until it reaches the 'scoreToGet' provided, and then loses. At this point the user can save the score easily if desired.

After ending the test, the program will end when the 'x' key is pressed, so make sure to save the score before typing an x and closing the browser.

Specific ending behaviour can be defined by removing the

```
web.waitForKey("x")
```

at the end of the interact_with_webpage function, and adding the desired end code.

In order to automatically save the results, you can use the following:

```
web.pressButton("Save score")
web.waitForKey("x")
```

## Environment variable .env file

If you want to sign in to your account when running the program, a .env file must be provided with the following values:

```
USERNAME=userUsername
PASSWORD=userPassword
```

The values provided must be for your [human benchmark account](https://humanbenchmark.com/signup)

## Test Result and Explanations

### [Aim Test](/aimTest.py):

- Best score: 29ms
- Explanation: This speed is close to optimal for my computer, however on a better computer a higher score is very possible. This score means one target is clicked per 1ms

### [Chimp Test](/chimpTest.py):

- Best score: 41
- Explanation: This is the highest score possible, and the game ends once you reach this score

### [Number Memory](/chimpTest.py):

- Best score: 86
- Explanation: There is no known limit for how high a score can be achieved. As you reach higher scores, it takes an excedingly long time to do a single level

### [Reaction Time](/reactionTime.py):

- Best score: 9ms
- Explanation: This speed is the fastest I can get on my computer, however on a better computer a higher score is very possible

### [Sequence Memory](/sequencyMemory.py):

- Best score: 66
- Explanation: There is no known limit for how high a score can be achieved. As you reach higher scores, it takes very long to do a single level

### [Typing Test](/typingTest.py):

- Best score: 9248 words per minute
- Explanation: This score is close to the highest I can get on my computer, although every time it is run I get a vastly different score. A higher score should be possible on a better computer

### [Verbal Memory](/verbalMemory.py):

- Best score: 666
- Explanation: There is no known limit for how high a score can be achieved. Each level takes the same amount of time so you can easily get a very large score

### [Visual Memory](/visualMemory.py):

- Best score: 98
- Explanation: A higher score may be possible, but this is where I lose on my computer. Some levels will not save correct and the program loses. However, due to the 3 lives given, a high score can still be obtained
