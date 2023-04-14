# testing which uses the pyhton built in assert statements


# Creation of instances of classes
destination = Destination()
localization = Localization()
navigation = Navigation()
sensor = Sensor()
perception = Perception()
data_store = DataStore()
central_control = CentralControlUnit()
car = PhysicalCar()

# Set test data
destination_data = {"name": "Book Shop", "latitude": 39.773972, "longitude": -125}
localization_data = {"latitude": 39.773972, "longitude": -125}
sensor_data = {"type": "camera", "image": "image_data"}

# Test case 1: Perception detects a pedestrian and sends data to data store
perception_data = {"type": "pedestrian", "distance": 10}
perception.analyze(perception_data)
data_store.store_perception_data(perception.get_data())

# Test case 2: Perception detects a red light and sends data to data store
perception_data = {"type": "traffic_light", "color": "red"}
assert perception.analyze(perception_data)
data_store.store_perception_data(perception.get_data())

# Test case 3: Central control unit retrieves data from data store and generates corrective response
perception_data = data_store.retrieve_perception_data()
corrective_response = central_control.get_corrective_response(perception_data)
assert corrective_response == "deccelerate"

# Test case 4: Central control unit generates a corrective response based on destination data and localization data
navigation_data = navigation.calculate_route(destination_data, localization_data)
corrective_response = central_control.get_corrective_response(navigation_data)
assert corrective_response == "straight"

# Test case 5: Central control unit generates a corrective response based on sensor data
corrective_response = central_control.get_corrective_response(sensor_data)
assert corrective_response == "none"

# Test case 6: Physical car receives corrective response and performs action
car.perform_action(corrective_response)
assert car.current_speed == 0  
# The Expected outcome will be that the car should have decelerated to 0 in speed
