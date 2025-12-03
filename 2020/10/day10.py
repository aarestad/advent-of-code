input = """26
97
31
7
2
10
46
38
112
54
30
93
18
111
29
75
139
23
132
85
78
99
8
113
87
57
133
41
104
98
58
90
13
91
20
68
103
127
105
114
138
126
67
32
145
115
16
141
1
73
45
119
51
40
35
150
118
53
80
79
65
135
74
47
128
64
17
4
84
83
147
142
146
9
125
94
140
131
134
92
66
122
19
86
50
52
108
100
71
61
44
39
3
72"""''

example_one = """16
10
15
5
1
11
7
19
6
12
4"""


if __name__ == "__main__":
    adapters = [int(a) for a in example_one.split("\n")]
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)

    current_adapter = 0

    num_one_jolt_diffs = 0
    num_three_jolt_diffs = 0  # including built-in

    for i in range(1, len(adapters)):
        difference = adapters[i] - adapters[i - 1]

        if difference == 1:
            num_one_jolt_diffs += 1
        elif difference == 3:
            num_three_jolt_diffs += 1
        else:
            print(f'unexpected diff: {difference}')

    print('part one:')
    print(num_one_jolt_diffs * num_three_jolt_diffs)
