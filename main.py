"""自动化测试演示模块.

这个模块提供了使用 PyAutoGUI 进行自动化操作的基本功能，
包括屏幕尺寸获取、鼠标移动和键盘输入等操作。
"""

import time
from typing import Tuple

import pyautogui


def get_screen_size() -> Tuple[int, int]:
    """获取屏幕尺寸."""
    return pyautogui.size()


def draw_square(start_x: float, start_y: float, size: float) -> None:
    """画一个正方形.

    Args:
        start_x: 起始x坐标
        start_y: 起始y坐标
        size: 正方形边长
    """
    pyautogui.moveTo(start_x, start_y, duration=1.0)
    for _ in range(4):
        pyautogui.moveRel(size, 0, duration=0.5)
        pyautogui.moveRel(0, size, duration=0.5)
        pyautogui.moveRel(-size, 0, duration=0.5)
        pyautogui.moveRel(0, -size, duration=0.5)


def type_text(text: str, interval: float = 0.1) -> None:
    """模拟键盘输入文字.

    Args:
        text: 要输入的文字
        interval: 每个字符之间的间隔时间
    """
    pyautogui.write(text, interval=interval)
    pyautogui.press("enter")


def main() -> None:
    """主程序入口函数，执行自动化测试演示。."""
    print("程序将在3秒后开始运行...")
    time.sleep(3)

    # 获取屏幕尺寸
    screen_width, screen_height = get_screen_size()
    print(f"屏幕尺寸: {screen_width} x {screen_height}")

    # 画方形
    draw_square(screen_width / 2, screen_height / 2, 200)

    # 输入文字
    type_text("Hello, PyAutoGUI!")


if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    try:
        main()
    except pyautogui.FailSafeException:
        print("程序已停止：触发了 failsafe 机制")
    except Exception as e:
        print(f"发生错误: {str(e)}")
