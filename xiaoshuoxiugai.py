# _*_ coding:utf-8 _*_

# 小说文档处理脚本
# 需求：识别小说文档，整理格式，识别标题,换行,结尾加空格,带图形界面

import os
import argparse
import re
import tkinter as tk
from tkinter.filedialog import *


# 文档处理函数
def modify_text():
    source_file = file_path.get()
    output_file = os.path.join('C://Users', 'lingh', 'Desktop', os.path.split(source_file)[1])
    title_pattern = re.compile(r'\u7B2C?\d+\u7AE0?\s+[\u4E00-\u9FA5]+')  # 形式: 第234章 章节标题
    with open(source_file, 'r', encoding='gbk') as fread:
        with open(output_file, 'w', encoding='gbk') as fwrite:
            while True:
                line_contain = fread.readline()
                match_result = title_pattern.match(line_contain)                 # 章节标题匹配
                if line_contain:
                    if line_contain.isspace():
                        write_contain = ''
                    elif match_result:
                        write_contain = '\n'+line_contain.strip('\n')+'  '+'\n'
                    else:
                        write_contain = line_contain.strip('\n')+'  '+'\n'
                    fwrite.write(write_contain)
                else:
                    break
        fread.close()


def path_select():
    global file_path
    file_path.set(askopenfilename())


window = tk.Tk()
window.title('小说文档处理脚本')
window.geometry('300x400')
# 选择路径窗口
file_path = tk.StringVar()
tk.Label(window, text='文件路径:').grid(row=0,column=0)
tk.Entry(window, textvariable=file_path).grid(row=0,column=1)
tk.Button(window, text='选择文件', command=path_select).grid(row=0, column=3)
# 文档处理窗口部分
tk.Button(window, text='处理文件', command=modify_text).grid(row=1, column=0)
window.mainloop()