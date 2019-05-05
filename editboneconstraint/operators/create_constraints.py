import bpy
from mathutils import Matrix
from editboneconstraint.utils import flatten_matrix


class AddConstraintOperator(bpy.types.Operator):
    bl_idname = "editbone.constraint_add"
    bl_label = "Add Edit Bone Constraint"
    bl_property= "type"

    type: bpy.props.EnumProperty(
        name="Type",
        items=(
            ('CopyLocation', "Copy Location", ""),
            ('CopyRotation', "Copy Rotation", ""),
            # ('CopyScale', "Copy Scale", ""),
            ('CopyTransform', "Copy Transform", ""),
            ('ChildOf', "Child Of", ""),
        ),
    )

    @classmethod
    def poll(cls, context):
        return bool(context.selected_editable_bones)

    def execute(self, context):
        bone = context.active_bone
        constraint = bone.constraints.add()
        constraint.name = self.type
        constraint.type = self.type
        constraint.bone = bone.name
        constraint.head_tail = 0.0
        constraint.influence = 1.0
        return {"FINISHED"}


class AddConstraintWithTargetsOperator(bpy.types.Operator):
    bl_idname = "editbone.constraint_add_with_targets"
    bl_label = "Add Edit Bone Constraint (With Targets)"
    bl_property= "type"

    type: bpy.props.EnumProperty(
        name="Type",
        items=(
            ('CopyLocation', "Copy Location", ""),
            ('CopyRotation', "Copy Rotation", ""),
            # ('CopyScale', "Copy Scale", ""),
            ('CopyTransform', "Copy Transform", ""),
            ('ChildOf', "Child Of", ""),
        ),
    )

    @classmethod
    def poll(cls, context):
        return bool(context.selected_editable_bones)

    def execute(self, context):
        target = context.selected_editable_bones[0]
        bone = context.selected_editable_bones[1]
        constraint = bone.constraints.add()
        constraint.name = self.type
        constraint.type = self.type
        constraint.bone = bone.name
        constraint.target = target.name
        constraint.head_tail = 0.0
        constraint.influence = 1.0
        constraint.offset = flatten_matrix(target.matrix.inverted() @ bone.matrix)
        return {"FINISHED"}
    
    def invoke(self, context, event):
        context.window_manager.invoke_search_popup(self)
        return {'RUNNING_MODAL'}
