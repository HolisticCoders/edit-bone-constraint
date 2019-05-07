import bpy
from . import sort_bones_by_constraints
from editboneconstraint.constraints import ConstraintManager


def evaluate_graph():
    active_object = bpy.context.view_layer.objects.active
    if (
        active_object
        and active_object.type == "ARMATURE"
        and active_object.mode == "EDIT"
    ):
        armature = active_object.data
        sorted_bones = sort_bones_by_constraints(armature)
        for bone in sorted_bones:
            manager = ConstraintManager(bone)
            manager.evaluate()


def auto_evaluate_timer():
    package_name = __package__.split(".")[0]
    prefs = bpy.context.preferences.addons[package_name].preferences

    evaluate_graph()

    return prefs.auto_evaluation_timer
