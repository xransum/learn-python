"""Nox sessions."""
import os
import tempfile
from typing import Any

import nox
from nox.sessions import Session

CONFIG_FILE = "pyproject.toml"
PYTHON_RUNTIMES = ["3.8"]
PYTHON_DEFAULT_RUNTIME = ["3.8"]

package = "learn_python"
locations = "src", "tests"

nox.options.sessions = [
    "tests",
]


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    """Install packages constrained by Poetry's lock file.

    This function is a wrapper for nox.sessions.Session.install. It
    invokes pip to install packages inside of the session's virtualenv.
    Additionally, pip is passed a constraints file generated from
    Poetry's lock file, to ensure that the packages are pinned to the
    versions specified in poetry.lock. This allows you to manage the
    packages as Poetry development dependencies.

    Arguments:
        session: The Session object.
        args: Command-line arguments for pip.
        kwargs: Additional keyword arguments for Session.install.

    """

    constraints_file = os.path.join(session.virtualenv.location, "constraints.txt")
    with tempfile.NamedTemporaryFile(delete=True) as constraints:
        session.run(
            "poetry",
            "export",
            "--with=dev",
            "--format=requirements.txt",
            f"--output={constraints.name}",
            external=True,
        )
        with open(constraints_file, "w") as filtered_constraints:
            with open(constraints.name, "r") as constraints_content:
                for line in constraints_content:
                    if ";" not in line:
                        filtered_constraints.write(line)

        session.install(f"--constraint={constraints_file}", *args, **kwargs)


@nox.session(python=PYTHON_DEFAULT_RUNTIME)
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with=dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        install_with_constraints(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python=PYTHON_RUNTIMES)
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", "--ignore-missing-imports", *args)



@nox.session(python=PYTHON_RUNTIMES)
def tests(session: Session) -> None:
    """Run the test suite."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", "--only=main", external=True)
    install_with_constraints(
        session, "coverage[toml]", "pytest", "pytest-cov", "pytest-mock"
    )
    session.run("pytest", *args)
