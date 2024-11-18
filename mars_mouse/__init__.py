import sys


def reloadModule(name="mars_mouse", *args):
    """Reload a module and its sub-modules from a given module name.

    Args:
        name (str): Module Name. Default value is "mars_module".

    """

    for mod in sys.modules.copy():
        if mod.startswith(name):
            print(f"Removing module: {mod}")
            del sys.modules[mod]
