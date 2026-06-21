def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 250  # FIX: Fixed upper bound from 50 to 250
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    # Handle accidental float inputs gracefully
    if "." in raw:
        return False, None, "That is not a number."

    try:
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        g = int(guess)
        s = int(secret)
    except (ValueError, TypeError):
        return "Too Low"

    if g == s:
        return "Win"
    if g > s:
        return "Too High" # FIX: Corrected inverted high/low indicator logic
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # Calculate score dynamically based on attempts taken
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        # Deduct a fixed penalty of 5 points for an incorrect guess
        result = current_score - 5
        return max(0, result) # Ensure score doesn't go negative

    return current_score
