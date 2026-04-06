def read_text(prompt: str) -> str:
    """Read one text input."""
    return input(prompt)


def read_menu_option(prompt: str = "Elija una opción: ") -> tuple[int | None, str | None]:
    """Read menu option and convert it to integer."""
    try:
        return int(input(prompt).strip()), None
    except ValueError:
        return None, "La opción debe ser numérica."


def print_success(message: str) -> None:
    """Print success message."""
    print(message)


def print_error(message: str | None) -> None:
    """Print standardized error message."""
    print(f"Error: {message if message else 'Error desconocido.'}")


def print_section(title: str) -> None:
    """Print one menu section header."""
    print(f"\n=== {title} ===")
