# -*- coding: utf-8 -*-
"""
微信多开助手
============

一个极简的 Windows GUI 小工具，用于一次性启动多个微信实例。

作者  : simon
邮箱  : scoln@foxmail.com
许可  : MIT License
"""

import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox   # 必须显式导入：不能依赖 filedialog 的导入副作用

__version__ = "1.0.1"
__author__ = "simon"
__license__ = "MIT"

# 允许一次启动的最大实例数（防止误输入天文数字把电脑拖死）
MAX_COUNT = 20

# 常见微信安装路径
WECHAT_CANDIDATES = [
    r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",
    r"C:\Program Files\Tencent\WeChat\WeChat.exe",
    r"D:\Program Files (x86)\Tencent\WeChat\WeChat.exe",
    r"D:\Program Files\Tencent\WeChat\WeChat.exe",
    os.path.expanduser(r"~\AppData\Local\Tencent\WeChat\WeChat.exe"),
]


def find_wechat_path(parent=None):
    """按常见路径查找微信，找不到则让用户手动选择。返回路径或空字符串。"""
    for path in WECHAT_CANDIDATES:
        if os.path.exists(path):
            return path

    # 都没找到，让用户自己选
    messagebox.showinfo(
        "未找到微信",
        "没有在常见位置找到微信程序。\n\n"
        "接下来请手动选择 WeChat.exe（通常位于\n"
        "C:\\Program Files (x86)\\Tencent\\WeChat\\ 目录下）。",
        parent=parent,
    )
    path = filedialog.askopenfilename(
        title="请选择微信安装路径（WeChat.exe）",
        filetypes=[("微信程序", "WeChat.exe"), ("可执行文件", "*.exe"), ("所有文件", "*.*")],
        parent=parent,
    )
    return path or ""


def open_wechat(count, parent=None):
    """启动 count 个微信实例。返回实际启动的数量，失败返回 0。"""
    # 入口再做一次保护，避免被其它调用方式绕过校验
    if not isinstance(count, int) or count < 1:
        messagebox.showwarning("数量不对", "启动数量需要是大于 0 的整数。", parent=parent)
        return 0

    if count > MAX_COUNT:
        messagebox.showwarning(
            "数量过多",
            "一次最多启动 %d 个，已按 %d 个处理。\n（防止误输入把电脑拖慢）" % (MAX_COUNT, MAX_COUNT),
            parent=parent,
        )
        count = MAX_COUNT

    wechat_path = find_wechat_path(parent)
    if not wechat_path:
        messagebox.showerror("错误", "未选择微信程序，已取消。", parent=parent)
        return 0
    if not os.path.exists(wechat_path):
        messagebox.showerror("错误", "这个路径不存在：\n%s" % wechat_path, parent=parent)
        return 0

    started = 0
    for _ in range(count):
        try:
            os.startfile(wechat_path)
            started += 1
        except OSError as exc:
            messagebox.showerror("启动失败", "启动微信时出错：\n%s" % exc, parent=parent)
            break

    if started:
        messagebox.showinfo(
            "完成",
            "已启动 %d 个微信实例。\n\n如果只出现了 1 个，请确认启动前微信完全退出了。" % started,
            parent=parent,
        )
    return started


def parse_count(text):
    """把输入框内容解析为正整数。不合法时返回 None（不抛异常）。"""
    text = (text or "").strip()
    if not text:
        return None
    try:
        value = int(text)
    except ValueError:
        return None
    if value < 1:
        return None
    return value


def main():
    root = tk.Tk()
    root.title("微信多开助手 v%s" % __version__)
    root.resizable(False, False)

    # 居中显示
    root.update_idletasks()
    width, height = 400, 160
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 3
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    frame = tk.Frame(root, padx=16, pady=14)
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text="选择要启动的微信数量：", font=("Microsoft YaHei UI", 11)).grid(
        row=0, column=0, columnspan=4, pady=(0, 12)
    )

    entry = tk.Entry(frame, width=6, justify="center", font=("Consolas", 11))
    entry.insert(0, "2")

    def on_confirm():
        count = parse_count(entry.get())
        if count is None:
            messagebox.showwarning(
                "请输入数字",
                "请输入一个大于 0 的整数，例如 2、3、5。",
                parent=root,
            )
            entry.focus_set()
            entry.select_range(0, "end")
            return
        open_wechat(count, parent=root)

    tk.Button(frame, text="双开", width=8, command=lambda: open_wechat(2, parent=root)).grid(
        row=1, column=0, padx=4
    )
    tk.Button(frame, text="三开", width=8, command=lambda: open_wechat(3, parent=root)).grid(
        row=1, column=1, padx=4
    )
    entry.grid(row=1, column=2, padx=4)
    tk.Button(frame, text="确认", width=8, command=on_confirm).grid(row=1, column=3, padx=4)

    tk.Label(
        frame,
        text="注意：多开前请确认微信已完全退出，否则只会激活已有窗口。",
        fg="#c0392b",
        font=("Microsoft YaHei UI", 9),
    ).grid(row=2, column=0, columnspan=4, pady=(14, 0))

    entry.focus_set()
    root.bind("<Return>", lambda _e: on_confirm())
    root.mainloop()


if __name__ == "__main__":
    main()
