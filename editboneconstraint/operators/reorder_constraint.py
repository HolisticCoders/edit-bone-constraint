import bpy
from .base_bone_operator import BaseBoneOperator

class BaseMoveConstraintOperator(BaseBoneOperator):
    def execute(self, context):
        return {"FINISHED"}

    def invoke(self, context, event):
        self.is_shift_pressed = event.shift
        self.execute(context)
        return {"RUNNING_MODAL"}


class MoveConstraintDownOperator(bpy.types.Operator, BaseMoveConstraintOperator):
    bl_idname = "editbone.move_constraint_down"
    bl_label = "Move Constraint Down"

    def execute(self, context):
        bone = self.bone
        if bone:
            constraint_index = bone.constraints.find(self.constraint_name)
            constraint_count = len(bone.constraints)
            if constraint_index != -1 and constraint_index < constraint_count - 1:
                if self.is_shift_pressed:
                    new_index = constraint_count - 1
                else:
                    new_index = constraint_index + 1
                bone.constraints.move(constraint_index, new_index)

        return {"FINISHED"}


class MoveConstraintUpOperator(bpy.types.Operator, BaseMoveConstraintOperator):
    bl_idname = "editbone.move_constraint_up"
    bl_label = "Move Constraint Up"

    def execute(self, context):
        bone = self.bone
        if bone:
            constraint_index = bone.constraints.find(self.constraint_name)
            if constraint_index != -1 and constraint_index > 0:
                if self.is_shift_pressed:
                    new_index = 0 
                else:
                    new_index = constraint_index - 1
                bone.constraints.move(constraint_index, new_index)

        return {"FINISHED"}
