from wordle_game import get_feedback

class WordleSolver:


    def __init__(self, word_list):
        self.possible_words = word_list.copy()
        self.english_letter_frequencies = {
            'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
            'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
            'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
            'P': 1.93, 'B': 1.49, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
            'Q': 0.10, 'Z': 0.07
        }   
    
    def choose_best_word(self):
        """
        Choose the best word based on the current possible words.
        Using letter frequency analysis to determine the best guess.
        """
        def calculate_word_score(word):
            return sum(self.english_letter_frequencies.get(letter.upper(), 0) for letter in set(word))

        best_word = max(self.possible_words, key=calculate_word_score)
        return best_word

    def receive_feedback(self, guess, feedback):
        """
        Update the list of possible words based on the feedback received.
        """
        words = []
        for word in self.possible_words:
            if get_feedback(guess, word) == feedback:
                words.append(word)
        self.possible_words = words
