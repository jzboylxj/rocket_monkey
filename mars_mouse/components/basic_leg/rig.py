from ...rig_funcs import build_skeleton


class Rig:
    def __init__(self, guide):
        self.guide = guide

        self.bind_joints = []
        self.fk_joints = []
        self.ik_joints = []

    def build(self, *args, **kwargs):
        self.dict_guide = self.guide.serialize()

        components = self.dict_guide["components"]
        self.bind_joints = build_skeleton(components, "SKIN")
        self.fk_joints = build_skeleton(components, "FK")
        self.ik_joints = build_skeleton(components, "IK")

        return
