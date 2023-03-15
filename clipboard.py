import time
import pyperclip


class Clipboard:

    def __init__(self):
        self.data = []
        self.top = None

    def run(self):
        while True:
            text = pyperclip.paste()
            if text and text != self.top:
                self.top = text
                self.data.insert(0, text)
                print(self.data)
            time.sleep(0.2)


if __name__ == '__main__':
    cb = Clipboard()
    cb.run()

