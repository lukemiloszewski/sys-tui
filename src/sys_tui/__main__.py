import typer


app = typer.Typer()


@app.command()
def main() -> None:
    """sys_tui."""


if __name__ == "__main__":
    app(prog_name="sys-tui")  # pragma: no cover
