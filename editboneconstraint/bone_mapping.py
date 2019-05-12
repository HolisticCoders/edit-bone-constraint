from uuid import uuid4
import bpy
from collections import defaultdict


class BoneMapping:
    _instance = None
    _mapping = defaultdict(dict)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            armatures = bpy.data.armatures
            for armature in armatures:
                for bone in armature.edit_bones:
                    uuid = bone.editboneconstraint.uuid
                    if not uuid:
                        continue
                    cls._mapping[armature][uuid] = bone

        return cls._instance

    @property
    def mapping(self):
        return self._mapping.copy()

    def armature_bones(self, armature):
        return self.mapping[armature].values()

    def register_bone(self, armature, bone):
        uuid = str(uuid4())
        bone.editboneconstraint.uuid = uuid
        self._mapping[armature][uuid] = bone
        return uuid

    def bone_from_uuid(self, armature, uuid):
        return self._mapping[armature].get(uuid, None)

