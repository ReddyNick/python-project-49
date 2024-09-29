import random
import math


def construct_brain_prime_questions():
    prompt = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    num_questions = 3
    min_number = 1
    max_number = 99

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    question_answer_pairs = []
    for _ in range(num_questions):
        num = random.randint(min_number, max_number)
        question = str(num)
        answer = 'yes' if is_prime(num) else 'no'
        question_answer_pairs.append((question, answer))

    return question_answer_pairs, prompt
