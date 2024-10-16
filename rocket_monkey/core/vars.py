import os


customPrefsPath = False
"""为首选项设置一个自定义目录。如果没有找到'rocketPrefs'，将在此文件夹中创建。默认为False"""

relativePath = os.path.dirname(os.path.realpath(__file__)) + os.sep
