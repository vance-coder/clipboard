import time
import pyperclip

from utils.parser import parse_url
from utils.beautify import beautify_json


class Clipboard:

    def __init__(self):
        self.data = []
        self.top = None
        self.max_len = 20

    def run(self):
        while True:
            text = pyperclip.paste()

            if text and text != self.top:
                self.try_parse(text)

                self.top = text
                self.data.insert(0, text)

                if len(self.data) > self.max_len:
                    self.data.pop()

            time.sleep(0.1)

    def try_parse(self, stg: str):
        ret = parse_url(stg)

        if ret:
            print(beautify_json(ret))


if __name__ == '__main__':
    cb = Clipboard()
    cb.run()

    # 可能的文档变形、
    # pandas
    # 可以根据网上的工具来看看做啥功能哈哈
    # 判断url，url转字典？
    # 字典转json
    # 格式化输出

