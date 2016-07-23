# Pythonic

## Object-Oriented Programming

- A programming paradigm that organizes software design around objects.
- Class (Blueprint) or Object = State + Behavior

### Features of OOP

- Class - Blueprint for creating objects.
- Object - Instance created from the class.
- Encapsulation - Bundling of data and methods that act on that data into a single unit (class). [properties and behaviors OR attributes and methods OR data and actions]
- Data Abstraction - Show only the essential attributes (Interfaces) and hide unnecessary details from the user (Implementation).
- Inheritance
- Polymorphism
- Dynamic Binding
- Message Passing

### Advantages of OOP

- Modularity - Independent modules (Classes or Blueprints or objects)
- Extensibility - Objects can be extended to include new attributes and behavior.
- Reusability - Faster development and less cost of developement
- Maintainablity - Since the design is modular, we can make changes to the modules without making large-scale changes.
- Higher quality software - More time and resources can be used to test the software.
- Overall it improves software-development productivity.

### Classes

- Blueprint for creating objects.
- YOU design the class = state + behavior of the object.
- Class ~ Abstract, Instance ~ Concrete

### Identify classes in a problem statement

- Problem statement
- Identify objects
- Identify state + behavior for each objects.
- Create blueprints or classes

### Instances

- Objects created from the class.
- Instance Attributes vs Class Attributes

### Constructor - __init__()

- Special method used to define the initial state of the object when it's created.
- It is called automatically when an instance is created.

### Encapsulation

- Purpose of class (unit) that contains attributes and methods is to restrict access from outside of that unit (Information-hiding principle).
- Class prevents direct access to the attributes in order to avoid making potentially problematic changes to the state.
- Outside world can only see public members of the class.
- Getters and Setters are specific methods that help us follow information-hiding principle by protecting the data and providing an indirect way to access that data.

### Data Abstraction

- Let's us hide the complexity of internal implementation of the class from the user.
- Class = Interface + Implementation
- Interface - The "visible" part of the class that the program can interact with. It's basically what features to show from that class.
- Implementation - The internal part of the class with the code that performs the functionality behind the scenes. It is the actual code that makes all functionality of the class work.
- In the class, we choose to expose only the members that should be exposed and all other members are non-public which can't/shouldn't be accessed from outside of the class.
- User --> Blackbox(class) --> Effect - A user of the class knows how to interact with the blackbox but doesn't know the details of the internal implementation of the class. He/She only knows the effect that the blackbox will have. This way we are hiding the implementation from the user and we can change it without affecting how the user interacts with a member of the class.
- IMPORTANT: Abstraction also allows us to abstract out common parts of the code to avoid repetition (Inheritance - Reusability) - Representations of more abstract objects. Ex: Dog class
