import bpy

from editboneconstraint.graph import sort_bones_by_constraints
from editboneconstraint.constraints import instanciate_constraint_from_property


class EvaluateEditBoneConstraintsOperator(bpy.types.Operator):
    bl_idname = "editbone.evaluate_edit_bone_constraints"
    bl_label = "Evaluate Edit Bone Constraints"

    @classmethod
    def poll(cls, context):
        return context.object.type == "ARMATURE"

    def execute(self, context):
        armature = context.object.data
        sorted_bones = sort_bones_by_constraints(armature)
        for bone in sorted_bones:
            for constraint_prop in bone.constraints:
                constraint = instanciate_constraint_from_property(constraint_prop)
                constraint.evaluate()
        return {"FINISHED"}