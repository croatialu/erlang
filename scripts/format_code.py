"""代码格式化工具."""

import subprocess
import sys
from typing import List, Optional


def run_command(command: List[str], capture: bool = True) -> bool:
    """运行命令并返回是否成功。."""
    try:
        if capture:
            subprocess.run(  # noqa: S603
                command, check=True, capture_output=True, text=True, shell=False
            )
        else:
            subprocess.run(command, check=True, shell=False)  # noqa: S603
        return True
    except subprocess.CalledProcessError as e:
        if capture:
            print(f"命令执行失败: {' '.join(command)}")
            print(f"错误输出: {e.stderr}")
        return False


def lint_code() -> int:
    """运行代码检查工具。.

    Returns:
        int: 0 表示成功，1 表示失败
    """
    print("开始代码检查...")

    # 使用 ruff 检查代码
    if not run_command(["ruff", "check", "."], capture=False):
        print("代码检查失败！")
        return 1

    print("代码检查通过！")
    return 0


def format_code() -> Optional[str]:
    """运行代码格式化工具."""
    print("开始格式化代码...")

    # 使用 ruff format 替代 black
    if not run_command(["ruff", "format", "."]):
        return "Ruff 格式化失败"
    print("代码格式化完成！")
    return None


def main() -> int:
    """主程序入口函数，执行代码格式化。."""
    error = format_code()
    if error:
        print(f"错误: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
