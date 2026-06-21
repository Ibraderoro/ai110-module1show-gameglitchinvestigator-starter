from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Bug: Hard difficulty was capped at 50 instead of 250 ---

def test_hard_difficulty_range():
    low, high = get_range_for_difficulty("Hard")
    assert high == 250, f"Hard difficulty should cap at 250, got {high}"

def test_easy_and_normal_ranges_unchanged():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)


# --- Bug: parse_guess silently truncated float strings instead of rejecting them ---

def test_parse_guess_rejects_float_string():
    ok, value, err = parse_guess("3.7")
    assert ok is False, "Float strings should be rejected"
    assert value is None
    assert err is not None

def test_parse_guess_rejects_empty():
    ok, value, err = parse_guess("")
    assert ok is False

def test_parse_guess_rejects_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False

def test_parse_guess_accepts_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


# --- Bug: check_guess broke when secret was passed as a string (int/str type mismatch) ---

def test_check_guess_string_secret_win():
    # app.py passed secret as str("50") on even attempts; must still detect a win
    result = check_guess(50, "50")
    assert result == "Win"

def test_check_guess_string_secret_too_high():
    result = check_guess(60, "50")
    assert result == "Too High"

def test_check_guess_string_secret_too_low():
    result = check_guess(40, "50")
    assert result == "Too Low"

def test_check_guess_returns_plain_string_not_tuple():
    # Original buggy version returned a 2-tuple; fixed version returns a plain string
    result = check_guess(50, 50)
    assert isinstance(result, str), "check_guess must return a plain string, not a tuple"


# --- Bug: update_score awarded points for "Too High" on even attempts and let score go negative ---

def test_update_score_too_high_always_penalizes():
    # Even attempt number used to award +5 instead of penalizing
    score = update_score(10, "Too High", 2)
    assert score == 5, f"Too High should always subtract 5, got {score}"

def test_update_score_too_low_penalizes():
    score = update_score(10, "Too Low", 1)
    assert score == 5

def test_update_score_never_goes_negative():
    # Score should floor at 0, not go below
    score = update_score(3, "Too High", 1)
    assert score == 0, f"Score must not go negative, got {score}"

def test_update_score_win_uses_attempt_number_directly():
    # Bug used attempt_number + 1; correct formula is 100 - 10 * attempt_number
    score = update_score(0, "Win", 3)
    assert score == 70, f"Win on attempt 3 should award 70 points, got {score}"

def test_update_score_win_minimum_10_points():
    # Attempt 10+ would yield <= 0 without the floor
    score = update_score(0, "Win", 10)
    assert score == 10, f"Win should award at least 10 points, got {score}"
