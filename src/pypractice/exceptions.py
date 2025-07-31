class BadUserDictError(Exception):
    """Custom exception class to indicate that the dictionary is not correctly formatted to construct a User from"""

    def __init__(self, msg: str | None = None) -> None:
        super().__init__(msg)

    def __str__(self) -> str:
        return (
            "Dictionary passed to User constructor object did not have appropriate keys"
        )
