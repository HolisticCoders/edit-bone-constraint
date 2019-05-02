from editboneconstraint.constraints.abstractconstraint import AbstractConstraint
import bpy
from mathutils import Matrix


class CopyRotation(AbstractConstraint):
    def evaluate(self):
        for i in range(10):
            print()
        if not self.target:
            return
        armature = self.property.id_data
        bone = armature.edit_bones[self.bone]
        target = armature.edit_bones[self.target]

        # we can't directly change the bone's matrix's translation
        new_mat = target.matrix.copy()
        new_mat.translation = bone.matrix.to_translation()
        bone.matrix = new_mat


exported_constraints = [CopyRotation]
