import bpy

from editboneconstraint.constraints import instanciate_constraint_from_property


class CreateConstraintOperator(bpy.types.Operator):
    bl_idname = "editbone.createconstraint"
    bl_label = "Create Edit Bone Constraint"
    constraint_type: bpy.props.EnumProperty(
        items=[
            ("ChildOf", "Child Of", "Child Of"),
            ("CopyTransform", "Copy Transform", "Copy Transform"),
            ("CopyLocation", "Copy Location", "Copy Location"),
            ("CopyRotation", "Copy Rotation", "Copy Rotation"),
            ("CopyScale", "Copy Scale", "Copy Scale"),
        ]
    )
    constraint_target: bpy.props.StringProperty()

    def execute(self, context):
        bone = context.selected_bones[0]
        constraint = bone.constraints.add()
        constraint.name = self.constraint_type
        constraint.type = self.constraint_type
        return {"FINISHED"}


class EvaluateEditBoneConstraintsOperator(bpy.types.Operator):
    bl_idname = "editbone.evaluate_edit_bone_constraints"
    bl_label = "Evaluate Edit Bone Constraints"

    @classmethod
    def poll(cls, context):
        return context.object.type == "ARMATURE"

    def execute(self, context):
        armature = context.object.data
        for bone in armature.edit_bones:
            for constraint_prop in bone.constraints:
                constraint = instanciate_constraint_from_property(constraint_prop)
                constraint.evaluate()
        return {"FINISHED"}
