from button import Button


class App:
    def __init__(self) -> None:
        self.running = True
        self.button = Button()

    def run(self) -> None:
        while self.running:
            self.button.update()
