import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")



def hello(count, name):
    #comments go here
    #doc String is a type comment
  """Simple
       program that
        greets NAME for a total of COUNT times.
  """
  y=34
  print(y)
  for _ in range(count):
    click.echo(f"Hello, {name}!")
  m=34
  print(m)

hello()