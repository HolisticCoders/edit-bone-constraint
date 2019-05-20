import bpy
import logging
from . import sort_bones_by_constraints
from editboneconstraint.constraints import ConstraintManager


logger = logging.getLogger(__name__)


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

    try:
        evaluate_graph()
    except Exception as e:
        logger.error(e)

    return prefs.auto_evaluation_timer
