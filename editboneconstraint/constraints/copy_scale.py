import bpy
from mathutils import Matrix

from .abstract_constraint import AbstractConstraint


class CopyScale(AbstractConstraint):
    def evaluate(self, matrix_before):
        if not self.target:
            return
        new_mat = matrix_before @ Matrix.Scale(
            self.get_target_matrix().to_scale()[0], 4
        )
        return new_mat


exported_constraints = [CopyScale]
