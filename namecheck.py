import click

def logic(name):
    if name == "Marco":
        return "Polo"
    else:
        return "No Match"

@click.command()
@click.option("--name")
def marco(name):
    """This is a Marco Polo function"""
    
    result = logic(name)
    click.echo(click.style('Checking Marco Polo', fg='green'))
    if result == "Polo":
        click.echo(click.style(f"{result}",bg='blue', fg='red' ))
    else:
        click.echo(click.style(f"ATTENTION! Wrong Name: {result}", 
            blink=True, bold=True))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    marco()