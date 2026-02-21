import csv


class Robot():
    def __init__(self, name, battery, positionx, positiony):  #introducing robot with battery and position
        self.name = name 
        self.battery = battery
        self.positionx= positionx
        self.positiony = positiony
        print(f"{self.name} has battery level {self.battery} and is at position ({self.positionx}, {self.positiony})!")  #clarifying our status at the start of the program
    
    #defining our move function, which will allow us to move the robot and update its battery level and position accordingly. 
    def move(self, distancex, distancey):
        self.positionx += distancex
        self.positiony += distancey
        self.battery -= 5  #Each movement reduces battery by 5 percent
        if self.battery < 20:  #If battery is below 20 percent, we need to send warning
            print(f"Warning: {self.name} has low battery! Please recharge soon.")
        print(f"{self.name} has battery level {self.battery} and is now at position ({self.positionx},{self.positiony})!")

    #defining our recharge function which allows robot to charge and have control of battery percentage. it also includes checks for valid inputs
    def recharge(self):
        try:
            recharge_amount = int(input(f"How much would you like to recharge {self.name}'s battery? (Enter a number between 0 and 100): "))
            if recharge_amount < 0 or recharge_amount > 100:
                raise ValueError("Recharge amount must be between 0 and 100.")
        except ValueError:
            print(f"Error: please enter a valid number between 0 and 100.")
            return
        self.battery += recharge_amount
        print(f"{self.name} has been recharged to {self.battery}%!")
        
    # just having a function to have an update on the robot
    def report_status(self):
        print(f"{self.name} has battery level {self.battery} and is at position ({self.positionx}, {self.positiony})!")


# begining to define our ground robot 
class GroundRobot(Robot):
        def __init__(self, name, battery, positionx, positiony, wheelcount, max_speed):
            super().__init__(name, battery, positionx, positiony)
            self.wheelcount = wheelcount
            self.max_speed = max_speed
        
        #asking user for distance and speed. Also includes checks for max speed, low battery, and valid inputs.
        def drive(self, speed, directionx, directiony):
            #validating user input for direction for ground robot to move
            try:
                if directionx < 0 or directiony < 0:
                    raise ValueError("Robot cannot move to negative coordinates.")
            except ValueError:
                print("Error: Please enter valid numbers for direction.")
                return
            self.positionx += directionx
            self.positiony += directiony
            #validating for speed input for control
            if speed > self.max_speed:
                print(f"Speed cannot exceed {self.max_speed} mph! Setting speed to {self.max_speed} mph.")
                speed = self.max_speed

            #updating the battery
            self.battery -= 5 * ((directionx + directiony) / 10)  #Battery usage increases with distance
            if self.battery < 20:
                print(f"Warning: {self.name} has low battery! Please recharge soon.")
            if self.battery < 0:
                print("Battery depleted! Please recharge before driving.")
            print(f"{self.name} drove {directionx+directiony} miles at {speed} mph, Battery level is now {self.battery}% and position is ({self.positionx}, {self.positiony}).")
        
        # making sure our ground robot has enough wheens for stability, and providing a warning if it doesn't.
        def check_wheels(self):
            if self.wheelcount < 4:
                print(f"Warning: {self.name} has only {self.wheelcount} wheels! Consider adding more for better stability.")
            else:
                print(f"{self.name} has {self.wheelcount} wheels, which is sufficient for stable movement.")
        

    # creating our done class, which will have the ability to fly and check its altitude.
