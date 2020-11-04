import copy
import random

class Hat:

    contents = []

    def __init__(self, **kwargs):
        self.contents = []
        # Add contents of the hat based on the parameters provided
        for color, value in kwargs.items():
            for val in range(value):
                self.contents.append(color)

    # Method for drawing balls from the hat
    def draw(self, nballs):
        # Take the whole hat contents in case we request for all balls
        if nballs >= len(self.contents):
            # Make a deep copy of hat contents
            balls_drawn = copy.deepcopy(self.contents)
            # Remove all balls from the hat contents
            self.contents = []
            # Return balls drawn
            return balls_drawn
        # Get a random sample of 'nballs' balls from the hat contents
        balls_drawn = random.sample(self.contents, nballs)
        # Remove balls drawn from the hat
        for ball in balls_drawn:
            self.contents.remove(ball)
        # Return balls drawn
        return balls_drawn

# Function for performing experiments
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successes = 0
    # Loop over each experiment
    for iexperiment in range(num_experiments):
        random.seed(iexperiment)
        # Make a deep copy of a hat
        full_hat = copy.deepcopy(hat)
        # Make a draw from the hat
        balls_drawn = full_hat.draw(num_balls_drawn)
        # Check if we succeeded to draw expected balls
        success = True
        for color, value in expected_balls.items():
            if balls_drawn.count(color) < value:
                success = False
                break
        # Increase number of successes
        if success == True:
            num_successes += 1
    # Return estimated probability
    return num_successes / num_experiments