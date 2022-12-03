from pathlib import Path
from tempfile import TemporaryDirectory
import glob
from click.testing import CliRunner

from sord.cli import cli


def setup():
    """Create tempdir and generate files"""
    td = TemporaryDirectory()
    tdp = Path(td.name)
    file_numbers = '1 2 3 4 5 6'.split()
    file_content = '1 2 2 3 3 3'.split()
    for n, c in zip(file_numbers, file_content):
        p = tdp / f'file{n}.txt'
        with open(p, 'w') as f:
            f.write(c)
    return td


def test_originals_correct():
    expected_originals = [f'file{n}.txt' for n in (1, 2, 4)]
    _test_cli('original', expected_originals)


def test_duplicates_correct():
    expected_duplicate = [f'file{n}.txt' for n in (3, 5, 6)]
    _test_cli('duplicate', expected_duplicate)


def _test_cli(kind, expected, *args):
    td = setup()
    runner = CliRunner()
    result = runner.invoke(cli, [kind, *glob.glob(td.name + '/*'), *args])
    assert result.exit_code == 0
    assert sorted(result.output.strip().split('\n')) == [td.name + '/' + f for f in expected]
    td.cleanup()
