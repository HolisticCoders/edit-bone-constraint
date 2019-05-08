from .abstract_constraint import AbstractConstraint
import bpy


class CopyTransform(AbstractConstraint):
    def evaluate(self, matrix_before):
        if not self.target:
            return
        return self.get_target_matrix()


exported_constraints = [CopyTransform]
