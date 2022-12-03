import os
import sys
from pprint import pprint

import click
from tqdm import tqdm

from sord.util import group_items, file_contents


@click.command()
@click.argument('output', type=click.Choice(['original', 'duplicate'], case_sensitive=False))
@click.argument('files', nargs=-1, type=click.Path(exists=True, dir_okay=False))
@click.option('--verbose', '-v', is_flag=True, help='Print intermediate hash dictionary.')
@click.option('--progress', '-p', is_flag=True, help='Show a progress bar.')
def cli(output, files, progress, verbose):
    """Simple program that sorts original files from duplicates by hash and date.
    RETURN type specifies whether to return originals or duplicates."""
    identifiers = files
    items = file_contents(files)

    if progress:
        items = tqdm(items)

    hashes = group_items(items, identifiers)
    results = {'original': [], 'duplicate': []}
    for hash_, paths in hashes.items():
        original, *duplicate = sorted(paths, key=lambda p: os.path.getctime(p))
        results['original'].append(original)
        results['duplicate'].extend(duplicate)

    if verbose:
        pprint(dict(hashes), stream=sys.stderr)

    print('\n'.join(results[output]))
