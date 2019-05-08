from .abstract_constraint import AbstractConstraint
import bpy
from mathutils import Matrix


class ChildOf(AbstractConstraint):
    def evaluate(self, matrix_before):
        if not self.target:
            return
        target_mat_with_scale = self.target.matrix.copy() @ Matrix.Scale(
            self.target.length, 4
        )
        new_mat = target_mat_with_scale @ self.offset
        return new_mat


exported_constraints = [ChildOf]
