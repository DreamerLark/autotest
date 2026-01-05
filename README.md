# Playwright UI Click Tests (Python)

这是一个最小的 Python 示例项目：使用 **Playwright** 对“界面”进行自动化 **点击** 测试（基于 `pytest`）。

## 目录结构

- `ui_click_tests/`：示例代码（内置一段 HTML 页面，用于演示点击交互）
- `tests/`：自动化测试用例（点击按钮、勾选复选框等）

## 环境要求

- Python >= 3.10

## 安装

```bash
python -m venv .venv
source .venv/bin/activate

pip install -e ".[test]"
python -m playwright install chromium
```

> 说明：Playwright 需要安装浏览器（如 chromium）。如果你在 CI 环境中运行，请确保相应步骤已执行。

## 运行测试

```bash
pytest
```

如果当前环境没有安装 Playwright 浏览器，测试会自动 `skip`（避免因为缺少浏览器导致整体失败）。

## 运行一个可视化 Demo（可选）

```bash
python -m ui_click_tests.run_demo
```

该命令会打开一个浏览器窗口，加载内置页面并执行几次点击操作，方便直观看到效果。
