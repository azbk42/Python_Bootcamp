
# from turtle import Turtle, Screen

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pays", ["France", "Spain"])
table.add_column("Ville", ["Paris", "Madrid"]) 

table.align = "l"


print(table)