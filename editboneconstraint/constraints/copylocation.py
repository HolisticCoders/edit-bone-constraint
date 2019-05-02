from editboneconstraint.constraints.abstractconstraint import AbstractConstraint
import bpy
from mathutils import Matrix


class CopyLocation(AbstractConstraint):
    def evaluate(self):
        if not self.target:
            return
        armature = self.property.id_data
        bone = armature.edit_bones[self.bone]
        target = armature.edit_bones[self.target]

        # we can't directly change the bone's matrix's translation
        new_mat = bone.matrix.copy()
        new_mat.translation = target.matrix.to_translation()
        bone.matrix = new_mat

        #  updating an edit bone matrix doesn't refresh the viewport automatically
        bpy.context.area.tag_redraw()


exported_constraints = [CopyLocation]