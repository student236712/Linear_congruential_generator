import time
import matplotlib.pyplot as plt
import numpy as np


def random(m, a, c, index):
    return ((index * a) + c) % m


def randomly_generated(m, c, a, initial_index):
    outputs = []
    counter = 0
    x = 0
    while True:
        if counter == 0:
            x = random(m, a, c, initial_index)
        else:
            x = random(m, a, c, x)

        if outputs.__contains__(x):
            break
        outputs.append(x)
        counter += 1

    return outputs


m = np.power(2, 10)
a = 225
c = 0
initial = time.time_ns()
generated_numbers = randomly_generated(m=m, c=c, a=a, initial_index=initial)
plt.scatter(np.arange(len(generated_numbers)), generated_numbers)
plt.grid(True)
plt.ylabel('Numbers generated using random generator')
plt.xlabel('Step')
plt.title('Numbers generated using params: ' + 'm= ' + str(m) + ', a= ' + str(a) + ', c= ' + str(c))
plt.savefig('Linear_congruential_generator_run_8.png')
plt.show()
