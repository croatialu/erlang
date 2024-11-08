# Erlang

一个基于 Python 的自动化工具项目。

## 技术栈

- Python 3.13+
- Poetry（包管理）
- PyAutoGUI（自动化控制）
- 代码质量工具链

## 开始使用

### 环境要求

- Python 3.13 或更高版本
- Poetry 包管理器

### 安装

1. 克隆项目
``` bash
git clone [项目地址]
cd erlang
```

2. 安装依赖
``` bash
poetry install
```

## 开发指南

### 可用命令

```bash
# 运行项目
poetry run start

# 运行测试
poetry run test

# 类型检查
poetry run type-check

# 代码格式化
poetry run format

# 代码检查
poetry run lint
```

### 代码规范

本项目使用严格的代码质量控制工具链：

- **Ruff**: 快速的 Python linter 和格式化工具
  - 行长度限制：88 字符
  - Python 目标版本：3.8+
  - 启用规则包括：
    - pycodestyle (E)
    - pyflakes (F)
    - isort (I)
    - flake8-bugbear (B)
    - 等...

- **Black**: 代码格式化
  - 行长度：88 字符
  - 目标 Python 版本：3.8+

- **isort**: import 语句排序
  - 配置与 Black 兼容

- **mypy**: 静态类型检查

- **codespell**: 拼写检查

### Git 提交规范

项目使用 Commitizen 进行提交信息规范化：

- 提交格式遵循 Conventional Commits
- 版本号格式：v0.1.0
- 使用彩色提交提示界面

提交代码时推荐使用：
```bash
git add .
git commit
```

### 预提交检查

项目配置了 pre-commit 钩子，在提交前会自动运行代码检查：

```bash
# 手动运行检查
pre-commit run --all-files
```

## 项目结构

```
erlang/
├── README.md
├── pyproject.toml    # 项目配置
├── main.py          # 主入口
└── tests/           # 测试目录
```

## 许可证
MIT

## 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request
```
