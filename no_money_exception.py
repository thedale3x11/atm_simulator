class NoMoneyError(Exception):
    def __init__(self) -> None:
        self.message="No enough money."
        super().__init__(self.message)