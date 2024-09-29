import random


def construct_brain_even_questions():
    prompt = 'Answer "yes" if the number is even, otherwise answer "no".'
    num_questions = 3
    min_number = 0
    max_number = 99

    question_answer_pairs = []
    for _ in range(num_questions):
        rand_number = random.randint(min_number, max_number)
        answer = 'yes' if rand_number % 2 == 0 else 'no'
        question_answer_pairs.append((rand_number, answer))

    return question_answer_pairs, prompt
