from wordle_game import get_feedback

class WordleSolver:
    def __init__(self, word_list):
        self.possible_words = word_list.copy()

    def make_guess(self):
        return self.possible_words[0]  #! fucking shitty ai

    def receive_feedback(self, guess, feedback):
        """
        Update the list of possible words based on the feedback received.
        """
        words = []
        print("NEW ATTEMPT")
        for word in self.possible_words:
            if get_feedback(guess, word) == feedback:
                words.append(word)
                print(f"Word {word} matches feedback {feedback}")
        self.possible_words = words
