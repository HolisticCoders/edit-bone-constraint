from .abstract_constraint import AbstractConstraint
import bpy


class CopyScale(AbstractConstraint):

    def evaluate(self, matrix_before, length_before):
        if not self.target:
            return
        return matrix_before, self.target.length


exported_constraints = [CopyScale]
