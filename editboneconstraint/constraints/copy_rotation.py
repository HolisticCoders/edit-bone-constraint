from .abstract_constraint import AbstractConstraint
import bpy


class CopyRotation(AbstractConstraint):
    def evaluate(self, matrix_before):
        if not self.target:
            return
        # we can't directly change the bone's matrix's translation
        new_mat = self.target.matrix.copy()
        new_mat.translation = matrix_before.to_translation()
        return new_mat


exported_constraints = [CopyRotation]
