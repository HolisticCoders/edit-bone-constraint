import bpy


class EditBoneConstraintProperty(bpy.types.PropertyGroup):
    type: bpy.props.StringProperty(name="Type")
    target: bpy.props.StringProperty(name="Target")
    bone: bpy.props.StringProperty(name="Bone")
    influence: bpy.props.FloatProperty(name="Influence", default=1.0, min=0.0, max=1.0)
    head_tail: bpy.props.FloatProperty(name="Head/Tail", default=0.0, min=0.0, max=1.0)

    offset: bpy.props.FloatVectorProperty(name="Offset", size=16, subtype="MATRIX")
    initial_matrix: bpy.props.FloatVectorProperty(name="Original Matrix", size=16, subtype="MATRIX")
    initial_length: bpy.props.FloatProperty(name="Initial Length")