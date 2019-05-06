import bpy


class MoveConstraintDownOperator(bpy.types.Operator):
    bl_idname = "editbone.move_constraint_down"
    bl_options = {"INTERNAL", "UNDO"}

    def execute(self, context):
        print("Moving Constraint Down")
        return {"FINISHED"}


class MoveConstraintUpOperator(bpy.types.Operator):
    bl_idname = "editbone.move_constraint_up"
    bl_options = {"INTERNAL", "UNDO"}

    def execute(self, context):
        print("Moving Constraint Up")
        return {"FINISHED"}
