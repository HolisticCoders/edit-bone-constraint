from editboneconstraint.constraints.abstract_constraint import AbstractConstraint
import bpy
from mathutils import Matrix


class CopyRotation(AbstractConstraint):
    def evaluate(self):
        if not self.target:
            return
        # we can't directly change the bone's matrix's translation
        new_mat = self.target.matrix.copy()
        new_mat.translation = self.bone.matrix.to_translation()
        self.bone.matrix = new_mat


exported_constraints = [CopyRotation]
