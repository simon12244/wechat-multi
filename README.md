<div align="center">

# 微信多开助手

**一个极简的 Windows 微信多开小工具 · 双击即用**

[![Release](https://img.shields.io/github/v/release/simon12244/wechat-multi?style=flat-square&label=版本)](https://github.com/simon12244/wechat-multi/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/simon12244/wechat-multi/total?style=flat-square&label=下载)](https://github.com/simon12244/wechat-multi/releases)
[![License](https://img.shields.io/github/license/simon12244/wechat-multi?style=flat-square&label=许可)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D4?style=flat-square&logo=windows&logoColor=white)](#下载)

[下载](#下载) · [功能](#功能) · [使用方法](#使用方法) · [常见问题](#常见问题) · [自己编译](#自己编译)

</div>

---

## 这是什么

微信官方客户端默认限制同一台电脑只能运行一个实例。这个小工具用最简单的方式绕开这个限制：
直接多次调用 `WeChat.exe`，从而在一台电脑上同时登录多个微信账号。

- **不需要注入、不需要 hook、不修改微信任何文件**
- 纯 Python 标准库编写，**零第三方依赖**
- 提供打包好的 exe，**不装 Python 也能用**

> 适用场景：一个工作号 + 一个生活号，或多店铺 / 多客服账号同时在线。

---

## 截图

![主界面](https://github.com/user-attachments/assets/4f8b6651-5b91-47a7-a506-8396f77c5f1f)

![使用示意](https://github.com/user-attachments/assets/59f465c7-a79b-45a9-9160-771919a372dc)

---

## 下载

| 方式 | 说明 |
|---|---|
| **[Releases 页面](https://github.com/simon12244/wechat-multi/releases/latest)** | 推荐。下载 `125.exe`，双击即可运行，无需安装 Python |
| [备用网盘链接](https://www.123684.com/s/k6J9jv-dyEuA) | 访问 GitHub 较慢时使用 |
| [源码压缩包](https://github.com/simon12244/wechat-multi/archive/refs/heads/main.zip) | 只有一个 `.py` 文件，可直接审阅和修改 |

`125.exe` 由 PyInstaller 打包，体积约 10 MB，**已包含 Python 运行时**。

---

## 功能

- **一键双开** — 点一下启动第 2 个微信
- **一键三开** — 点一下启动第 3 个微信
- **自定义数量** — 输入 1–20 之间的任意数字
- **自动查找微信** — 自动扫描常见安装位置（C 盘 / D 盘、Program Files、用户目录）
- **找不到就问你** — 无法自动定位时弹出文件选择框，手动指定 `WeChat.exe`
- **输入保护** — 输入空值、字母、小数、0 或负数时给出提示，不会静默失败（v1.0.1 新增）
- **数量上限** — 单次最多 20 个，避免误输入把电脑拖死（v1.0.1 新增）

---

## 使用方法

### 方式一：直接使用打包好的程序（推荐）

1. 从 [Releases](https://github.com/simon12244/wechat-multi/releases/latest) 下载 `125.exe`
2. **先确认微信已完全退出**（托盘图标也要退出，否则只会激活已有窗口）
3. 双击 `125.exe`
4. 点「双开」/「三开」，或在输入框填数量后点「确认」

### 方式二：从源码运行

需要 Python 3.8 或更高版本。`tkinter` 是 Python 标准库，**不需要 pip 安装任何东西**。

```bash
git clone https://github.com/simon12244/wechat-multi.git
cd -
python wechat_multi_open.py
```

> 若提示 `No module named tkinter`（仅部分精简版 Python 才有此问题），
> Windows 官方安装包默认已包含，无需处理。

---

## ⚠️ 重要注意事项

1. **多开前必须先完全退出微信。** 如果已有一个微信在运行，再点「双开」通常只会把已有窗口
   激活到前台，看起来像"没反应"。请从托盘图标右键退出，或用任务管理器结束 `WeChat.exe` 后再操作。
2. **本工具只负责"启动多个实例"，不涉及任何账号安全机制。** 多开的账号行为同样受微信官方
   风控约束，请自行评估账号风险。
3. **请勿用于批量养号、营销群发等违规用途。** 请遵守微信软件许可协议及相关法律法规，
   使用后果由使用者自行承担。
4. 部分微信版本（尤其新版）会对多开做检测，可能出现多开失败或账号需二次验证的情况，
   这属于微信客户端行为，本工具无法干预。
5. 本工具**不读取、不存储、不联网上传**你的任何数据。全部逻辑只有一个文件，可自行审阅。

---

## 常见问题

<details>
<summary><b>点了「双开」没有任何反应？</b></summary>

先确认微信是否已完全退出。微信最小化到托盘时进程仍在运行，此时再启动只会激活已有窗口。

彻底退出的方法：

- 右键点击托盘区的微信图标 → 退出
- 或按 `Ctrl+Shift+Esc` 打开任务管理器，结束所有 `WeChat.exe` 进程

</details>

<details>
<summary><b>提示「未找到微信」怎么办？</b></summary>

工具会自动扫描这些位置：

```
C:\Program Files (x86)\Tencent\WeChat\WeChat.exe
C:\Program Files\Tencent\WeChat\WeChat.exe
D:\Program Files (x86)\Tencent\WeChat\WeChat.exe
D:\Program Files\Tencent\WeChat\WeChat.exe
%LOCALAPPDATA%\Tencent\WeChat\WeChat.exe
```

如果装在其它盘符或自定义目录，在弹窗里手动选择 `WeChat.exe` 即可。

</details>

<details>
<summary><b>微信 4.0 / 新版微信能用吗？</b></summary>

新版微信的可执行文件路径可能变了（例如变成 `Weixin.exe`，或安装在
`C:\Program Files\Tencent\Weixin\`）。此时用弹窗手动选择新的可执行文件即可。
如果新版微信从程序层面禁止了多开，本工具无法绕过。

</details>

<details>
<summary><b>会不会被封号？</b></summary>

本工具不修改客户端、不注入、不 hook，只是多次启动同一个 exe。
但"同一设备多账号同时在线"是否触发风控由微信决定，工具无法保证。
请自行判断风险，建议只用于自己的正常工作 / 生活账号。

</details>

<details>
<summary><b>为什么 exe 有 10 MB？</b></summary>

因为用 PyInstaller 把 Python 运行时一起打包进去了，这样目标电脑不需要装 Python。
如果想更小，可以直接运行源码（需要本机有 Python）。

</details>

<details>
<summary><b>杀毒软件报毒？</b></summary>

PyInstaller 打包的程序被误报是常见现象（打包器本身曾被大量恶意软件使用过）。可以：

- 直接运行源码 `python wechat_multi_open.py`，完全避开 exe
- 或按下方 [自己编译](#自己编译) 一节重新打包一份

</details>

---

## 自己编译

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name 125 wechat_multi_open.py
```

生成的程序在 `dist/125.exe`。

---

## 项目结构

```
.
├── wechat_multi_open.py   # 全部逻辑，单文件
├── README.md              # 本文件
├── CHANGELOG.md           # 版本变更记录
└── LICENSE                # MIT
```

---

## 更新记录

见 [CHANGELOG.md](CHANGELOG.md)。当前版本 **v1.0.1**。

---

## 反馈

有问题或建议，欢迎在 [Issues](https://github.com/simon12244/wechat-multi/issues) 提出。
如果这个工具帮到了你，给个 ⭐ 就是最好的支持。

---

## 许可证

[MIT License](LICENSE) © 2025 simon
