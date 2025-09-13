
class Jedi:
    """A Jedi, who uses the Force for good."""
    def introduce(self):
        print("I am a Jedi Knight.")

    def use_the_force(self):
        print("I use a Force Push to open the door!")


class Sith:
    """A Sith, who uses the Force for power."""
    def introduce(self):
        print("I am a Sith Lord.")

    def use_the_force(self):
        print("I use a Force Choke to open the door... wait, what?")


class ProtocolDroid:
    """A droid that mimics force abilities."""
    def introduce(self):
        print("I am a protocol droid, "
              "fluent in six million forms of communication.")

    def use_the_force(self):
        print("I use a hydraulic piston to open the door. Beep boop.")


def conduct_training(trainee):
    """
    A function that trains any object with a `use_the_force` method.
    This is where polymorphism happens!
    """
    trainee.introduce()
    trainee.use_the_force()
    print("Training exercise complete!\n")




# Create instances of different classes.
luke = Jedi()
vader = Sith()
c3po = ProtocolDroid()

# Conduct the training. The `conduct_training` function
# doesn't care about the type of object, only that it has the
# `use_the_force` method.
conduct_training(luke)
conduct_training(vader)
conduct_training(c3po)