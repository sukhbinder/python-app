from cookiecutter.main import cookiecutter
import pathlib

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_generated_files(tmpdir):
    generate(
        tmpdir,
        {
            "app_name": "python-foo",
            "description": "blah",
            "entrypoint_name": "hello"
        },
    )
    assert paths(tmpdir) == {'python-foo/.github', 'python-foo/.github/workflows/test.yml', 'python-foo', 'python-foo/LICENSE',
                             'python-foo/README.md', 'python-foo/tests', 'python-foo/python_foo',
                             'python-foo/.github/workflows/publish.yml', 'python-foo/.github/workflows',
                             'python-foo/tests/test_python_foo.py', 'python-foo/python_foo/__init__.py',
                             'python-foo/python_foo/__main__.py','python-foo/python_foo/cli.py',
                             'python-foo/pyproject.toml', 'python-foo/.gitignore','python-foo/.github/workflows'}

def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}
