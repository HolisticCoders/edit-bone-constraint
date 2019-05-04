from editboneconstraint.constraints.abstractconstraint import AbstractConstraint
import bpy


class CopyTransform(AbstractConstraint):

    def evaluate(self):
        if not self.target:
            return
        self.bone.tail[0] = self.target.tail[0]
        self.bone.tail[1] = self.target.tail[1]
        self.bone.tail[2] = self.target.tail[2]
        self.bone.head[0] = self.target.head[0]
        self.bone.head[1] = self.target.head[1]
        self.bone.head[2] = self.target.head[2]
        self.bone.roll = self.target.roll



exported_constraints = [CopyTransform]