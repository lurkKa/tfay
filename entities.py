
class MicrowaveEntity:
    type_of_entity = None
    
    def __init__(self):
        type_of_entity = self.type_of_entity

class Microwave(MicrowaveEntity):
    model= None,
    capacity_limit = 0,
    mode = None
    

    def __init__(self):
        model = self.model
        capacity=self.capacity

class Socket(MicrowaveEntity):
    voltage = 0 ,

    def __init__(self):
        voltage = self.voltage,

class Food(MicrowaveEntity):
    name = None,
    quantity = 0

    def __init__(self):
        name = self.name
        quantity = self.quantity
