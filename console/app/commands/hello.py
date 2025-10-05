import click


@click.command("hello")
@click.option("--name", help="The name of the user to greet", default="User")
def hello_command(name: str) -> None:
    return click.echo(f"Hello, {name}! Welcome To Number Guess!")
