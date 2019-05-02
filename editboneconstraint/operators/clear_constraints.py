import bpy


class ClearConstraintOperator(bpy.types.Operator):
    bl_idname = "editbone.clear_edit_bone_constraints"
    bl_label = "Clear Edit Bone Constraint"

    @classmethod
    def poll(cls, context):
        return bool(context.selected_editable_bones)

    def execute(self, context):
        for bone in context.selected_editable_bones:
            bone.constraints.clear()
        return {"FINISHED"}