import click

# Make this a command line script
@click.command()
# Require that at least one file be given that already exists and is readable and writable
@click.argument("files_to_be_read", nargs=-1, type=click.Path(exists=True, readable=True, writable=True))
# @click.option("--format", multiple=True, default=["json"])
def view(files_to_be_read):
    for filename in files_to_be_read:
        file = ''.join(filename)
        friendly_file = click.format_filename(file)
        click.echo(f'Opening {friendly_file}. . .')
        click.echo('_______________________________________________________________________________')
        content = click.open_file(friendly_file, mode='r', encoding=None, errors='strict', lazy=None, atomic=False)
        click.echo(content.read())
        click.echo('_______________________________________________________________________________')