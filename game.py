class WordleGame:
    def __init__(self, target_word, max_attempts=6):
        self.target_word = target_word
        self.max_attempts = max_attempts
        self.attempts = []
        self.bad_attempt = False
        self.game_won = False
        self.game_lost = False

    def process_guess(self, guessed_word):
        guessed_word = guessed_word.lower()
        self.attempts.append(guessed_word)

        if guessed_word == self.target_word:
            self.game_won = True
        elif len(self.attempts) >= self.max_attempts:
            self.game_lost = True

    def color_feedback(self, guessed_word):
        feedback = ["gray"] * len(self.target_word)
        target_letters = list(self.target_word)

        for i, letter in enumerate(guessed_word):
            if letter == target_letters[i]:
                feedback[i] = "green"
                target_letters[i] = ""

        for i, letter in enumerate(guessed_word):
            if feedback[i] == "gray" and letter in target_letters:
                feedback[i] = "yellow"
                target_letters[target_letters.index(letter)] = ""

        return feedback
