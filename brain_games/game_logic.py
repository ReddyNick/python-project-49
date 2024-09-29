import prompt
from brain_games.cli import welcome_user


def run_game(question_answer_pairs, game_prompt):
    user_name = welcome_user()
    print(game_prompt)

    is_all_correct = True
    for question, correct_answer in question_answer_pairs:
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            is_all_correct = False
            break

    if is_all_correct:
        print(f"Congratulations, {user_name}!")
