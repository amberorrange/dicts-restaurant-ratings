"""Restaurant rating lister."""


data = open("scores.txt")
ratings_dict = {}

for line in data:
    name, rating = line.rstrip().split(":")

    ratings_dict[name] = rating


for dname in sorted(ratings_dict): 
    print(f"{dname} is rated at {ratings_dict[dname]}.")
    print()