class Drone(Robot):
        def __init__(self, name, battery, max_altitude, current_altitude, positionx, positiony):
            super().__init__(name, battery, positionx, positiony)
            self.max_altitude = max_altitude
            self.current_altitude = current_altitude
        #asking user for altitude and providing checks for max altitude and low battery warnings. Also includes a status update after flying.
        def fly(self, altitude, distancex, distancey):
            
            #validating user input for x and y direction for drone to move
            try:
                if distancex < 0 or distancey < 0:
                    raise ValueError("Drone cannot move to negative coordinates.")
            except ValueError:
                print("Error: Please enter valid numbers for direction.")
                return
            self.positionx += distancex
            self.positiony += distancey

            #validating user input for altitude for control
            if altitude > self.max_altitude:
                print(f"Altitude cannot exceed {self.max_altitude} feet! Setting altitude to {self.max_altitude} feet.")
                altitude = self.max_altitude
            elif altitude < 0:
                print("In order to fly you must be above ground level! Setting altitude to 0 feet.")
                altitude = 0
            self.current_altitude = altitude

            #updating the battery usage based off of altitude
            self.battery -= 10 * (altitude / 100)  #Battery usage increases with altitude
            if self.battery < 20:
                print(f"Warning: {self.name} has low battery! Please recharge soon.")
            print(f"{self.name} flew to {self.current_altitude} feet, Battery level is now {self.battery}%")

        def land(self):
            self.current_altitude = 0
            print(f"{self.name} has landed on ground, Battery level is now {self.battery}%")


    #defining our robot arm class
class RobotArm(Robot):
    def __init__(self, name, battery, positionx, positiony, joints, max_reach):
        super().__init__(name, battery, positionx, positiony)
        self.joints = joints
        self.max_reach = max_reach

    #making the extend function which will extend in order to grab or drop objects. 
    def extend(self, distance):
        #validating user input for distance to extend
        try:
            if distance < 0:
                raise ValueError("Robot arm cannot extend to negative distance.")
        except ValueError:
            print("Error: Please enter a valid number for distance.")
            return
        if distance > self.max_reach:
            print(f"Distance cannot exceed {self.max_reach} feet! Setting distance to {self.max_reach} feet.")
            distance = self.max_reach
        self.positionx += distance  # Assuming extension is in the x direction for simplicity
        self.battery -= 5 * (distance / 10)  #Battery usage increases with distance extended
        if self.battery < 20:
            print(f"Warning: {self.name} has low battery! Please recharge soon.")
        print(f"{self.name} extended {distance} feet, Battery level is now {self.battery}% and position is ({self.positionx}, {self.positiony}).")

    # grabs and drops the objects, and provides a status update after each action.
    def grab(self):
        print(f"{self.name} is grabbing an object, Battery level is now {self.battery}%")
    def release(self):
        print(f"{self.name} is releasing an object, Battery level is now {self.battery}%")


    # finally, will define fleet manager class, which manages multiple robots in fleet including adding and removing robots and reporting the status of the entire fleet.
class Fleet_Manager():
        def __init__(self):
            self.robots = []

        def add_robot(self, robot):
            self.robots.append(robot)
            print(f"{robot.name} has been added to the fleet!")

        def remove_robot(self, robot_name):
            for robot in self.robots:
                if robot.name == robot_name:
                    self.robots.remove(robot)
                    print(f"{robot.name} has been removed from the fleet!")
                    return
            print(f"No robot named {robot_name} found in the fleet.")

        def report_fleet_status(self):
            print("Fleet Status Report:")
            for robot in self.robots:
                robot.report_status()


#making sure our reports are saved using csv 

        def save_fleet_status(self, filename):
            with open(filename, 'w', newline='') as data_file:
                writer = csv.writer(data_file)
                writer.writerow(['Type', 'Name', 'Battery', 'PositionX', 'PositionY'])
                for robot in self.robots:
                    if isinstance(robot, GroundRobot):
                        writer.writerow(['GroundRobot', robot.name, robot.battery, robot.positionx, robot.positiony])
                    elif isinstance(robot, Drone):
                        writer.writerow(['Drone', robot.name, robot.battery, robot.positionx, robot.positiony])
                    elif isinstance(robot, RobotArm):
                        writer.writerow(['RobotArm', robot.name, robot.battery, robot.positionx, robot.positiony])