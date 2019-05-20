from .abstract_constraint import AbstractConstraint
import bpy
from mathutils import Matrix


class CopyRotation(AbstractConstraint):
    def evaluate(self, matrix_before):
        if not self.target:
            return
        # we can't directly change the bone's matrix's translation
        scale = matrix_before.to_scale()[0]
        new_mat = self.target.matrix.copy() @ Matrix.Scale(scale, 4)
        new_mat.translation = matrix_before.to_translation()
        return new_mat


exported_constraints = [CopyRotation]
