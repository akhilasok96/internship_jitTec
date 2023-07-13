class Plant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.machines = []
    
    def addMachines(self, machine):
        self.machines.append(machine)

class Machine:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.spares = []
    
    def addSpares(self, spare_parts):
        self.spares.append(spare_parts)

class Pump(Machine):
    def __init__(self, name, model, power):
        super().__init__(name, model)
        self.power = power

class Mixer(Machine):
    def __init__(self, name, model, pressure):
        super().__init__(name, model)
        self.pressure = pressure

class Spares:
    def __init__(self, name, part_no):
        self.name = name
        self.part_no = part_no
    
    def displaySpares(self, part_no):
        pass

def plant_Main():
    plants = []
    while True:
        print("\n===== Plant Operations =====")
        print("1. Create Plant")
        print("2. Add Machines")
        print("3. Spare Part Details")
     
        choice = int(input("Enter your choice (1-3): "))

        match choice:
            case 1:
                pName = input("Enter the plant name: ")
                pLoc = input("Enter the location: ")
                p = Plant(pName, pLoc)
                plants.append(p)
                print("Plant created!")
            case 2:
                mName = input("Enter the machine name: ")
                mModel = input("Enter the machine model: ")
                mplant = input("Enter the plant: ")
                m = Machine(mName, mModel)
                print("Plant created!")
            case 3:
                pass
            case 4:
                print("Exiting the program...")
                break
plant_Main()

