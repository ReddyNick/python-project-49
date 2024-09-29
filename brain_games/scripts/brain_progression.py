#!/usr/bin/env python3
from brain_games.game_logic import run_game
from brain_games.games.brain_progression import construct_brain_progression_questions  # noqa: E501


def main():
    question_answer_pairs, prompt = construct_brain_progression_questions()
    run_game(question_answer_pairs, prompt)


if __name__ == "__main__":
    main()
