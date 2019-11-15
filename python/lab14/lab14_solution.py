# Battleships, with objects
# Colin Turner

class Fleet(object):
    ''' Allows many ships to be contained in one side or fleet

    name   is the name of the fleet
    ships  is a list of Ship objects'''

    def __init__(self, name):
        ''' Set up, assuming name to be mandatory '''
        self.ships = list()
        self.name = name

    def __str__(self):
        ''' Print the fleet name and number of ships alive '''
        return self.name + ': ' + str(self.count_live_ships()) + ' ships afloat' 

    def add_ship(self, ship):
        ''' Add a ship object to this fleet '''
        self.ships.append(ship)

    def count_live_ships(self):
        ''' Return how many ships are afloat '''
        afloat = 0
        for ship in self.ships:
            if not ship.destroyed:
                afloat += 1

        return afloat

    def check_if_hit(self, coordinates):
        ''' Check all the ships in the fleet for a given coordinate attack '''
        for ship in self.ships:
            ship.check_if_hit(coordinates)

    def report(self):
        ''' Print a fleet report '''
        #Print the minimal name and report
        print(self)

        # Now for each ship
        for ship in self.ships:
            print(ship)


class Battleship(object):
    '''A class to represent a ship from the game
    Battleships.

    name      the name of the ship
    position  a list of tuples that define where the ship is
    destroyed a boolean variable whether the ship is sunk
    '''

    def __init__(self, name):
        ''' Initialise the ship, name mandatory '''
        self.name = name
        self.destroyed = False
        self.positions = list()

    def __str__(self):
        ''' Gives the ship name and current status '''
        if self.destroyed:
            status = 'destroyed'
        else:
            status = 'live'
            
        return self.name + ': status ' + status

    def add_position(self, coordinates):
        ''' Add the tuple of coordinates to the current list '''
        self.positions.append(coordinates)

    def check_if_hit(self, coordinates):
        ''' See if a coordinate hit this ship

        returns true if ship destroyed, false otherwise'''
    
        # Assume it's a miss
        hit = False

        # Check every coordinate in positions
        for position in self.positions:
            if coordinates == position:
                # They are the same, so it's a hit
                hit = True
                
        if hit:
            # Ok, but is the ship already dead?
            if self.destroyed:
                print("You hit an already destroyed ship")
                return False

            else:
                # No, so label the ship as killed
                print("The ship has been hit")
                self.destroyed = True
        else:
            # Only comment if ship isn't already destroyed
            if not self.destroyed:
                print("That was a miss")
        return hit


def main():
    
    # Add a ship
    enterprise = Battleship(name='Enterprise')

    # Define the cells it covers
    enterprise.add_position((1,2))
    enterprise.add_position((2,2))
    enterprise.add_position((3,2))

    columbia = Battleship(name='Columbia')
    columbia.add_position((5,5))
    columbia.add_position((5,6))

    # Create a fleet and add these two ships to it.
    ours = Fleet('themuns')
    ours.add_ship(enterprise)
    ours.add_ship(columbia)

    # More ships
    discovery = Battleship(name='Discovery')
    discovery.add_position((7,2))

    challenger = Battleship(name='Challenger')
    challenger.add_position((8,1))
    challenger.add_position((8,2))
    challenger.add_position((8,3))

    # Create a second fleet and add these ships to it.
    theirs = Fleet('usuns')

    theirs.add_ship(discovery)
    theirs.add_ship(challenger)

    # Keep going while one team has live ships
    while ours.count_live_ships() and theirs.count_live_ships():
        # Ask for a coordinate pair
        x = int(input("X coordinate: "))
        y = int(input("Y coordinate: "))

        # Make it a tuple
        coordinates = (x, y)

        # Check each fleet for hits
        ours.check_if_hit(coordinates)
        theirs.check_if_hit(coordinates)

        # print a status report
        print('Ships left {}'.format(ours.count_live_ships() + theirs.count_live_ships()))
        theirs.report()
        ours.report()

    # When we get here, someone has won
    print("One fleet has been destroyed")

        
if __name__ == '__main__':
    main()
