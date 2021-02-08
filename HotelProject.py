class Room:

    def __init__(self, roomNum, bedType, smoking, rate):

        self.roomNum = roomNum

        self.bedType = bedType

        self.smoking = smoking

        self.rate = rate

        self.occupantName = None

        self.occupied = False

    def getBedType(self):

        return self.bedType

    def getSmoking(self):

        return self.smoking

    def getRoomNum(self):

        return self.roomNum

    def getRoomRate(self):

        return self.rate

    def getOccupant(self):

        return self.occupantName

    def setOccupied(self, occupied):

        self.occupied = occupied

    def setOccupant(self, occupantName):

        self.occupantName = occupantName

    def setRoomNum(self, roomNum):

        self.roomNum = roomNum

    def setBedType(self, bedType):

        self.bedType = bedType

    def setRate(self, rate):

        self.rate = rate

    def setSmoking(self, smoking):

        self.smoking = smoking

    def isOccupied(self):

        return self.occupied

    def __str__(self):

        roomStr = '\nRoom Number: ' + str(self.roomNum)

        if (self.occupied and (self.occupantName != None)):

            roomStr += '\nOccupant Name : ' + self.occupantName

        else:

            roomStr += '\nOccupant Name : Not Occupied'

        roomStr += '\nSmoking room : ' + self.smoking + '\nBed Type : ' + self.bedType + '\nRate : ' + "{0:.1f}".format(
            self.rate) + '\n'

        return roomStr


# Hotel class

class Hotel:
    NOT_FOUND = -1

    def __init__(self, name, location):

        self.name = name

        self.location = location

        self.numOfRooms = 0

        self.theRooms = [None] * 10

        self.occupiedCnt = 0

    def getName(self):

        return self.name

    def getLocation(self):

        return self.location

    def setName(self, name):

        self.name = name

    def setLocation(self, location):

        self.location = location

    def isFull(self):

        return (self.numOfRooms == self.occupiedCnt)

    def isEmpty(self):

        return (self.occupiedCnt == 0)

    def addRoom(self, roomNumber, bedType, smoking, price):

        if self.numOfRooms < len(self.theRooms):

            room = Room(roomNumber, bedType, smoking, price)

            self.theRooms[self.numOfRooms] = room

            self.numOfRooms += 1

        else:

            print('Rooms list in the Hotel is full')

    def addReservation(self, occupantName, smoking, bedType):

        roomFound = False

        for room in self.theRooms:

            if ((room != None) and (not room.isOccupied()) and (room.getSmoking().lower() == smoking.lower()) and (
                    room.getBedType().lower() == bedType.lower())):
                room.setOccupied(True)

                room.setOccupant(occupantName)

                self.occupiedCnt += 1

                roomFound = True

                break

        if (roomFound):

            print('Reservation finished successfully!')

        else:

            print('Unable to find room with the given preferences!')

    def cancelReservation(self, occupantName):

        ind = self.findReservation(occupantName)

        if ind != self.NOT_FOUND:
            self.theRooms[ind].setOccupied(False)

            self.theRooms[ind].setOccupant(None)

            self.occupiedCnt -= 1

            print('Reservation was cancelled successfully!')

        if ind == self.NOT_FOUND:
            print("Reservation doesn't exist")

    def findReservation(self, occupantName):

        for i in range(self.numOfRooms):

            if ((self.theRooms[i].isOccupied()) and (self.theRooms[i].getOccupant().lower() == occupantName.lower())):
                return i

        return self.NOT_FOUND

    def printReservationList(self):

        for room in self.theRooms:

            if ((room != None) and (room.isOccupied())):
                print(room)

    def getDailySales(self):

        dailySales = 0

        for room in self.theRooms:

            if ((room != None) and (room.isOccupied())):
                dailySales += room.getRoomRate()

        return dailySales

    def occupancyPercentage(self):

        if self.numOfRooms > 0:
            return (float(self.occupiedCnt * 100) / self.numOfRooms)

        return 0

    def __str__(self):

        hotelStr = 'Hotel Name : ' + self.name + '\nNumber of Rooms : ' + str(
            self.numOfRooms) + '\nNumber of Occupied Rooms : ' + str(self.occupiedCnt)

        hotelStr += '\n\nRoom Details are :\n'

        for i in range(self.numOfRooms):
            hotelStr += str(self.theRooms[i])

        return hotelStr


# function to display and get the user choice

def menu():
    print('1. Add room')

    print('2. Add Reservation')

    print('3. Cancel Reservation')

    print('4. Print Reservation List')

    print('5. Get Daily Sales')

    print('6. Get Occupancy Percentage')

    print('7. Exit')

    choice = int(input('Enter a choice(1-7) : '))

    while choice < 1 or choice > 7:
        print('Invalid choice')

        choice = int(input('Enter a choice(1-7) : '))

    return choice


# main function

def main():
    hotel = Hotel("Beach Marriot", "NNN")

    hotel.addRoom(101, "queen", "s", 100)

    hotel.addRoom(102, "king", "n", 110)

    hotel.addRoom(103, "king", "n", 88)

    hotel.addRoom(104, "twin", "s", 100)

    hotel.addRoom(105, "queen", "n", 99)

    print(hotel)

    done = False

    while not done:

        choice = menu()

        if choice == 1:

            roomNumber = int(input('Room Number : '))

            bedType = input('Bed Type : ')

            smoking = input('Smoking(s) or Non-Smoking(n) : ')

            price = float(input('Price : '))

            hotel.addRoom(roomNumber, bedType, smoking, price)



        elif choice == 2:

            occupantName = input('Occupant Name : ')

            smoking = input('Smoking room(s) or Non-Smoking(n) : ')

            bedType = input('Bed Type : ')

            hotel.addReservation(occupantName, smoking, bedType)

        elif choice == 3:

            occupantName = input('Occupant Name : ')

            hotel.cancelReservation(occupantName)

        elif choice == 4:

            hotel.printReservationList()

        elif choice == 5:

            print('Daily Sales : %.2f' % (hotel.getDailySales()))

        elif choice == 6:

            print('Occupancy Percentage : %.2f' % (hotel.occupancyPercentage()))

        else:

            done = True


# call the main function

main()   