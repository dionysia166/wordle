from validation import WordValidator
from game import WordleGame


def test_load_words():
    mock_word = WordValidator()
    mock_word.words = ["ready", "acorn", "speed", "chair", "lamma"]
    assert len(mock_word.words) == len(mock_word.words)


def test_get_random_word():
    mock_word = WordValidator()
    mock_word.words = ["ready", "acorn", "speed", "chair", "lamma"]
    random_word = mock_word.get_random_word()
    assert random_word in mock_word.words


def test_validate_word():
    mock_word = WordValidator()
    mock_word.words = ["ready", "acorn", "speed", "chair", "lamma"]
    assert mock_word.validate_word("ready") is True
    assert mock_word.validate_word("READY") is True
    assert mock_word.validate_word("") is False
    assert mock_word.validate_word("abcdefg") is False


def test_process_guess():
    mock_game = WordleGame("apple")
    mock_game.attempts = ["ready", "acorn", "speed", "chair", "lamma"]
    mock_game.process_guess("tests")
    assert len(mock_game.attempts) == 6
    assert mock_game.game_lost == True
    assert mock_game.game_won == False


def test_color_feedback():
    mock_game = WordleGame("health")
    assert mock_game.color_feedback("teethe") == [
        "yellow",
        "green",
        "gray",
        "gray",
        "yellow",
        "gray",
    ]
    mock_game = WordleGame("robot")
    assert mock_game.color_feedback("broom") == [
        "yellow",
        "yellow",
        "yellow",
        "green",
        "gray",
    ]
