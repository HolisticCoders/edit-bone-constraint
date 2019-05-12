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

        for i, constraint in enumerate(
            context.active_bone.editboneconstraint.constraints
        ):
            self.draw_constraint(context, constraint, i)

    def draw_constraint(self, context, constraint, index):
        layout = self.layout
        box = layout.box()

        self.header_template(context, constraint, index, box)

        if constraint.show_expanded:
            self.body_template(context, constraint, box)

    def header_template(self, context, constraint, index, layout):
        row = layout.row()

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

        if len(context.active_bone.editboneconstraint.constraints) > 1:
            col = row.column()
            reorder_row = col.row(align=True)
            if index == 0:
                operator = reorder_row.operator(
                    "editbone.move_constraint_down", text="", icon="TRIA_DOWN"
                )
                operator.constraint_name = constraint.name
                operator.bone_name = constraint.bone
            elif index == len(context.active_bone.editboneconstraint.constraints) - 1:
                operator = reorder_row.operator(
                    "editbone.move_constraint_up", text="", icon="TRIA_UP"
                )
                operator.constraint_name = constraint.name
                operator.bone_name = constraint.bone
            else:
                operator = reorder_row.operator(
                    "editbone.move_constraint_down", text="", icon="TRIA_DOWN"
                )
                operator.constraint_name = constraint.name
                operator.bone_name = constraint.bone
                operator = reorder_row.operator(
                    "editbone.move_constraint_up", text="", icon="TRIA_UP"
                )
                operator.constraint_name = constraint.name
                operator.bone_name = constraint.bone

        col = row.column()
        operator = col.operator(
            "editbone.delete_constraint", text="", icon="X", emboss=False
        )
        operator.constraint_name = constraint.name
        operator.bone_name = constraint.bone

    def body_template(self, context, constraint, layout):
        row = layout.row()
        row.prop_search(constraint, "target", context.object.data, "edit_bones")

        if constraint.type == "CopyLocation":
            self.copy_location_template(constraint, layout)

        row = layout.row()
        row.prop(constraint, "influence", slider=True)

    def copy_location_template(self, constraint, layout):
        row = layout.row()
        row.label(text="Head/Tail:")
        row.prop(constraint, "head_tail", text="", slider=True)
