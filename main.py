from wordle_game import WordleGame, load_word_list
from ai_solver import WordleSolver

def main():
    word_list = load_word_list()
    game = WordleGame(word_list)
    solver = WordleSolver(word_list)

    attempts, history = game.simulate_game(solver)

    if attempts != -1:
        print(f"🎯 AI solved it in {attempts} tries!")
    else:
        print("💀 AI failed.")

    for guess, feedback in history:
        print(f"{guess.upper()} → {feedback}")

if __name__ == "__main__":
    main()
