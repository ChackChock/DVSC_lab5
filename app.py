from button import Button


class App:
    def __init__(self) -> None:
        self.running = True
        self.button = Button([50, 75], [100, 100])

    def start(self) -> None:
        while self.running:
            self.button.update([100, 100])
