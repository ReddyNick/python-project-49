import random


def construct_brain_progression_questions():
    prompt = 'What number is missing in the progression?'
    num_questions = 3
    min_number, max_number = 1, 20
    min_delta, max_delta = 1, 20
    min_seq_size, max_seq_size = 5, 12

    question_answer_pairs = []
    for _ in range(num_questions):
        start = random.randint(min_number, max_number)
        delta = random.randint(min_delta, max_delta)
        seq_size = random.randint(min_seq_size, max_seq_size)

        sequence = []
        next_num = start
        for _ in range(seq_size):
            sequence.append(str(next_num))
            next_num += delta

        mask_index = random.randint(0, len(sequence) - 1)
        answer = sequence[mask_index]
        sequence[mask_index] = '..'
        question = ' '.join(sequence)

        question_answer_pairs.append((question, answer))

    return question_answer_pairs, prompt
