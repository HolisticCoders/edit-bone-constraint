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

        for constraint in context.active_bone.constraints:
            self.draw_constraint(context, constraint)

    def draw_constraint(self, context, constraint):
        layout = self.layout
        box = layout.box()

        row = box.row()
        row.prop(constraint, "name")

        row = box.row()
        row.prop_search(constraint, "target", context.object.data, "edit_bones")

        row = box.row()
        row.prop(constraint, "head_tail")

        row = box.row()
        row.prop(constraint, "influence")
