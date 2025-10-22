from imaplib import Literal
from typing import Any


def read_data() -> str:
    with open("data.md", "r", encoding="utf-8") as f:
        return f.read()

# 这个函数的返回值,就是刚才输入的文章分块儿之后. 输出的是一个列表
def get_chunks() -> list[str]:
    content: str = read_data()
    chunks: list[str] = content.split('\n\n')  # 当遇到两个回车就切分, 根据不同的文本调整

    # 根据更改, 调整为当遇到#开头, 即为标题或者章节名称时, 归纳为同一段落
    result: list[Any] = []
    header: Literal[''] = ''
    for c in chunks:
        if c.startswith("#"):
            header += f"{c}\n"
        else:
            result.append(f"{header}{c}")
            header: Literal[''] = ''

    return result

if __name__ == '__main__':
    chunks: list[str] = get_chunks()
    for c in chunks:
        print(c)
        print("--------------------")


# 除了手写一个分块函数之外, 网上也有一些现成的分块算法
# 比如说langchain里面的 Recursive Character Text Splitter, 一个更为强大的分块算法

# 分块之后, 需要对文本内容做embedding, 然后存进向量数据库之中
