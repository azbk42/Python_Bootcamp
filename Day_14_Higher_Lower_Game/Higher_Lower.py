from logo import logo
from data import data
import random


person = data[random.randint(0,len(data)-1)]

print(f"Nom: {person['name']}")
print(f"Nombre d'abonnés: {person['follower_count']}")
print(f"Description: {person['description']}")
print(f"Pays: {person['country']}")