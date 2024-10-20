# python-app cookiecutter template

Cookiecutter template for creating new Python command-line tools.

Use this template on your own machine with cookiecutter.

## Installation

You'll need to have [cookiecutter](https://cookiecutter.readthedocs.io/) installed. I recommend pipx for this:
```bash
pipx install cookiecutter
```
Regular `pip` will work OK too.

## Examples

Three examples of tools that were initially created using this template:

- [meet](https://github.com/sukhbinder/meet): A comand-line utility for taking setting outlook meetings from cli
- [cronzy](https://github.com/sukhbinder/cronzy: A crontab implementation to for windows and simple text interface
- [pyscheduler](https://github.com/sukhbinder/pyscheduler:  Tools for accessing scheduler via cli

## Usage

Run `cookiecutter gh:sukhbinder/python-app` and then answer the prompts. Here's an example run:
```
$ cookiecutter gh:sukhbinder/python-app
app_name []: python app template demo
description []: Demonstrating https://github.com/sukhbinder/python-app
hyphenated [python-app-template-demo]:
underscored [python_app_template_demo]:
github_username []: sukhbinder
author_name []: Sukhbinder Singh
```
I strongly recommend accepting the suggested value for "hyphenated" and "underscored" by hitting enter on those prompts.

This will create a directory called `python-app-template-demo` - the tool name you enter is converted to lowercase and uses hyphens instead of spaces.

See https://github.com/sukhbinder/python-app-template-demo for the output of this example.

## Developing your command-line tool

Having created the new structure from the template, here's how to start working on the tool.

If your tool is called `my-new-tool`, you can start working on it like so:
```bash
cd my-new-tool
# Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate
# Install dependencies so you can edit the project:
pip install -e '.[test]'
# With zsh you have to run this again for some reason:
source venv/bin/activate
# Confirm your tool can be run from the command-line
my-new-tool --version
```
You should see the following:
```bash
my-new-tool, version 0.1
```
You can run the default test for your tool like so:
```bash
python -m pytest
```
This will execute the test in `tests/test_my_new_tool.py`.

Now you can open the `my_new_tool/cli.py` file and start adding python [commands and groups](https://python.palletsprojects.com/en/7.x/commands/).

## Creating a Git repository for your tool

You can initialize a Git repository for your tool like this:
```bash
cd my-new-tool
git init
git add .
git commit -m "Initial structure from template"
# Rename the 'master' branch to 'main':
git branch -m master main
```
## Publishing your tool to GitHub

Use https://github.com/new to create a new GitHub repository sharing the same name as your tool, which should be something like `my-new-tool`.

Push your `main` branch to GitHub like this:
```bash
git remote add origin git@github.com:YOURNAME/my-new-tool.git
git push -u origin main
```
The template will have created a GitHub Action which runs your tool's test suite against every commit.

## Publishing your tool as a package to PyPI

The template also includes a `publish.yml` GitHub Actions workflow for publishing packages to [PyPI](https://pypi.org/), using [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish).

To use this action, you need to create a PyPI account and [configure a Trusted Publisher](https://til.sukhbinderillison.net/pypi/pypi-releases-from-github) for this package.

Once you have created your account, navigate to https://pypi.org/manage/account/publishing/ and create a "pending publisher" for the package. Use the following values:

- **PyPI Project Name:** The name of your package
- **Owner:** Your GitHub username or organization - the "foo" in `github.com/foo/bar`
- **Repsitory name:** The name of your repository - the "bar" in `github.com/foo/bar`
- **Workflow name:** `publish.yml`
- **Environment name:** `release`

Now, any time you create a new "Release" on GitHub the Action will build your package and push it to PyPI.

The tag for your release needs to match the `VERSION` string at the top of your `pyproject.toml` file. You should bump this version any time you release a new version of your package.
