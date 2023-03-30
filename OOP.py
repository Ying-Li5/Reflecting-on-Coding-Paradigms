# generate class named Podracer
# define them w/ max_speed, condition (perfect, trashed, repaired), and price attributes.
class Podracer:
  # __init__ is a constructor
  def __init__(self, max_speed, condition, price):
    # self - a parameter that reference to the current instance of the class (in this one the class is Podracer), and used to access variables that belongs to the class
    self.max_speed = max_speed
    self.condition = 'mint'
    self.price = price

    # define a repair method that will update the condition of the podracer to "repaired"
  def repair(self):
    self.condition = "repaired"
    print(f"The Podracer is now {self.condition}.")


# generate a new class called AnakinsPod that inherits Podracer.
# It should contain speical method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  # uses parameters of the parents?
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def boost(self):
    self.max_speed *= 2
    print(f"The AnakinsPod max speed is now {self.max_speed}.")


# generate another class called SebulbasPod that inherits Podracer.
# It should contain special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):

  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def flame_jet(self, other):
    other.condition: "trashed"
    print(f"What happened? The SebulbasPod is now {other.condition}!")


car = Podracer(10, "perfect", 100)
car.repair()

car2 = AnakinsPod(20, "trashed", 200)
car2.boost()

car3 = SebulbasPod(30, "repaired", 300)
car3.flame_jet(car2)

# OOP Prompt
# 1. How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
   # Inheritance - The parent class is Podracer. It inherits the properties and methods of the parents class which are (max_speed, condition, price). The child classes are AnakinsPod and SebulbasPod, which uses the super() method.
   # Polymorphism - This is used in AnakinsPod(Podracer), we did the product sign because the max speed is increased by 2.

# 2. Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
  # No, because OOP allows us to tracks the variable associated with Podracer a lot easier. 

# 3. How in particular did Object Oriented Programming assist in the solving of this problem?
   # OOP assisted in solving this problems because there was so many variable involved with Podracer that allowed us to implement those variable easier to avoid running into errors.