from wordle_game import WordleGame, load_word_list
from ai_solver import WordleSolver

def test_ai_solver(num_tests=4000):
    word_list = load_word_list()
    wins = 0

    for i in range(num_tests):
        game = WordleGame(word_list)
        solver = WordleSolver(word_list)

        attempts, _ = game.simulate_game(solver)
        print(_[len(_)-1], i)

        if attempts != -1:  
            wins += 1

    win_percentage = (wins / num_tests) * 100
    print(f"AI won {wins} out of {num_tests} games.")
    print(f"Win percentage: {win_percentage:.2f}%")

if __name__ == "__main__":
    test_ai_solver()