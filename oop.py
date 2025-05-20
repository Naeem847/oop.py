class House:
    address:str="house no.123"
    no_of_door:int=2
    no_of_room:int=4
    def __init__(self):
        print(self.address)

naeem_house=House()
nadeem_house=House()
print(naeem_house.address)
print(naeem_house.no_of_door)
print(nadeem_house.no_of_room)



