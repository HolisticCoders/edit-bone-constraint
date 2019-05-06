import bpy

class BaseBoneOperator:
    bl_options = {"INTERNAL", "UNDO"}

    bone_name: bpy.props.StringProperty()
    constraint_name: bpy.props.StringProperty()

    @property
    def bone(self):
        if self.bone_name:
            armature = bpy.context.active_object.data
            return armature.edit_bones[self.bone_name]
