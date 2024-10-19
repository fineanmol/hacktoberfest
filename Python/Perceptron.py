import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Perceptron:
    def __init__(self, learning_rate=0.1, max_iters=100):
        # Initialize parameters
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.weights = None
        self.bias = None
        self.history = []

    def sigmoid(self, x):
        # Sigmoid activation function
        return 1 / (1 + np.exp(-x))

    def fit(self, X, y):
        # Initialize weights and bias
        n_samples, n_features = X.shape
        self.weights = np.random.randn(n_features)
        self.bias = 1

        for _ in range(self.max_iters):
            correct_classifications = True  # Track if all predictions are correct

            for i, x_i in enumerate(X):
                # Compute linear combination and apply sigmoid
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_pred = self.sigmoid(linear_output)

                # Classify based on sigmoid output
                predicted_label = 1 if y_pred >= 0.5 else 0

                # If misclassified, update weights and bias
                if predicted_label != y[i]:
                    correct_classifications = False
                    error = y[i] - y_pred
                    self.weights += self.learning_rate * error * x_i
                    self.bias += self.learning_rate * error

                # Store history for visualization
                self.history.append((self.weights.copy(), self.bias))

            # Stop if all samples are classified correctly
            if correct_classifications:
                break

    def get_history(self):
        # Return history of updates
        return self.history

def animate(i):
    # Get weights and bias for the current iteration
    weights, bias = history[i]
    ax.clear()
    
    # Plot data points
    for j in range(len(y)):
        if y[j] == 1:
            ax.scatter(X[j, 0], X[j, 1], marker='o', color='blue', s=100)
        else:
            ax.scatter(X[j, 0], X[j, 1], marker='x', color='red', s=100)

    # Plot decision boundary
    x_values = np.linspace(min(X[:, 0])-1, max(X[:, 0])+1, 100)
    y_values = -(weights[0] * x_values + bias) / weights[1]
    ax.plot(x_values, y_values, color='green')

    ax.set_xlim(min(X[:, 0])-2, max(X[:, 0])+2)
    ax.set_ylim(min(X[:, 1])-2, max(X[:, 1])+2)
    ax.set_title(f'Iteration {i+1}')

# Training data
X = np.array([[2, 1], [-2, -1], [1, -2], [-1, -2], [2, -1], [-1, 1], [3, 4]])
y = np.array([1, 0, 1, 0, 1, 0, 0])

# Train perceptron model
perceptron = Perceptron(learning_rate=0.1, max_iters=100)
perceptron.fit(X, y)

# Get history of weight updates for animation
history = perceptron.get_history()

# Set up plot for animation
fig, ax = plt.subplots()
plt.grid(True)
ani = FuncAnimation(fig, animate, frames=len(history), interval=500, repeat=False)
plt.show()
