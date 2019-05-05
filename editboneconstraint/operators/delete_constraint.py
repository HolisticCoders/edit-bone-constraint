import bpy

from editboneconstraint.properties import EditBoneConstraintProperty


class DeleteConstraintOperator(bpy.types.Operator):
    bl_idname = "editbone.delete_constraint"
    bl_label = "Delete Constraint"
    bl_options = {"INTERNAL"}


    def execute(self, context):
        print("Deleting Constraint")
        return {"FINISHED"}
