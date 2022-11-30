in_file = "day1.txt"
with open(in_file) as f:
    lines = f.readlines()
data = [l.strip('\n') for l in lines]
