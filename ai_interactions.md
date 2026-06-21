# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| **Float String Pollution** (e.g., inputting `"3.7"`) | *"Identify edge-case inputs like float strings that might break a naive integer cast in parse_guess, and write a pytest case to handle them gracefully."* | `test_parse_guess_rejects_float_string()` asserting `ok is False`, `value is None`, and `err is not None`. | **Yes** | Streamlit text inputs capture strings. If a user enters a decimal, direct casting via `int()` crashes the script with a `ValueError`. This ensures it is caught defensively early. |
| **String-Poluted Secret Keys** (Type Mismatches) | *"Write a test block ensuring check_guess does not crash or evaluate incorrectly if app.py passes the secret number as a string data type on even attempts."* | `test_check_guess_string_secret_win()` asserting `check_guess(50, "50") == "Win"`. | **Yes** | The initial buggy game mutated the type of the secret variable across turns. Forcing internal defensive casting to `int()` within the utility functions isolates the runtime from type bugs. |
| **Zero-Floor Point Bounds** (Negative Score Drift) | *"Generate a pytest function to verify that consecutive penalties applied by update_score never drive the player's points into negative integers."* | `test_update_score_never_goes_negative()` asserting `update_score(3, "Too High", 1) == 0`. | **Yes** | Frequent incorrect guesses deduct 5 points at a time. Using mathematical clamping via `max(0, result)` structurally protects the integrity of the player scoring boundary. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
