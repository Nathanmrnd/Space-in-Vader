class GameObject:
    def __init__(self, column: int, line: int) -> None:
        self._column = column
        self._line = line

    def move_up(self) -> None:
        self._line -= 1

    def move_down(self) -> None:
        self._line += 1

    def move_left(self) -> None:
        self._column -= 1

    def move_right(self) -> None:
        self._column += 1

    def is_on_the_left_edge(self) -> bool:
        return self._column == 0

    def is_on_the_right_edge(self) -> bool:
        return self._column == 99

    def is_on_the_up_edge(self) -> bool:

        return self._line == 0

    def is_on_the_down_edge(self) -> bool:
        return self._line == 150
