import bpy
from mathutils import Matrix
from editboneconstraint.utils import flatten_matrix


class CreateCopyTransformConstraintOperator(bpy.types.Operator):
    bl_idname = "editbone.createcopytransformconstraint"
    bl_label = "Create Edit Bone Copy Transform Constraint"

    def execute(self, context):
        target = context.selected_editable_bones[0]
        bone = context.selected_editable_bones[1]
        constraint = bone.constraints.add()
        constraint.name = "Copy Transform"
        constraint.type = "CopyTransform"
        constraint.bone = bone.name
        constraint.target = target.name
        return {"FINISHED"}


class CreateChildOfConstraintOperator(bpy.types.Operator):
    bl_idname = "editbone.createchildofconstraint"
    bl_label = "Create Edit Bone Child Of Constraint"

    def execute(self, context):
        target = context.selected_editable_bones[0]
        bone = context.selected_editable_bones[1]
        constraint = bone.constraints.add()
        constraint.name = "Child Of"
        constraint.type = "ChildOf"
        constraint.bone = bone.name
        constraint.target = target.name

        offset_mat = bone.matrix @ target.matrix.inverted()
        constraint.offset = flatten_matrix(offset_mat)

        return {"FINISHED"}


class CreateCopyLocationConstraintOperator(bpy.types.Operator):
    bl_idname = "editbone.create_copy_location_constraint"
    bl_label = "Create Edit Bone Copy Location Constraint"

    def execute(self, context):
        target = context.selected_editable_bones[0]
        bone = context.selected_editable_bones[1]
        constraint = bone.constraints.add()
        constraint.name = "Copy Location"
        constraint.type = "CopyLocation"
        constraint.bone = bone.name
        constraint.target = target.name
        return {"FINISHED"}
