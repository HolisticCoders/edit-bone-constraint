from editboneconstraint.constraints.abstractconstraint import AbstractConstraint
import bpy
from mathutils import Matrix


class ChildOf(AbstractConstraint):
    def evaluate(self):
        if not self.target:
            return
        armature = self.property.id_data
        bone = armature.edit_bones[self.bone]
        target = armature.edit_bones[self.target]
        new_mat = self.offset @ target.matrix
        bone.matrix = new_mat


exported_constraints = [ChildOf]