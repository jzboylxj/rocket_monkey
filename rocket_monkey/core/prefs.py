import os
from os.path import expanduser

from rocket_monkey.core.vars import customPrefsPath


def get_prefs_folder():
    # 获取用户的主文件夹
    path = expanduser("~")
    if customPrefsPath is not False:
        # 检查路径是否有效
        if os.path.isdir(customPrefsPath):
            path = customPrefsPath
        else:
            print("Error: 找不到自定义首选项路径，返回到默认路径")
            print(f"Path: {customPrefsPath}")

    full_path = path + os.sep + "rocketPrefs"
    # 如果配置文件夹不在就创建它
    if os.path.exists(full_path):
        os.makedirs(full_path)

        # 创建用户文件夹
        write_category(full_path + os.sep + "User Actions")
        write_category(full_path + os.sep + "User Actions" + os.sep + "Unsorted")

    return full_path


def get_settings_path():
    """返回rocket的配置文件的完整路径

    Returns:
        str: rocket的配置文件的完整路径
    """
    return get_prefs_folder() + os.sep + "rocket_settings.json"


def prefs_exists():
    """返回在指定目录下rocket monkey的配置文件的存在状态

    Returns:
        bool: 文件存在为True否则为False
    """
    return os.path.exists(get_settings_path())
