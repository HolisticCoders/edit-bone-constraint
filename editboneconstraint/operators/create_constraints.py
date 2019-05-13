import bpy
from mathutils import Matrix
from editboneconstraint.utils import flatten_matrix
from .base_bone_operator import BaseBoneOperator


class BaseAddConstraint:
    bl_options = {"UNDO"}
    bl_property = "type"
    type: bpy.props.EnumProperty(
        name="Type",
        items=(
            ("CopyLocation", "Copy Location", ""),
            ("CopyRotation", "Copy Rotation", ""),
            ("CopyScale", "Copy Scale", ""),
            ("CopyTransform", "Copy Transform", ""),
            ("ChildOf", "Child Of", ""),
        ),
    )

    def _create_constraint_on_bone(self, bone):
        is_first_constraint = not bone.editboneconstraint.constraints.values()
        if is_first_constraint:
            rest_matrix = bone.matrix.copy() @ Matrix.Scale(bone.length, 4)
            bone.editboneconstraint.rest_matrix = flatten_matrix(rest_matrix)

        constraint = bone.editboneconstraint.constraints.add()
        constraint.bone = bone.name
        constraint.name = self.type
        constraint.type = self.type
        constraint.head_tail = 0.0
        constraint.influence = 1.0

        return constraint

    def invoke(self, context, event):
        context.window_manager.invoke_search_popup(self)
        return {"FINISHED"}


class AddConstraintOperator(bpy.types.Operator, BaseAddConstraint):
    bl_idname = "editbone.constraint_add"
    bl_label = "Add Edit Bone Constraint"

    @classmethod
    def poll(cls, context):
        return bool(context.active_bone)

    def execute(self, context):
        bone = context.active_bone
        self._create_constraint_on_bone(bone)
        return {"FINISHED"}


class AddConstraintWithTargetsOperator(bpy.types.Operator, BaseAddConstraint):
    bl_idname = "editbone.constraint_add_with_targets"
    bl_label = "Add Edit Bone Constraint (With Targets)"

    @classmethod
    def poll(cls, context):
        return len(context.selected_editable_bones) >= 2

    def execute(self, context):
        bone = context.active_bone
        targets = context.selected_editable_bones
        targets.remove(bone)
        for target in targets:
            constraint = self._create_constraint_on_bone(bone)
            constraint.target = target.name

            target_mat_with_scale = target.matrix.copy() @ Matrix.Scale(
                target.length, 4
            )
            bone_mat_with_scale = bone.matrix.copy() @ Matrix.Scale(bone.length, 4)

            constraint.offset = flatten_matrix(
                target_mat_with_scale.inverted() @ bone_mat_with_scale
            )

        return {"FINISHED"}
