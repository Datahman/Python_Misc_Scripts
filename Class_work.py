# Demonstration of class inheritance

class AddMul(object):
    # Initialziation constructor
    def __init__(self, a=0, b=0):
        self. a = a
        self.b = b
    def __str__(self):
        return '('+ str(self.a) + ',' + str(self.b) + ')'
          
    def add(self):
        return self.a + self.b
    def multiply(self):
        return self.a * self.b
        
class SubtractDiv(AddMul):
    def __str__(self):
        return '(' + str(self.a) + ',' + str(self.b) + ')'
        
    def Subtract(self):
        return self. a - self.b
    def Divide(self):
        return float(self. a / self. b) 


# Static/ Class method

class Car(object):
    @staticmethod
    def has_wheel(wheel):
        wheel = wheel
        print 'This car has wheels:' + str(wheel)



# Demonstration of Meta-classes to use abstract aka virtual methods (C++)

# The problem :
# Use vehicle as an Abstract Base Class (ABC) on any vehicle type e.g: Car, bike, truck
# vehicle sale price: $5k * wheels
# vehucle buy price: vehicle_type_price_tag - (0.1 * miles driven)
from abc import ABCMeta, abstractmethod

# Set vehicle class to as ABC which inherits from None (object).

class Vehicle(object):
    """ A vehicle for sale at a given dealership.

        Attributes:
            wheels:
            miles_driven:
            make:
            model:
            year:
            sold_date:
    """
    __metaclass__ = ABCMeta
    # Global attributes to be over-written
    vehicle_type_price_tag = 0 # Value dependent on vehicle type
    wheels = 0 # As above

    def __init__(self, miles_driven, make, model, year, sold_date):
        self.miles_driven = miles_driven
        self.make = make
        self.model = model
        self.year = year
        self.sold_date = sold_date
        
    # Method to calculate vehicle sale
    
    def sale_price(self):
        if self.sold_date is not None:
            return 0.0 # If sold already
        return 5000.0 * self.wheels
    # Method to calculate buy out sale
    
    def buy_out(self):
        if self.sold_date is not None:
            return 0.0 # Not yet sold    
        return self.vehicle_type_price_tag - (0.1 * self.miles_driven) 
    # Make a virtual method for vehicle type
    
    @abstractmethod
    def vehicle_type(self):
        """Return a string representation of the vehicle type. """
        pass
         
      
class Bus(Vehicle):
    wheels = 4
    vehicle_type_price_tag = 10000

    def vehicle_type(self):
        return 'bus'
class Car(Vehicle):
    wheels = 4
    vehicle_type_price_tag = 8000

    def vehicle_type(self):
        return 'car'
        
if __name__ == '__main__':
    a = Car(10000, 'Honda', 'Subaha', '2016', None)
    print((a.buy_out(), a.sale_price(), a.vehicle_type()))
    #a = AddMul(2,5)

    #b = SubtractDiv(10,4).Divide()
    #print (b)

    #c = Car().has_wheel(4)
    #print(c)