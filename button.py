class Button:
    def __init__(self, center, size) -> None:
        self.center = center
        self.size = size

    def update(self, mouse_coords) -> None:
        if (
            self.center[0] - self.size[0] / 2
            <= mouse_coords[0]
            <= self.center[0] + self.size[0] / 2
            and self.center[1] - self.size[1] / 2
            <= mouse_coords[1]
            <= self.center[1] + self.size[1] / 2
        ):
            print("mouse in")

    def render(self) -> None:
        print(f"{self} is drowing")
