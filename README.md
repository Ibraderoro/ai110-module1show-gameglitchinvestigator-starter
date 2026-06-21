# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Game Purpose:** The application is designed to act as an interactive numeric guessing playground where players select a difficulty tier, analyze system direction hints (Higher/Lower), and attempt to pin down a dynamically generated secret integer within a set limit of turns.

- **Bugs Discovered:**
  1. **Variable Commitment Issue (State Flip):** On even-numbered guess attempts, the system explicitly re-cast the secret integer into a string format, causing a catastrophic `TypeError` or faulty alphabetical evaluation when compared against numeric inputs.
  2. **Inverted Directional Indicator Hints:** The operational boundaries inside the evaluation block were backward, feeding players an instruction to guess *higher* when their entry was already exceeding the secret target.
  3. **Broken Scoring Engine:** Incorrect guesses on even turns mistakenly increased the user's score instead of penalizing them, and consecutive failures could plunge the cumulative score deep into negative values.
  4. **Stale State Cache on Refresh:** The "New Game" button updated the secret number but failed to flush the active win/loss status string, locking players into an infinite freeze-screen loop.
  5. **Off-by-One Counter Reset:** The guess submission block incremented turn counts unconditionally prior to evaluating data cleanliness, cutting player turns short.
- **Fixes Applied:**
  1. Isolated and decoupled all backend operations into `logic_utils.py` while ensuring strict parameters casting (`int()`) to stop data type pollution.
  2. Reversed the comparison conditions (`guess > secret`) to trigger clean, accurate textual evaluations (`"Too High"`, `"Too Low"`).
  3. Integrated a scoring clamp via `max(0, result)` to ensure player scores cleanly floor at zero.
  4. Configured the "New Game" workflow to fully clear, reset, and reinitialize every persistent session state dictionary track.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. **Setup & Configuration:** The player launches the interface, setting the game difficulty to **Normal**. The back-end engine automatically instantiates a fresh session state configuration, generating a secret tracking target (e.g., `50`), resetting attempts to `0`, and setting the baseline score to `0`.
2. **First Guess Execution (High):** The player types `75` into the input bar and submits. The engine handles the input, flags it as valid, and returns a plain string status of `"Too High"`. The web view converts this value to display a helpful warning banner: **Go LOWER!**
3. **Second Guess Execution (Low):** The player adjusts and inputs `25`. The engine checks the number, determines it is below the boundary, and triggers the active UI indicator: **Go HIGHER!**
4. **Target Capture (Winning State):** The player submits exactly `50`. The validation algorithm reports an exact match (`"Win"`). The score tracker awards points utilizing the dynamic attempt efficiency algorithm (`100 - 10 * attempt_number`), fires off a screen-wide celebratory balloon animation, updates the system state cache status to `"won"`, and displays the final score dashboard.
5. **Session Flush:** The player hits the **"New Game "** button. The application cleanly wipes the history cache arrays, refreshes the core session status parameters back to `"playing"`, sets the score back to `0`, selects an entirely new hidden integer, and securely mounts a fresh board setup.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
================================================================================ test session starts ================================================================================
platform darwin -- Python 3.13.13, pytest-9.1.0, pluggy-1.6.0
rootdir: /Users/salisuibrahim/dev/machine-learning/CodePath/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 18 items                                                                                                                                                                  

tests/test_game_logic.py ..................                                                                                                                                   [100%]

================================================================================ 18 passed in 0.01s =================================================================================


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
