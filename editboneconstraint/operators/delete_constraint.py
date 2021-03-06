import bpy
from .base_bone_operator import BaseBoneOperator


class DeleteConstraintOperator(bpy.types.Operator, BaseBoneOperator):
    bl_idname = "editbone.delete_constraint"
    bl_label = "Delete Constraint"
    bl_options = {"INTERNAL", "UNDO"}

    bone_name: bpy.props.StringProperty()
    constraint_name: bpy.props.StringProperty()

    @property
    def bone(self):
        if self.bone_name:
            armature = bpy.context.active_object.data
            return armature.edit_bones[self.bone_name]

    def execute(self, context):
        bone = self.bone
        constraint_index = bone.editboneconstraint.constraints.find(self.constraint_name)
        if bone and constraint_index != -1:
            bone.editboneconstraint.constraints.remove(constraint_index)
        return {"FINISHED"}
