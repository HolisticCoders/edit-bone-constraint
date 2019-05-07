import bpy
from bpy.app import timers
from editboneconstraint.graph import auto_evaluate_timer


class EnableAutoEvaluationOperator(bpy.types.Operator):
    bl_idname = "editbone.enable_auto_evaluation"
    bl_label = "Enable Auto Evaluation"
    bl_options = {"INTERNAL"}

    def execute(self, context):
        package_name = __package__.split(".")[0]
        prefs = bpy.context.preferences.addons[package_name].preferences
        if not timers.is_registered(auto_evaluate_timer):
            timers.register(auto_evaluate_timer, persistent=True)
        prefs.auto_evaluation = True
        return {"FINISHED"}


class DisableAutoEvaluationOperator(bpy.types.Operator):
    bl_idname = "editbone.disable_auto_evaluation"
    bl_label = "Disable Auto Evaluation"
    bl_options = {"INTERNAL"}

    def execute(self, context):
        package_name = __package__.split(".")[0]
        prefs = bpy.context.preferences.addons[package_name].preferences
        if timers.is_registered(auto_evaluate_timer):
            timers.unregister(auto_evaluate_timer)
        prefs.auto_evaluation = False
        return {"FINISHED"}

