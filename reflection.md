# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- When I first ran the game, the Streamlit user interface loaded successfully in my browser, but attempting to play it immediately exposed major functional breakdown under the hood. The application suffered from severe data type mismatch errors when comparing inputs, and the gameplay mechanics did not behave logically. Specifically, the hint engine was completely inverted, giving a "Too Low" hint when my guess was actually higher than the secret number. Furthermore, clicking the "New Game" button failed to flush out the cache, causing old state values to persist and leave the app frozen on prior screens.

**Bug Reproduction Log**
  | Input | Expected Behavior | Actual Behavior | Console Output / Error |
  | Guess: '60' (Secret: '50') | Display a "Too High" hint warning. | Rendered a "Too Low" hint on screen. | None |
  | Any valid guess input | Decrement total attempts remaining by 1. | Subtracted points incorrectly, driving scores below zero. | None |
  | Click "New Game" button | Completely flush out active session state and pick a new target. | Cached values persisted, preventing a proper state refresh. | None |

## 2. How did you use AI as a teammate?

- I used Gemini and Claude Sonnet as my AI workspace pair-programmers to break down architectural bugs and plan the file refactor.
- One correct suggestion occurred when the AI advised completely separating the core gameplay math from the UI layer into 'logic_utils.py' and enforcing an explicit string return type. I verified this suggestion by running my test runner execution script, which immediately satisfied the grading contract requirements.
- One incorrect/misleading suggestion occurred when the AI initially tried to fix the terminal execution environment path by suggesting recursive code loop wraps inside 'app.py'. I verified this was wrong by identifying that Streamlit runs from top to bottom on every interaction, meaning recursion would cause resource crashes instead of solving path lookup errors.

---

## 3. Debugging and testing your fixes

- I decided a bug was genuinely fixed only when it simultaneously passed our automated Python tests and worked perfectly during manual playtesting.
- I ran our comprehensive unit tests using the explicit binary execution command './venv/bin/python -m pytest', which successfully validated 14 separate behavioral assertions across our script functions. This test block proved that my edge-case fixes—like protecting the score from going negative and catching string input mismatches—were bulletproof.
- The AI helped me understand the test files by annotating how the grading script called 'check_guess' directly without booting up the browser wrapper. This breakdown showed me exactly how to protect the required API signatures without altering required functionality.

---

## 4. What did you learn about Streamlit and state?

- Imagine Streamlit is a kitchen recipe script that completely re-runs from top to bottom every single time you tap a button, adjust a slider, or enter text. Because the code starts entirely over on every click, normal Python variables have total amnesia and forget your score or your secret number instantly. Streamlit Session State ('st.session_state') acts like a persistent memory vault on the side that safely guards your data across those re-runs so the game can actually track your progress.

---

## 5. Looking ahead: your developer habits

- I want to reuse the habit of thoroughly reviewing the automated testing suite files before writing a single line of application logic to map out expected interfaces.
- Next time I develop with an AI teammate, I will exclusively use "Ask before edit" or planning mode to carefully inspect git diff alterations line-by-line before allowing changes to rewrite my repository.
- This project changed my perspective by proving that AI-generated programs frequently look structurally convincing on the surface while remaining functionally broken underneath. Ultimately, a software engineer cannot blindly trust generated logic and must always act as the final human oversight authority through rigorous testing.
