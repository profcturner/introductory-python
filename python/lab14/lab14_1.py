
class Fleet(object):

    def __init__(self):
        self.ships = list()

    def add_ship(self, ship):
        self.ships.append(ship)

    def count_live_ships(self):
        afloat = 0
        for ship in self.ships:
            if not ship.destroyed:
                afloat += 1

        return afloat

    
    

class Battleship(object):
    '''A class to represent a ship from the game
    Battleships.

    name      the name of the ship
    position  a list of tuples that define where the ship is
    destroyed a boolean variable whether the ship is sunk
    '''

    def __init__(self, name=''):
        self.name = name
        self.destroyed = False
        self.positions = list()

    def add_position(self, coordinates):
        self.positions.append(coordinates)

    def check_if_hit(self, coordinates):
        if self.destroyed:
            print("You hit an already destroyed ship")
            return False
        
        hit = False
        for position in self.positions:
            if coordinates == position:
                hit = True
                
        if hit:        
            print("The ship has been hit")
            self.destroyed = True
        else:
            print("That was a miss")
        return hit


def main():
    
    # Add a ship
    enterprise = Battleship(name='Enterprise')

    # Define the cells it covers
    enterprise.add_position((1,2))
    enterprise.add_position((2,2))
    enterprise.add_position((3,2))

    ours = Fleet()
    ours.add_ship(enterprise)

    print(ours.count_live_ships())

    # Test the code to see if it is hit
    enterprise.check_if_hit((5,5))
    enterprise.check_if_hit((2,2))
    enterprise.check_if_hit((2,2))

    print(ours.count_live_ships())
    

if __name__ == '__main__':
    main()
