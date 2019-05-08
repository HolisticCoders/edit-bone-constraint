# Edit Bone Constraint
Edit Bone Constraint is a Blender 2.80+ addon that lets you add constraints from any edit bone to any edit bone, as long as they are a part of the same armature.

### This, can improve your workflows in a few ways:
- After having setup all your edit bones constraints, you can change the rest pose of a rig very quickly by just moving some "Guide" bones instead of having to move every single bone of the armature
- If you are on a production with a lot of similar assets (let's say biped characters) you can make the rig for one, import it in every other asset, move the guide bones and get to skinning. Your rigs will all be exactly the same without having to rely on an autorig.
- If some assets utilizing the same rigs have a few different things, you can modify the rig as you see fit without having to write post scripts since you do not need to worry about rebuilding the rig.
- You can easily create constraints from scripts if you want to integrate this to your existing tools, allowing for a very custom made workflow that will work for anyone.

### Implemented constraints
- Copy location
- Copy Rotation
- Copy Scale
- Copy Transform
- Child Of

### TODO
- New Constraints:
  - Track To (aim constraint).
  - Pole vector (used to automatically place pole vectors based on a chain of bones)
  - Python constraint that lets you run an arbitrary script.
- More options for the constraints (copy the location on only a specific axis for example)
- Find a way to reference the bones directly rather than storing their names in StringProperty.
- Better cycles detection in the evaluation of the constraints graph.

### A few random things to note:
- This will _not_ slow down your rigs at all. The evaluation of the rig and the evaluation of the constraints are absolutely not related. (we made our own very simple dependency graph, dedicated to the edit mode of the armatures)
- The evaluation is by default ran 30 times a second, you can change this in the addon preferences and even disable the auto evaluation. If you do so, you have an operator that you can call to evaluate the graph manually (search "Evaluate Edit Bone Constraints")
- The constraints will _not_ be evaluated if a cycle is detected.
- The cycles are detected on a bone-level for now meaning that `bone1 > copy location > bone2 > copy rotation > bone1` will be considered as a cycle. This will probably change in the future
- The scaling part of the constraints can behave a bit awkwardly for now as edit bones don't really have a scale but rather a distance between their head and tail (Meaning we don't handle negative scaling well).
- Renaming a bone will break the constraints it owns and the constraints in which it is a target.
