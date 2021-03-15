import re
from types import MethodType, FunctionType

import jieba


def clean_txt(raw):
    fil = re.compile(r"[^0-9a-zA-Z\u4e00-\u9fa5]+")
    return fil.sub(' ', raw)

def seg(sentence, sw, apply=None):
    if isinstance(apply, FunctionType) or isinstance(apply, MethodType):
        sentence = apply(sentence)
    return ' '.join([i for i in jieba.cut(sentence) if i.strip() and i not in sw])

def stop_words(stop_words_path):
    with open(stop_words_path, 'r', encoding='utf-8') as swf:
        return [line.strip() for line in swf]


if __name__ == "__main__":
    # 对某个sentence进行处理：
    content = '上海天然橡胶期价周三再创年内新高，主力合约突破21000元/吨重要关口。'
    res = seg(content.lower().replace('\n', ''), stop_words(), apply=clean_txt)
    print(res)