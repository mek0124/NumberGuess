import random
import click


@click.command("play_game")
@click.option("--username", help="Your username for the game")
@click.option("--tries", default=5, help="The number of tries the user gets for the game. 5 by default")
@click.option("--answer", help="The answer for the other person to guess. Random (1-20) by default")
def play_game(username: str, tries: int, answer: int = None):
    if not answer:
        answer = random.randint(1,21)
        
    while tries > 0:
        user_guess = int(input("Your Guess"))

    return click.echo(f"Game Over! Answer: {answer}")