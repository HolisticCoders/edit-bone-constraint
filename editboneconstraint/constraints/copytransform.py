from editboneconstraint.constraints.abstractconstraint import AbstractConstraint
import bpy


class CopyTransform(AbstractConstraint):

    def evaluate(self):
        if not self.target:
            return
        armature = self.property.id_data
        bone = armature.edit_bones[self.bone]
        target = armature.edit_bones[self.target]

        bone.tail[0] = target.tail[0]
        bone.tail[1] = target.tail[1]
        bone.tail[2] = target.tail[2]
        bone.head[0] = target.head[0]
        bone.head[1] = target.head[1]
        bone.head[2] = target.head[2]
        bone.roll = target.roll



exported_constraints = [CopyTransform]