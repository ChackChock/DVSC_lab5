class Button:
    def __init__(self, center, size) -> None:
        self.center = center
        self.size = size
        self.hovered = False

    def update(self, mouse_coords, mouse_state) -> None:
        self.hovered = False
        if (
            self.center[0] - self.size[0] / 2
            <= mouse_coords[0]
            <= self.center[0] + self.size[0] / 2
            and self.center[1] - self.size[1] / 2
            <= mouse_coords[1]
            <= self.center[1] + self.size[1] / 2
        ):
            self.hovered = True

        if mouse_state == "pressed" and self.hovered:
            print(f"{self} class <Button> is clicked!")

    def render(self) -> None:
        print(f"{self} class <Button> is drawing")
