import copy
import random
# Consider using the modules imported above.

class Hat:

    contents = []

    def __init__(self, **kwargs):
        self.contents = []
        # Add contents of the hat based on the parameters provided
        for color, value in kwargs.items():
            for val in range(value):
                self.contents.append(color)

    # Method for drawing from the hat
    def draw(self, nballs):
        # Take the whole hat in case we request for all balls
        if nballs >= len(self.contents):
            balls_drawn = copy.deepcopy(self.contents)
            self.contents = []
            return balls_drawn
        balls_drawn = random.sample(self.contents, nballs)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successes = 0
    for iexperiment in range(num_experiments):
        random.seed(iexperiment)
        full_hat = copy.deepcopy(hat)
        balls_drawn = full_hat.draw(num_balls_drawn)
        success = True
        for color, value in expected_balls.items():
            if balls_drawn.count(color) < value:
                success = False
                break
        if success == True:
            num_successes += 1
    return num_successes / num_experiments