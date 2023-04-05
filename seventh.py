class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))






class vehicle:
    def __init__(self, color, type, terrain) -> None:
        self.color = color
        self.type = type
        self.terrain = terrain

    def __str__(self) -> str:
        return (
            "{ "
            + f"color : {self.color}, type: {self.type}, terrain: {self.terrain}"
            + " }"
        )


bus = vehicle("blue", "electric", "land")
ship = vehicle("red", "fuel", "water")
plane = vehicle("white", "fuel", "air")

print(bus)
