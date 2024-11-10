import json
import os
from os.path import expanduser

from rocket_monkey.core.vars import customPrefsPath, relativePath


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
    if not os.path.exists(full_path):
        os.makedirs(full_path)

        # 创建用户文件夹
        write_category(full_path + os.sep + "User Actions")
        write_category(full_path + os.sep + "User Actions" + os.sep + "Unsorted")

    return full_path


def validate_json(input):
    try:
        json.dumps(input)
        return True
    except Exception:
        return False


def get_default_script_paths():
    # 用户脚本路径
    user_path = get_prefs_folder() + os.sep + "User Actions" + os.sep
    path_data = [{"name": "User", "path": user_path, "enable": True}]
    # 默认脚本路径
    parentPath = os.path.abspath(os.path.join(relativePath, os.pardir))
    default_path = parentPath + os.sep + "actions" + os.sep
    path_data.append({"name": "Default", "path": default_path, "enabled": True})

    return path_data


def get_settings_path():
    """返回rocket的配置文件的完整路径

    Returns:
        str: rocket的配置文件的完整路径
    """
    return get_prefs_folder() + os.sep + "rocket_settings.json"


def create_settings_file(settings_dict=None):
    # 创建主目录，如果它不存在的话
    if not os.path.exists(get_prefs_folder()):
        os.makedirs(get_prefs_folder())

    if settings_dict is None:
        generic_settings_dict = {
            "alwaysOn": False,
            "listMode": "Latest",
            "mayaCommands": True,
            "noColorMode": True,
            "useRecommendedSearch": True,
            "scriptPath": get_default_script_paths(),
        }
        # 构建完整的字典
        settings_dict = {
            "generic": generic_settings_dict,
            "lists": {
                "Favorites": [],
                "Latest": [],
                "Blacklist": [],
            },
        }

    # 保存配置到文件里面
    output_path = get_settings_path()
    # 保存前验证数据
    status = validate_json(settings_dict)

    if not status:
        print("Error: 保存首选项的问题，json格式不正确")
        return False

    try:
        with open(output_path, "w") as outfile:
            json.dump(settings_dict, outfile, indent=3)
        return True
    except Exception as e:
        print(e)
        return False


def prefs_exists():
    """返回在指定目录下rocket monkey的配置文件的存在状态

    Returns:
        bool: 文件存在为True否则为False
    """
    return os.path.exists(get_settings_path())
