import json

#writing data to a JSON file
#not sure if we'll need to do this if we can just write in the JSON file directly

data = { "SrTiO3": {
    "lattice":
    [[3.9451301098, 0.0000000000, 0.0000000000],
    [0.0000000000, 3.9451301098, 0.0000000000],
    [0.0000000000, 0.0000000000, 3.9451301098]
    ],
    "atoms":
    [["Sr", 0.500000000, 0.500000000, 0.500000000],
    ["Ti", 0.000000000, 0.000000000, 0.000000000],
    ["O", 0.000000000, 0.000000000, 0.500000000],
    ["O", 0.500000000, 0.000000000, 0.000000000],
    ["O", 0.000000000, 0.500000000, 0.000000000]
    ],
    "forces":
    [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ],
  "stress":
    [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
}
}

with open("testDB2.json", "w") as write_file:
    json.dump(data, write_file, indent = 4)

#read all data from JSON file
#I just typed the data directly into the JSON with formatting
with open("testDB3.json", "r") as read_file:
    data_all = json.load(read_file)

print(data_all)

#read a part of the data from JSON file
with open("testDB3.json", "r") as read_file2:
    data_Si = json.load(read_file2)

print(data_Si["Si"])

    