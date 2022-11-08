class Door:
    
    def __init__(self):
        self.is_opened = False

    def open(self):
        self.is_opened = True
    def close(self):
        self.is_opened = False

class BlockedDoor(Door):

    def open(self):
        raise AttributeError("BlockedDoor cannot be opened!")
    def close(self):
        raise AttributeError("BlockedDoor cannot be closed!")

blocked_door = BlockedDoor()
# blocked_door.open()

blocked_door.close()




# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.