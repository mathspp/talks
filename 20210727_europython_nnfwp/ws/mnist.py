# MNIST
# “Hello, world!” of machine learning.

import csv
import numpy as np
from nn import Layer, Network, LeakyReLU, MSE


def load_data(path):
    """Load MNIST data from the given path."""
    with open(path, "r") as f:
        data = np.asarray(list(csv.reader(f)), dtype=float)
    return data


def to_col(array):
    return array.reshape((array.size, 1))


def test(net, test_data):
    """Compute the accuracy of the network on the given test data."""
    hits = 0
    for row in test_data:
        x = to_col(row[1:])
        out = net.forward_pass(x)
        guess = np.argmax(out)
        if guess == row[0]:
            hits += 1
    return hits/test_data.shape[0]


def train(net, train_data):
    """Train the network on the given training data."""

    ts = np.eye(10)

    for i, row in enumerate(train_data):
        if i % 1000 == 0:
            print(i)

        digit = row[0]
        x = to_col(row[1:])
        t = to_col(ts[int(digit), :])
        net.train(x, t)


if __name__ == "__main__":
    layers = [
        Layer(784, 16, LeakyReLU(0.1)),
        Layer(16, 16, LeakyReLU(0.1)),
        Layer(16, 10, LeakyReLU(0.1)),
    ]
    net = Network(layers, 0.001, MSE())

    # Test the network.
    test_data = load_data("mnistdata/mnist_test.csv")
    accuracy = test(net, test_data)
    print(f"Accuracy: {round(100 * accuracy, 2)}%")

    # Train the network.
    train_data = load_data("mnistdata/mnist_train.csv")
    train(net, train_data)

    # Test the network again.
    accuracy = test(net, test_data)
    print(f"Accuracy: {round(100 * accuracy, 2)}%")
