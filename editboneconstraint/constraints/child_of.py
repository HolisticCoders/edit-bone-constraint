from .abstract_constraint import AbstractConstraint
import bpy
from mathutils import Matrix


class ChildOf(AbstractConstraint):
    def evaluate(self, matrix_before, length_before):
        if not self.target:
            return
        new_mat = self.target.matrix @ self.offset
        return new_mat, length_before


exported_constraints = [ChildOf]
