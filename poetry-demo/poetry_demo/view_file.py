import click

@click.command()
@click.argument("filename", nargs=-1, type=click.Path(exists=True, readable=True, writable=True))
# @click.argument('input', type=click.File("r"))
# @click.argument('output', type=click.File('wb'))
# @click.option("--format", multiple=True, default=["json"])
def view(filename):
    file = ''.join(filename)
    file = click.format_filename(file)
    click.echo(f'Opening {file}. . .')
    click.echo('_______________________________________________________________________________')
    content = click.open_file(file, mode='r', encoding=None, errors='strict', lazy=None, atomic=False)
    click.echo(content)
    # click.open_file(mode='w', encoding=None, errors='strict', lazy=None, atomic=False)
    click.echo('_______________________________________________________________________________')