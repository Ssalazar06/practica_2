class Specialization:
    """Represents one engineer specialty."""

    __name: str

    def __init__(self, name: str):
        """Initialize specialty with name."""
        self.__name = name

    def get_name(self) -> str:
        """Return specialty name."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Update specialty name."""
        self.__name = name
