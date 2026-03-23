class DepartmentLocation:
    """Represents one physical location of a department."""

    __address: str

    def __init__(self, address: str):
        """Initialize one location with an address."""
        self.__address = address

    def get_address(self) -> str:
        """Return location address."""
        return self.__address

    def set_address(self, address: str) -> None:
        """Update location address."""
        self.__address = address
