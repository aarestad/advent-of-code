from typing import Optional, List


class OrbitingNode:
    def __init__(self, label: str, parent_label: Optional[str], parent: 'Optional[OrbitingNode]'):
        self.label = label
        self.parent_label = parent_label
        self.parent = parent
        self.children: 'List[OrbitingNode]' = []

    def parents(self):
        def parent_impl(me, prev_parents):
            if not me.parent:
                return prev_parents

            prev_parents.append(me.parent)
            return parent_impl(me.parent, prev_parents)

        return parent_impl(self, [])

    def num_parents(self):
        return 0 if not self.parent else self.parent.num_parents() + 1

    def __eq__(self, other):
        return self.label == other.label

    def __repr__(self):
        return "OrbitingNode(label={})".format(self.label)


def get_common_parent(node_1, node_2):
    node_1_parents = node_1.parents()
    node_2_parents = node_2.parents()

    intersection = [p for p in node_1_parents if p in node_2_parents]

    return sorted(intersection, key=lambda p: p.num_parents() if p else 0, reverse=True)[0]


if __name__ == '__main__':
    planets = {
        'COM': OrbitingNode('COM', None, None)
    }

    with open('06_input.txt') as orbits:
        for orbit in orbits:
            (parent_label, new_label) = orbit.strip().split(')')

            parent = planets.get(parent_label, None)
            new_planet = OrbitingNode(new_label, parent_label, parent)

            if parent:
                parent.children.append(new_planet)

            planets[new_label] = new_planet

            for p in planets.values():
                if p.parent_label == new_label:
                    p.parent = new_planet
                    new_planet.children.append(p)

    you = planets['YOU']
    santa = planets['SAN']
    common_parent = get_common_parent(you, santa)
    common_parent.parent = None

    print(you.num_parents() + santa.num_parents() - 2)
