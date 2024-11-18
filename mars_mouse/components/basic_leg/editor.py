from functools import partial
import pymel.core as pm

from .guide import Guide
from .rig import Rig

__version__ = "0.0.1"


class Editor:
    def __init__(self):
        self.builder_object = "legGuideBuilder"
        self.window_title = f"Leg Guide Builder v{__version__}"

        self.guide = Guide()
        self.rig = Rig(self.guide)

        self.initUI()

    def initUI(self):
        if pm.window(self.builder_object, q=True, ex=True):
            pm.deleteUI(self.builder_object)

        with pm.window(self.builder_object, title=self.window_title):
            with pm.frameLayout(label="General", marginWidth=10, marginHeight=10):
                with pm.columnLayout(adj=True, rowSpacing=10):
                    pm.button(
                        label="Build Leg Guide", command=partial(self.guide.build)
                    )
                    pm.button(
                        label="Build Leg Rig",
                        command=partial(self.rig.build),
                    )


def showEditor():
    Editor()
