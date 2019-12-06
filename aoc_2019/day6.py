from typing import Optional, List


class OrbitingNode:
    def __init__(self, label: str, parent_label: Optional[str], parent: 'Optional[OrbitingNode]'):
        self.label = label
        self.parent_label = parent_label
        self.parent = parent
        self.children: 'List[OrbitingNode]' = []

    @property
    def parents(self):
        def parent_impl(me, prev_parents):
            if not me.parent:
                return prev_parents

            prev_parents.append(me.parent)
            return parent_impl(me.parent, prev_parents)

        return parent_impl(self, [])

    def __eq__(self, other):
        return self.label == other.label


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

    common_parents = sorted([p1 for p1 in planets['YOU'].parents
                             if p1 in planets['SAN'].parents],
                            key=lambda p: len(p.parents))

    nearest_common_parent = common_parents[-1]
    nearest_common_parent.parent = None  # set this common parent as the root of a new subtree
    print(len(planets['YOU'].parents) + len(planets['SAN'].parents) - 2)
