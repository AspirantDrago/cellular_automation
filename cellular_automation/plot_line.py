class PlotLine:
    COLORS = 'bgrcmykw'
    _count_lines = 0

    def __init__(self, status):
        self._status: int = status
        self._arr: list[int] = []
        PlotLine._count_lines += 1
        self._color: str = self.COLORS[
            PlotLine._count_lines % len(self.COLORS)
        ]
        self._name: str | None = None
        self._visible: bool = True

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, value: bool) -> None:
        self._visible = value

    @property
    def status(self):
        return self._status

    def append(self, value: int):
        self._arr.append(value)

    def __getitem__(self, index: int) -> int:
        if index >= 0:
            raise IndexError('index must be negative')
        if index < -len(self._arr):
            return 0
        return self._arr[index]

    @property
    def color(self):
        return self._color

    def __str__(self) -> str:
        if self._name is not None:
            return self._name
        return f'Agent {self._status}'

    def get_last(self, count: int) -> list[int]:
        return [self[i] for i in range(-count, 0)]

    @color.setter
    def color(self, value: str) -> None:
        self._color = value

    def set_name(self, name: str | None) -> None:
        self._name = name
