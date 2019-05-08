import bpy


class EditBoneConstraintAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    auto_evaluation: bpy.props.BoolProperty(name="Auto Evaluation", default=True)
    auto_evaluation_timer: bpy.props.FloatProperty(
        name="Auto Evaluation Timer (In Seconds)",
        default=0.016,
        description="Time between two evaluations of the edit bones constraint graph in seconds.\n"
        "The lower the value, the more evaluations per second (eps).\n"
        "0.033 = 30eps.\n"
        "0.016 = 60eps.\n",
    )

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        if self.auto_evaluation:
            row.operator("editbone.disable_auto_evaluation", icon="PAUSE")
        else:
            row.operator("editbone.enable_auto_evaluation", icon="PLAY")

        row.prop(self, "auto_evaluation_timer")
