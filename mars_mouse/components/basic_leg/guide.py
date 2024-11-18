# -------------------------------------------------------
import pymel.core as pm


class Guide:

    def __init__(self, name="basic_leg", parent=None):
        self.name = name
        self.parent = parent

        self.components = [
            {
                "name": "leg",
                "parent": "",
                "position": [0, 13, 0],
            },
            {
                "name": "knee",
                "parent": "leg",
                "position": [0, 7, 1],
            },
            {
                "name": "ankle",
                "parent": "knee",
                "position": [0, 1, -1],
            },
        ]

    def build(self, *args, **kwargs):
        for index, guide in enumerate(self.components):
            guide_name = guide["name"]
            guide_parent = guide["parent"]
            guide_position = guide["position"]

            guide_node = pm.spaceLocator(name=guide_name)
            guide_node.translate.set(guide_position)

            if index > 0 and guide_parent != "":
                pm.parent(guide_node, self.components[index - 1]["name"])
            elif self.parent is not None and self.parent != "":
                pm.parent(guide_node, self.parent)

        return True

    def serialize(self, *args, **kwargs):
        return {"name": self.name, "components": self.components}

    def deserialize(self, data, *args, **kwargs):
        self.name = data["name"]
        self.parent = data["parent"]
        self.components = data["components"]
