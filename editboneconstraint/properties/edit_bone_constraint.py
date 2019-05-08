import bpy
import re


unique_names = ["name"]


class EditBoneConstraintProperty(bpy.types.PropertyGroup):
    type: bpy.props.StringProperty(name="Type")
    target: bpy.props.StringProperty(name="Target")
    bone: bpy.props.StringProperty(name="Bone")
    influence: bpy.props.FloatProperty(name="Influence", default=1.0, min=0.0, max=1.0)
    mute: bpy.props.BoolProperty(name="Mute", default=False)
    show_expanded: bpy.props.BoolProperty(name="Show Expanded", default=True)
    head_tail: bpy.props.FloatProperty(name="Head/Tail", default=0.0, min=0.0, max=1.0)
    offset: bpy.props.FloatVectorProperty(name="Offset", size=16, subtype="MATRIX")

    def __setattr__(self, name, value):
        def new_val(stem, nbr):
            # simply for formatting
            return "{st}.{nbr:03d}".format(st=stem, nbr=nbr)

        if name not in unique_names:
            # don't want to handle
            self[name] = value
            return
        if value == getattr(self, name):
            # check for assignement of current value
            return

        armature = self.id_data
        bone = armature.edit_bones[self.bone]
        coll = bone.constraints
        if value not in coll:
            # if value is not in the collection, just assign
            self[name] = value
            return

        # see if value is already in a format like 'name.012'
        match = re.match("(.*)\.(\d{3,})", value)
        if match is None:
            stem, nbr = value, 1
        else:
            stem, nbr = match.groups()

        # check for each value if in collection
        new_value = new_val(stem, nbr)
        while new_value in coll:
            nbr += 1
            new_value = new_val(stem, nbr)
        self[name] = new_value
