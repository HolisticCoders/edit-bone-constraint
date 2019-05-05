from .abstract_constraint import AbstractConstraint
import bpy


class CopyTransform(AbstractConstraint):

    def evaluate(self):
        if not self.target:
            return
        return self.target.matrix.copy(), self.target.length


exported_constraints = [CopyTransform]
