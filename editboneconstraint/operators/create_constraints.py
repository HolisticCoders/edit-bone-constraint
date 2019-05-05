import bpy
from mathutils import Matrix
from editboneconstraint.utils import flatten_matrix


# HACK: it seems properties are not properly inherited,
# so we declare it once here and assign it to both classes.
constraint_types = bpy.props.EnumProperty(
    name="Type",
    items=(
        ('CopyLocation', "Copy Location", ""),
        ('CopyRotation', "Copy Rotation", ""),
        ('CopyScale', "Copy Scale", ""),
        ('CopyTransform', "Copy Transform", ""),
        ('ChildOf', "Child Of", ""),
    ),
)



class AddConstraintOperator(bpy.types.Operator):
    bl_idname = "editbone.constraint_add"
    bl_label = "Add Edit Bone Constraint"
    bl_property = "type"

    type: constraint_types

    @classmethod
    def poll(cls, context):
        return bool(context.active_bone)

    def execute(self, context):
        bone = context.active_bone
        self._create_constraint_on_bone(bone)
        return {"FINISHED"}

    def _create_constraint_on_bone(self, bone):
        is_first_constraint = not bone.constraints.values()
        if is_first_constraint:
            bone.initial_matrix = flatten_matrix(bone.matrix)
            bone.initial_length = bone.length

        constraint = bone.constraints.add()
        constraint.name = self.type
        constraint.type = self.type
        constraint.bone = bone.name
        constraint.head_tail = 0.0
        constraint.influence = 1.0

        return constraint


class AddConstraintWithTargetsOperator(AddConstraintOperator):
    bl_idname = "editbone.constraint_add_with_targets"
    bl_label = "Add Edit Bone Constraint (With Targets)"

    type: constraint_types

    @classmethod
    def poll(cls, context):
        return len(context.selected_editable_bones) >= 2

    def execute(self, context):
        bone = context.selected_editable_bones[1]
        constraint = self._create_constraint_on_bone(bone)
        target = context.selected_editable_bones[0]
        constraint.target = target.name
        constraint.offset = flatten_matrix(target.matrix.inverted() @ bone.matrix)
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.invoke_search_popup(self)
        return {'RUNNING_MODAL'}
