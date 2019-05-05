from .abstract_constraint import AbstractConstraint
import bpy
from mathutils import Matrix


class ChildOf(AbstractConstraint):
    def evaluate(self):
        if not self.target:
            return
        new_mat = self.target.matrix @ self.offset
        self.bone.matrix = new_mat


exported_constraints = [ChildOf]
