import bpy


class EditBoneConstraint(bpy.types.PropertyGroup):
    type: bpy.props.StringProperty(name="Type")
    target: bpy.props.StringProperty(name="Target")
    bone: bpy.props.StringProperty(name="Bone")

