from controller import Robot

OBSTACLE_THRESHOLD = 80.0


#Robot and Hardware Init
robot = Robot()
camera = robot.getDevice("camera")


timestep = int(robot.getBasicTimeStep())

#Robot Hardware Init
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
camera.enable(timestep)

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

sensors = []

for i in range(8):
    sensor = robot.getDevice(f"ps{i}")
    sensor.enable(timestep)
    sensors.append(sensor)




#Simulation Loop

while robot.step(timestep) != -1:
    left_speed = 0.0
    right_speed = 0.0
    distances = [sensor.getValue() for sensor in sensors]
    #We find the obstacles using one of the 8 proximity sensors
    front_right = max(distances[0], distances[1])
    front_left = max(distances[6], distances[7])
    #Decide if said obstacle is too close
    if front_left > OBSTACLE_THRESHOLD or front_right > OBSTACLE_THRESHOLD:
        print("Obstacle Detected")
        if front_left > front_right:
            right_speed = -3.0
            left_speed = 3.0
        else:
            right_speed = 3.0
            left_speed = -3.0
    else:
        right_speed = 3.0
        left_speed = 3.0
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
    
    print(distances)