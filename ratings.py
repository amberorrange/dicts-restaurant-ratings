"""Restaurant rating lister."""


data = open("scores.txt")
ratings_dict = {}

for line in data:
    name, rating = line.rstrip().split(":")
    ratings_dict[name] = rating


def sort_restaurants(restaurants_dict):
    for dname in sorted(restaurants_dict): 
        print(f"{dname} is rated at {restaurants_dict[dname]}.")


sort_restaurants(ratings_dict)


user_restaurant = input("What restuarant do you want to score?  ")
score = input( f"What score wiil you give to {user_restaurant}?  ")
ratings_dict[user_restaurant] = score

sort_restaurants(ratings_dict)



