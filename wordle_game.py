import random

def load_word_list():
    with open("word_list.txt") as f:
        return [word.strip().lower() for word in f if len(word.strip()) == 5]

def get_feedback(guess, target):
    feedback = [''] * 5
    used = [False] * 5  

    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = '🟩'
            used[i] = True

    for i in range(5):
        if feedback[i] == '':
            if guess[i] in target:
                for j in range(5):
                    if guess[i] == target[j] and not used[j]:
                        feedback[i] = '🟨'
                        used[j] = True
                        break
                else:
                    feedback[i] = '⬛'
            else:
                feedback[i] = '⬛'

    return ''.join(feedback)

class WordleGame:
    def __init__(self, word_list, target_word=None):
        self.word_list = word_list
        self.target_word = target_word or random.choice(word_list)
        self.max_attempts = 6

    def simulate_game(self, solver):
        attempt = 1
        history = []

        while attempt <= self.max_attempts:
            guess = solver.choose_best_word()
            if guess not in self.word_list:
                raise ValueError(f"Invalid guess: {guess}")
            
            feedback = get_feedback(guess, self.target_word)
            solver.receive_feedback(guess, feedback)
            history.append((guess, feedback))

            if guess == self.target_word:
                return attempt, history
            attempt += 1

        return -1, history
