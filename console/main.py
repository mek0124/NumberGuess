from app.commands.hello import hello_command
from app.commands.game import play_game

import click


@click.group()
def cli():
    pass


cli.add_command(hello_command)
cli.add_command(play_game)


if __name__ == '__main__':
    cli()