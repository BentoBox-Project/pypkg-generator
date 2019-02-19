# Pypkg Generator
> Create a simple template of a python package.

Create a basic template of python package with a simple command line tool.

## Installation

OS X & Linux:

From PYPI

```sh
$ pip3 install pypkg-generator
```

from the source

```sh
$ git clone https://github.com/dany2691/pypkg-generator.git
$ cd pypkg-generator
$ python3 setup.py install
```

## Usage example

Open a terminal and type:

```sh
$ pkg-generator --help
```

And it'll display:

```sh
Options:
  -n, --name TEXT       The name of the package
  -p, --path TEXT       The path where the package will be created
  --tests / --no-tests  Create test suite directory or not, created by default
  --help                Show this message and exit.
```
There are many options for customization, you can decide what file will be created or not.

You must assign a name, or the project will be name  *forgotten_name*.

```sh
$ pkg-generator --name my-awesome-project
```

You can explicitly pass a path, otherwise, the project will be created in the current directory.

```sh
$ pkg-generator --name my-awesome-project --path /home/user/Documents/
```

# Development setup

This project uses _pipenv_ for dependecy resolution. It's a kind of mix between
pip and virtualenv. Follow the next instructions to setup the development enviroment.

```sh
$ git clone https://github.com/dany2691/pypkg-generator.git
$ cd pypkg-generator
$ pipenv shell
$ pip3 install -e .
```

To run the test-suite, inside the pypkg-generator directory:

```shell
$ pytest -vv test/
```

## Meta

Daniel Omar Vergara Pérez – [@dan1_net](https://twitter.com/dan1_net) – daniel.omar.vergara@gmail.com

[https://github.com/dany2691](https://github.com/dany2691)

## Contributing

1. Fork it (<https://gitlab.com/hexagondata_projects/pypkg-generator>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
