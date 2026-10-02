# 更新记录

本项目的所有重要变更都记录在此文件。

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [1.0.1] - 2026-10-02

### 修复

- **输入框非法内容会导致界面无响应**：原代码直接执行 `int(entry.get())`，
  当输入为空、纯空格、字母或小数时会抛出 `ValueError`。Tkinter 的事件回调不会捕获异常，
  表现为"点确认没反应、控制台报错"。现在改为 `parse_count()` 安全解析，非法输入会弹窗提示并选中输入框。
- **数量没有边界检查**：原来输入 `0` 或负数会静默什么都不做，输入超大数字会尝试启动同样多次。
  现在统一校验为大于 0，并且单次上限 20 个（超出会提示并按上限处理）。
- **显式导入 `messagebox`**：原代码使用 `tk.messagebox` 但只导入了 `filedialog`。
  当前能工作是因为 `filedialog` 会连带导入 `simpledialog` 与 `messagebox` 并挂到 `tkinter` 包上，
  这属于依赖导入副作用，不同 Python 版本可能失效。现已改为显式 `from tkinter import messagebox`。
- **路径有效性校验**：用户手动选择的路径会先检查是否存在，不存在时给出明确提示而不是 `startfile` 报错。
- **启动失败有反馈**：`os.startfile` 抛出的 `OSError` 会被捕获并提示，不再静默中断。

### 新增

- 启动成功后有完成提示，告知实际启动了几个实例。
- 支持在输入框按 `Enter` 直接确认。
- 窗口自动居中、禁止拉伸，按钮列对齐。
- 单文件顶部补充模块说明与 `__version__` / `__author__` / `__license__` 元信息。

### 变更

- 界面提示文字调整，明确告知"多开前需完全退出微信"。

## [1.0.0] - 2025-05-10

### 新增

- 首个版本。
- 一键双开、三开微信。
- 支持自定义启动数量。
- 自动扫描常见微信安装路径；找不到时弹出文件选择框手动指定。
- 使用 PyInstaller 打包为单文件 `125.exe`，无需安装 Python 即可运行。

[1.0.1]: https://github.com/simon12244/-/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/simon12244/-/releases/tag/v1.0.0
