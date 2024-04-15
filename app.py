from button import Button


class App:
    def __init__(self) -> None:
        self.running = True
        self.button1 = Button([50, 75], [100, 100])
        self.button2 = Button([50, 75], [100, 100])

    def run(self) -> None:
        while self.running:
            self.button1.update([100, 100])
            self.button2.update([100, 100])
