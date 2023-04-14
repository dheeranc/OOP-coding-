
import time
import random
from collections import deque


# Defining the user interface class

class UserInterface:
    def __init__(self):
        self.destination = None
        
    #method used to set the destination name from the user input
    #setting weather, location and traffic conditions from random conditions for the purpose for this program

    def set_destination(self):
        self.destination = Destination(input("Enter your destination: "))
        # collect destination conditions
        self.destination.get_location()
        self.destination.get_weather()
        self.destination.get_traffic()
        print("Destination set to", self.destination)

    def get_destination(self):
        return self.destination



# Defining the destination class, which 

class Destination:
    def __init__(self, name):
        self.Name = name
        self.location = None
        self.weather = None
        self.traffic = None

    # set location from given conditions 
    def get_location(self):
        self.location = random.choice(['Busy', 'Quiet', 'Empty'])
        return self.location

    # set weather random from given conditions 
    def get_weather(self):
        self.weather = random.choice(['Sunny', 'Rainy', 'Cloudy', 'Snowy'])
        return self.weather

    # set traffic conditions from the given conditions 
    def get_traffic(self):
        self.traffic = random.choice(['Low', 'Medium', 'High'])
        return self.traffic

    def get_name(self):
        return self.name
    
    # dislay the destination details 
    def __str__(self):
        return "Destination [ Name : "f"{self.Name}, Status : "f"{self.location}, Traffic :{self.traffic}" \
               f", Weather :{self.weather}] "



# Defining the Localization class, 

class Localization:
    def __init__(self):
        self.current_location = None
        self.current_speed = None

    #get user current location input 
    def get_location(self):
        self.current_location = input("Enter current location: ")
        print("Current location set to", self.current_location)

    # set speed between 40 to 100 km/h
    def get_speed(self):
        self.current_speed = random.randint(40, 100)
        print("Current speed is", self.current_speed, "km/h")


# Defining the navigation class

class Navigation:
    def __init__(self):
        self.route = None
        self.destination = None

    #display route and wait for 2sec
    def get_route(self, current_location):
        print("Calculating route to", self.destination, "from", current_location)
        time.sleep(2)
        
        # display locations points and create a route 
        self.route = [current_location, "Point 1", "Point 2", self.destination]
        print("Route:", self.route)

    def set_destination(self, des):
        self.destination = des


# Defining the sensor class

class Sensor:
    def __init__(self):
        self.camera = None
        self.lidar = None
        self.radar = None

    # get camaera sensor data
    def get_camera_data(self):
        self.camera = "Camera Data"
        print("Camera data collected")

    #get lidar sensor data
    def get_lidar_data(self):
        self.lidar = "Lidar Data"
        print("Lidar data collected")
    
    #get radar data
    def get_radar_data(self):
        self.radar = "Radar Data"
        print("Radar data collected")



# Defining the Perception class

class Perception:
    def __init__(self, s):
        self.sensor = s
        self.object_detection = None

    #call method to get sensor data
    def process_sensor_data(self):
        self.sensor.get_camera_data()
        self.sensor.get_lidar_data()
        self.sensor.get_radar_data()

    #objects detect nearby
    def detect_objects(self):
        self.object_detection = "Object Detection Data"
        print("Objects detected")
        

# defining the data storage class

# The DataStore class represents the storage system for the data
# that is generated via the self driving car

class DataStore:
    def __init__(self):
        self.nav_queue = deque()
        self.perception_stack = deque()

    def add_to_nav_queue(self, data):
        self.nav_queue.append(data)
        print("Added to navigation queue:", data)

    def add_to_perception_stack(self, data):
        self.perception_stack.append(data)
        print("Added to perception stack:", data)

#get_navigation and get_perception are used to retreive the oldest piece of data
#from the corresponding queue / stack

    def get_navigation_data(self):
        if self.nav_queue:
            return self
        else:
            return None

    def get_perception_data(self):
        if self.perception_stack:
            return self.perception_stack.pop()
        else:
            return None


# define the central control unit class
#the central conrol unit acts as the computer or processor of information to generate
#commands and decisons that are passed on the physical car to make

class CentralControlUnit:
    def __init__(self):
        self.datastore = DataStore()
        self.navigation_data = None
        self.perception_data = None
        self.physical_car = PhysicalCar()

#method retrieves the last navigation and perception data from the datastore
        
    def process_data(self):
        self.navigation_data = self.datastore.get_navigation_data()
        self.perception_data = self.datastore.get_perception_data()
        print("Processing data:", self.navigation_data, self.perception_data)


# retrieves the last navigation and perception data from data store

    def analyze_data(self):
        self.navigation_data = self.datastore.get_navigation_data()
        self.perception_data = self.datastore.get_perception_data()
        # Analyze perception and navigation data to determine corrective response
        # In this example, the corrective response is a simple "go straight" command
        corrective_response = "go straight"

        # Send the corrective response to the physical car
        self.physical_car.apply_corrective_response(corrective_response)
        # Perform analysis and make corrective responses

    def run(self):
        while True:
            self.process_data()
            self.analyze_data()
            time.sleep(1)
            
#define the Physical Car class, this was chnaged from vehicle interface
#this represent the actual car object

class PhysicalCar:
    def __init__(self):

        # car attributes 
        self.steering = 0
        self.acceleration = 0
        self.deceleration = 0

    def apply_corrective_response(self, corrective_response):
        # Apply the corrective response to adjust the car's trajectory
        # In this example, the corrective response is a simple "go straight" command, so nothing needs to be done
        print("Applying corrective response:", corrective_response)


# main function

# This runs the program allowing for the testing of different variables and locations 
# since there is not feedback from the perception module due to no real sensors the corrective responce remains to go straight 
if __name__ == '__main__':
    user_interface = UserInterface()
    user_interface.set_destination()
    localization = Localization()
    localization.get_location()
    sensor = Sensor()
    perception = Perception(sensor)
    navigation = Navigation()
    navigation.set_destination(user_interface.get_destination())
    navigation.get_route(localization.current_location)
    datastore = DataStore()
    datastore.add_to_nav_queue(navigation.route)
    datastore.add_to_perception_stack(perception.object_detection)
    c = CentralControlUnit()
    c.run()
