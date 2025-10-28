from __future__ import annotations
import subprocess
import sys
import typer

app = typer.Typer(help="Mini Automation Framework Runner")

def _run_pytest(args: list[str]) -> int:
    proc = subprocess.run([sys.executable, "-m", "pytest", *args])
    return proc.returncode

@app.command()
def ui() -> None:
    raise SystemExit(_run_pytest(["tests/ui"]))

@app.command()
def api() -> None:
    raise SystemExit(_run_pytest(["tests/api"]))

@app.command()
def all() -> None:
    raise SystemExit(_run_pytest(["tests"]))

if __name__ == "__main__":
    app()
