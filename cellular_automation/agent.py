class Agent:
    def __init__(self,
                 automation: 'Automation',
                 row: int,
                 col: int,
                 *args, **kwargs):
        self._automation = automation
        self._row = row
        self._col = col
