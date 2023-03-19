import time
import chardet
import pyperclip

from utils.parser import parse_url, date_parse, to_list
from utils.beautify import beautify_json
from utils.reformat import remove_blank_line


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

                coding_obj = chardet.detect(text.encode())
                if coding_obj['encoding'] == 'ascii':
                    print(text.encode().decode('unicode_escape'))

                self.top = text
                self.data.insert(0, text)

                if len(self.data) > self.max_len:
                    self.data.pop()

            time.sleep(0.1)

    def try_parse(self, stg: str):
        ret = parse_url(stg)
        if ret:
            print(beautify_json(ret))

        ret = date_parse(stg)
        if ret:
            print(str(ret))

        ret = to_list(stg)
        if ret:
            print(ret)

        ret = remove_blank_line(stg)
        if ret != stg:
            print(ret)

    def move(self, start: int):
        pass


if __name__ == '__main__':
    cb = Clipboard()
    cb.run()

    # 可能的文档变形
    # 可以根据网上的工具来看看做啥功能哈哈

    # 编码转换? unicode等
    # 日期
    # list，缩进的话可以转dict （init_data里面权限设计）
    # 去重
    # fixme 去空行, 一般是能转list的才会去空行吧，其他不去空行。
    # 字典合并
    # 如何快速删除二维列表中的某一列？
    import codecs
    # 2023/06/12
    # 2023/06/12
    # 去行号
    #

