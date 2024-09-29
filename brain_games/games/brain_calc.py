import random


def construct_brain_calc_questions():
    prompt = 'What is the result of the expression?'
    num_questions = 3
    min_number = 0
    max_number = 99
    operations = ['+', '-', '*']

    question_answer_pairs = []
    for _ in range(num_questions):
        a = random.randint(min_number, max_number)
        b = random.randint(min_number, max_number)

        if b > a:
            a, b = b, a

        operation = random.choice(operations)

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        else:
            result = a * b

        result = str(result)
        question = f"{a} {operation} {b}"
        question_answer_pairs.append((question, result))

    return question_answer_pairs, prompt
