from app import App


def start()-> None:
    print("Start!")
    app = App()
    app.run()
    print("End!")


if __name__ == "__main__":
    start()
