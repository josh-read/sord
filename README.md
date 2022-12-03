# **S**eperate **O**r **R**emove **D**uplicates

---

Command line tool to identify duplicate files.
Sord can be combined with other common command
line tools to relocate or rename originals or
delete duplicates. See usage for examples.

## Install

Until this package is added to PyPI, the
recommended way of installing sord is by cloning
from GitHub.

```commandline
$ git clone https://github.com/josh-read/sord/master
$ cd sord
$ pip install .
```

## Usage

The following examples have been tested on MacOS
Monterey 12.3.1. Assume there is a directory
`test/` containing three files:

- `file1.txt` which is unique.
- `file2.txt` which is different from `file1.txt`, but the same as
- `file3.txt`

Now, running sord on the files in `test/` gives:

```commandline
$ sord original test/*
file1.txt
file2.txt
```

or,

```commandline
$ sord duplicate test/*
file3.txt
```

because `file2.txt` was created before `file3.txt`.
Now this means it is possible to copy the originals:

```commandline
$ sord original test/* | xargs -I '{}' cp '{}' test_originals
```

or move the duplicates,

```commandline
$ sord duplicate test/* | xargs -I '{}' mv '{}' test_duplicates
```

or if you're feeling brave, delete them.

```commandline
$ sord duplicate test/* | xargs rm
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Support and bug reports

To ask for help or report an issue, please
[raise an issue](https://github.com/josh-read/sord/issues).

## License

[MIT](https://github.com/josh-read/sord/blob/master/LICENCE)