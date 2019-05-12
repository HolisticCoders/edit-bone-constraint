import bpy
from . import sort_bones_by_constraints
from editboneconstraint.constraints import ConstraintManager
from editboneconstraint.bone_mapping import BoneMapping
from uuid import uuid4


def evaluate_graph():
    active_object = bpy.context.view_layer.objects.active
    if (
        active_object
        and active_object.type == "ARMATURE"
        and active_object.mode == "EDIT"
    ):
        armature = active_object.data

        fix_duplicated_bones_uuids(armature)

        sorted_bones = sort_bones_by_constraints(armature)
        for bone in sorted_bones:
            manager = ConstraintManager(bone)
            manager.evaluate()


def auto_evaluate_timer():
    package_name = __package__.split(".")[0]
    prefs = bpy.context.preferences.addons[package_name].preferences

    evaluate_graph()

    return prefs.auto_evaluation_timer


def fix_duplicated_bones_uuids(armature):
    previous_eval_bones = BoneMapping().armature_bones(armature)
    current_eval_bones = [b for b in armature.edit_bones if b.editboneconstraint.uuid]
    new_bones = set(current_eval_bones) - set(previous_eval_bones)
    for bone in new_bones:
        BoneMapping().register_bone(armature, bone)
