import random


def construct_brain_gcd_questions():
    prompt = 'Find the greatest common divisor of given numbers.'
    num_questions = 3
    min_number = 0
    max_number = 99

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    question_answer_pairs = []
    for _ in range(num_questions):
        a = random.randint(min_number, max_number)
        b = random.randint(min_number, max_number)
        question = f"{a} {b}"
        answer = str(gcd(a, b))
        question_answer_pairs.append((question, answer))

    return question_answer_pairs, prompt
