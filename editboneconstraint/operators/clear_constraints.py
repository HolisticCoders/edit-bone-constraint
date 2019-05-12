import bpy


class ClearConstraintsOperator(bpy.types.Operator):
    bl_idname = "editbone.clear_constraints"
    bl_label = "Clear Edit Bone Constraints"
    bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return bool(context.selected_editable_bones)

    def execute(self, context):
        for bone in context.selected_editable_bones:
            bone.editboneconstraint.constraints.clear()
        return {"FINISHED"}
