from editboneconstraint.constraints.abstract_constraint import AbstractConstraint
import bpy


class CopyTransform(AbstractConstraint):

    def evaluate(self):
        if not self.target:
            return
        self.bone.matrix = self.target.matrix.copy()
        self.bone.length = self.target.length


exported_constraints = [CopyTransform]
