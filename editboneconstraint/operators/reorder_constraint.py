import bpy

class BaseMoveConstraint(bpy.types.Operator):
    bl_idname = "editbone.base_move_constraint_down"
    bl_label = "Move Constraint Down"
    bl_options = {"INTERNAL", "UNDO"}

    bone_name: bpy.props.StringProperty()
    constraint_name: bpy.props.StringProperty()

    @property
    def bone(self):
        if self.bone_name:
            armature = bpy.context.active_object.data
            return armature.edit_bones[self.bone_name]
    
    def invoke(self, context, event):
        self.is_shift_pressed = event.shift
        self.execute(context)
        return {"RUNNING_MODAL"}


class MoveConstraintDownOperator(BaseMoveConstraint):
    bl_idname = "editbone.move_constraint_down"
    bl_label = "Move Constraint Down"
    bl_options = {"INTERNAL", "UNDO"}

    bone_name: bpy.props.StringProperty()
    constraint_name: bpy.props.StringProperty()

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


class MoveConstraintUpOperator(BaseMoveConstraint):
    bl_idname = "editbone.move_constraint_up"
    bl_label = "Move Constraint Up"
    bl_options = {"INTERNAL", "UNDO"}

    bone_name: bpy.props.StringProperty()
    constraint_name: bpy.props.StringProperty()

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
