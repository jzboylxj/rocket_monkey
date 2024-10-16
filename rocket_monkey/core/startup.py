# 启动rocket monkey的主模块
import sys

try:
    sys.path.append("E:\\Works\\python\\HackProjects\\rocket_monkey")
except Exception:
    pass


from rocket_monkey.core import prefs


def start():
    """显示rocket monkey的窗口，如果没有找到首选项文件，创建它并显示教程窗口"""

    # 检查首选项的状态
    if prefs.prefs_exists():
        pass
    else:
        # existing_user = False
        prefs.create_settings_file()


if __name__ == "__main__":

    start()
