from .abstract_constraint import AbstractConstraint
import bpy


class CopyScale(AbstractConstraint):

    def evaluate(self):
        if not self.target:
            return
        return self.bone.matrix, self.target.length


exported_constraints = [CopyScale]
