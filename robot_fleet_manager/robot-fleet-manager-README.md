# Robot Fleet Management System
This project demonstrates object-oriented programming principles applied to real-world robotics scenarios through managing robot fleets. Robots showcased were ground, drone, and robot arms.

# Project Overview
Manage multiple types of robots (ground robots, drones, robot arms)
Track battery levels and positions in real-time
Monitor robot-specific capabilities (wheel count, altitude, reach)
Add/remove robots from fleet
Generate fleet status reports

# Robot Types
Ground Robot: 
- Capabilities: Drive with configurable speed and wheel count
- Features: Speed limiting, wheel stability checks
- Battery Usage: 5% per 10 miles traveled

Drone:
- Capabilities: Fly to specified altitudes, land safely
- Features: Maximum altitude enforcement, altitude tracking
- Battery Usage: 10% per 100 feet of altitude

Robot Arm:
- Capabilities: Extend to grasp objects at various distances
- Features: Maximum reach enforcement, joint tracking
- Battery Usage: 5% per 10 inches extended

# Key OOP Concepts Demonstrated:
- Inheritance: Child classes (GroundRobot, Drone, RobotArm) inherit common functionality from Robot base class
- Polymorphism: Each robot type has specialized behavior while sharing a common interface
- Encapsulation: Robot state (battery, position) is managed internally with controlled access
- Composition: FleetManager contains and manages multiple Robot objects

# Core Features
Robot Base Class:
- Position tracking
- Battery management with low-battery warnings
- Movement with automatic battery deduction
- Recharge functionality with 100% cap
- Status reporting

# What I Learned
Python Skills:
- Designing class hierarchies with inheritance
- Using super() to extend parent class functionality
- Exception handling for robust error management
- String formatting for clean output
- List manipulation for fleet management

Software Engineering Principles
- DRY (Don't Repeat Yourself). Shared functionality in base class
- Single Responsibility Principle (each class has one clear purpose)
- Code reusability through inheritance
- Separation of concerns (robots vs fleet management)

Robotics Concepts
- Multi-robot system architecture
- Resource management (battery as constrained resource)
- Robot capability modeling (wheels, altitude, reach)

# Future Enhancements
Planned Features:
- File I/O: Loading fleet data to CSV files
- Search functionality: Find robots by type or battery level
- Battery alerts: Automatic low-battery notifications
- Mission assignments: Assign tasks to specific robots
- Collision detection: Prevent robots from occupying same position
- Performance metrics: Track total distance traveled, battery efficiency

#
This is a learning project please feel free to send any sort of criticism. Any is welcomed!
