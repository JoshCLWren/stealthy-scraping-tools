# Stealthy Scraping Tools

Do not use puppeteer and playwright for scraping. [Explanation.](https://incolumitas.com/2021/05/20/avoid-puppeteer-and-playwright-for-scraping/)

We only use the [CDP](https://developer.chrome.com/docs/devtools/) to obtain the page source and to get the absolute coordinates for an arbitrary CSS selector. That's all what is needed for efficient scraping.

Mouse movements and typing is handled by `pyautogui` or other means, but not with JavaScript or with the CDP! Reason: Browser based mouse and keyboard emulation is very easy detectable!

## Theory 

1. Analyzing key strokes: [TypeNet: Deep Learning Keystroke Biometrics](https://arxiv.org/abs/2101.05570)
2. Research how to mimic human mouse movements: [BeCAPTCHA-Mouse: Synthetic Mouse Trajectories and Improved Bot Detection](https://arxiv.org/abs/2005.00890)

## Full Example

The bot challenge that can be found here [bot.incolumitas.com/#botChallenge](https://bot.incolumitas.com/#botChallenge) will be solved in the following quick tutorial.

The example code can be found in `example.py`.

Clone the repo:

```
git clone https://github.com/NikolaiT/stealthy-scraping-tools
cd stealthy-scraping-tools
```

Activate a pipenv environment with:

```bash
pipenv shell
```

And then run the bot with:

```python
python example.py
```

## TODO

+ Look at Kernel/OS level mouse/keyboard control commands (Ditch `pyautogui`)
+ Use the math from [ghost-cursor](https://github.com/Xetera/ghost-cursor)
+ Create a set of typign recordings and use it to derive rules for bot writing


