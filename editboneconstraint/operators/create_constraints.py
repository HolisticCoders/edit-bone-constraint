import bpy
from mathutils import Matrix
from editboneconstraint.utils import flatten_matrix


class CreateConstraintOperator(bpy.types.Operator):
    bl_idname = "editbone.create_constraint"
    bl_label = "Create Edit Bone Constraint"
    bl_options = {"INTERNAL"}
    constraint_name = None
    constraint_type = None

    @classmethod
    def poll(cls, context):
        return bool(context.selected_editable_bones)

    def execute(self, context):
        target = context.selected_editable_bones[0]
        bone = context.selected_editable_bones[1]
        constraint = bone.constraints.add()
        constraint.name = self.constraint_name
        constraint.type = self.constraint_type
        constraint.bone = bone.name
        constraint.target = target.name
        return {'FINISHED'}


class CreateCopyTransformConstraintOperator(CreateConstraintOperator):
    bl_idname = "editbone.create_copy_transform_constraint"
    bl_label = "Create Edit Bone Copy Transform Constraint"
    bl_options = set()  # overriding the {"INTERNAL"} of the parent class
    constraint_name = "Copy Transform"
    constraint_type = "CopyTransform"


class CreateChildOfConstraintOperator(CreateConstraintOperator):
    bl_idname = "editbone.createchildofconstraint"
    bl_label = "Create Edit Bone Child Of Constraint"
    bl_options = set()  # overriding the {"INTERNAL"} of the parent class
    constraint_name = "Child Of"
    constraint_type = "ChildOf"


class CreateCopyLocationConstraintOperator(CreateConstraintOperator):
    bl_idname = "editbone.create_copy_location_constraint"
    bl_label = "Create Edit Bone Copy Location Constraint"
    bl_options = set()  # overriding the {"INTERNAL"} of the parent class
    constraint_name = "Copy Location"
    constraint_type = "CopyLocation"


class CreateCopyRotationConstraintOperator(CreateConstraintOperator):
    bl_idname = "editbone.create_copy_rotation_constraint"
    bl_label = "Create Edit Bone Copy Rotation Constraint"
    bl_options = set()  # overriding the {"INTERNAL"} of the parent class
    constraint_name = "Copy Rotation"
    constraint_type = "CopyRotation"


class CreateCopyScaleConstraintOperator(CreateConstraintOperator):
    bl_idname = "editbone.create_copy_scale_constraint"
    bl_label = "Create Edit Bone Copy Scale Constraint"
    bl_options = set()  # overriding the {"INTERNAL"} of the parent class
    constraint_name = "Copy Scale"
    constraint_type = "CopyScale"
