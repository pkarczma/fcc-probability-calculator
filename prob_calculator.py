import copy
import random
# Consider using the modules imported above.

class Hat:

    contents = []

    def __init__(self, **kwargs):
        self.contents = []
        for color, value in kwargs.items():
            for val in range(value):
                self.contents.append(color)

    def draw(self, nballs):
        if nballs >= len(self.contents):
            balls_list = copy.deepcopy(self.contents)
            self.contents = []
            return balls_list
        balls_list = random.sample(self.contents, nballs)
        for ball in balls_list:
            self.contents.remove(ball)
        return balls_list

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