import bpy


class ConstraintStackPanel(bpy.types.Panel):
    bl_label = "Constraint Stack"
    bl_idname = "ARMATURE_PT_constraint_stack"
    bl_space_type = "PROPERTIES"
    bl_context = "bone"
    bl_region_type = "WINDOW"

    @classmethod
    def poll(cls, context):
        return context.object.type == "ARMATURE" and context.object.mode == "EDIT"

    def draw(self, context):
        layout = self.layout
        layout.operator_menu_enum(
            "editbone.constraint_add", "type", text="Add Edit Bone Constraint"
        )

        for i, constraint in enumerate(context.active_bone.constraints):
            self.draw_constraint(context, constraint, i)

    def draw_constraint(self, context, constraint, index):
        layout = self.layout
        box = layout.box()

        # HEADER
        row = box.row()

        col = row.column()
        if constraint.show_expanded:
            col.prop(
                constraint,
                "show_expanded",
                icon="TRIA_DOWN",
                icon_only=True,
                emboss=False,
            )
        else:
            col.prop(
                constraint,
                "show_expanded",
                icon="TRIA_RIGHT",
                icon_only=True,
                emboss=False,
            )

        col = row.column()
        col.label(text=constraint.type)

        col = row.column()
        if not constraint.target:
            col.alert = True
        col.prop(constraint, "name", text="")

        col = row.column()
        if constraint.mute:
            col.prop(constraint, "mute", icon="HIDE_ON", icon_only=True, emboss=False)
        else:
            col.prop(constraint, "mute", icon="HIDE_OFF", icon_only=True, emboss=False)

        if len(context.active_bone.constraints) > 1:
            col = row.column()
            reorder_row = col.row(align=True)
            if index == 0:
                reorder_row.operator("editbone.move_constraint_down", text="", icon="TRIA_DOWN")
            elif index == len(context.active_bone.constraints) - 1:
                reorder_row.operator("editbone.move_constraint_up", text="", icon="TRIA_UP")
            else:
                reorder_row.operator("editbone.move_constraint_down", text="", icon="TRIA_DOWN")
                reorder_row.operator("editbone.move_constraint_up", text="", icon="TRIA_UP")


        col = row.column()
        col.operator("editbone.delete_constraint", text="", icon="X", emboss=False)

        if constraint.show_expanded:
            # BODY
            row = box.row()
            row.prop_search(constraint, "target", context.object.data, "edit_bones")

            row = box.row()
            row.label(text="Head/Tail:")
            row.prop(constraint, "head_tail", text="", slider=True)

            row = box.row()
            row.prop(constraint, "influence", slider=True)
