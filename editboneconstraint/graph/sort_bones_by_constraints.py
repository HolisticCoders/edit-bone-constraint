import networkx


def sort_bones_by_constraints(armature):
    graph = networkx.DiGraph()

    bones = armature.edit_bones
    for bone in bones:
        for constraint in bone.constraints:
            target_name = constraint.target
            target = armature.edit_bones[target_name]

            if bone not in graph:
                graph.add_node(bone)
            if target not in graph:
                graph.add_node(target)

            graph.add_edge(target, bone)

    sorted_bones = networkx.topological_sort(graph)
    return sorted_bones
