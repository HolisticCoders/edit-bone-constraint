import bpy


class EditBoneConstraintProperty(bpy.types.PropertyGroup):
    type: bpy.props.StringProperty(name="Type")
    target: bpy.props.StringProperty(name="Target")
    bone: bpy.props.StringProperty(name="Bone")
    offset: bpy.props.FloatVectorProperty(name="Offset", size=16, subtype="MATRIX")
