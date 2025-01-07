from flask import Flask, request, render_template, session, redirect, flash
import secrets, uuid
from validation import WordValidator
from game import WordleGame

app = Flask(__name__)

app.secret_key = secrets.token_hex()

validator = WordValidator()
validator.load_words("words.txt")

target_word = validator.get_random_word()


@app.route("/")
def home():
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())
    return render_template("home.html")


@app.route("/game", methods=["GET"])
def game_get():
    game_state = session.get("game_state", {})

    if not game_state:
        game = WordleGame(target_word)
        game_state = {
            "target_word": game.target_word,
            "attempts": game.attempts,
            "max_attempts": game.max_attempts,
            "game_won": game.game_won,
            "game_lost": game.game_lost,
        }
        session["game_state"] = game_state
    else:
        game = WordleGame(game_state["target_word"])
        game.attempts = game_state["attempts"]
        game.game_won = game_state["game_won"]
        game.game_lost = game_state["game_lost"]

    feedback = [game.color_feedback(attempt) for attempt in game.attempts]

    current_attempt = len(game.attempts)

    return render_template(
        "game.html",
        attempts=game_state["attempts"],
        max_attempts=game_state["max_attempts"],
        feedback=feedback,
        current_attempt=current_attempt,
        game_won=game_state["game_won"],
        game_lost=game_state["game_lost"],
    )


@app.route("/game", methods=["POST"])
def game_post():
    game_state = session.get("game_state", {})

    game = WordleGame(game_state["target_word"])
    game.attempts = game_state["attempts"]
    game.game_won = game_state["game_won"]
    game.game_lost = game_state["game_lost"]

    guessed_word = "".join(
        request.form.get(f"attempt_{len(game.attempts)}_{i}", "").lower()
        for i in range(5)
    )

    if not validator.validate_word(guessed_word):
        flash("Invalid word", "error")
        game.bad_attempt = True
    else:
        game.process_guess(guessed_word)
        game.bad_attempt = False

    session["game_state"] = {
        "target_word": game.target_word,
        "attempts": game.attempts,
        "max_attempts": game.max_attempts,
        "game_won": game.game_won,
        "game_lost": game.game_lost,
    }

    if game.game_won:
        flash("Success! You’ve found the word!", "success")
    elif game.game_lost:
        flash(f"You didn't guess it. The word was '{game.target_word}'.", "error")

    return redirect("/game")

import os
if __name__ == "__main__":
    os.environ["FLASK_APP"] = "app.py"
