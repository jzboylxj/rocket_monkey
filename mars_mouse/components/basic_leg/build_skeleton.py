import pymel.core as pm


def build_skeleton(components, name="SKIN"):
    list_joint = []
    pm.select(cl=True)
    for component in components:
        print(f"{component=}")
        list_joint.append(
            pm.joint(
                name=f"{component['name']}_{name}_JNT",
                position=component["position"],
            )
        )
    return list_joint
