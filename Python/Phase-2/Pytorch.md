
## PyTorch
PyTorch is a dynamic and powerful tool for building and training machine learning models. It simplifies the process with its fundamental building blocks like tensors and neural networks and offers effective ways to define objectives and improve models using loss functions and optimizers. By leveraging PyTorch, anyone can gain the skills to work with large amounts of data and develop cutting-edge AI applications.

### PyTorch Tensors
PyTorch tensors are crucial tools in the world of programming and data science, which work somewhat like building blocks helping to shape and manage data effortlessly. These tensors allow us to deal with data in multiple dimensions, which is especially handy when working with things like images or more complex structures. 

**Definition of Tensors**
Tensors are multi-dimensional arrays that can hold data in various dimensions, similar to vectors and matrices but with the capability to have more than two dimensions.

**Types of Data**
Tensors can store different types of data, including scalar values, vectors, and higher-dimensional entities. They are essential for representing data in machine learning tasks.

**Creation of Tensors**
You can create tensors in PyTorch, including initializing them with random values or specific data types.
```python
import torch 

# Create a 3-dimensional tensor 
images = torch. rand((4, 28, 28)) 

# Get the second image 
second_image = images (1]
```

**Operations on Tensors**
Tensors support a wide range of operations, such as addition, multiplication, and reshaping, which are crucial for performing computations in deep learning models.

```python
a = torch.tensor([[1,  1],  [1,  0]])  
print(a)  
# tensor([[1, 1],  
#	      [1, 0]])  

print(torch.matrix_power(a,  2))  
# tensor([[2, 1],  
#	 	  [1, 1]])  

print(torch.matrix_power(a,  3))  
# tensor([[3, 2],  
# 	 	  [2, 1]])  

print(torch.matrix_power(a,  4))  
# tensor([[5, 3],  
#		  [3, 2]])
```

**Visualization**
You can display an image from a tensor using the Matplotlib library.
```python
import matplotlib.pyplot as plt 

# Display the image 
plt. imshow(second_image, cmap='gray') 
plt.axis('off') # disable axes 
plt. show()
```

#### Key Concepts
**Tensors**: Generalized versions of vectors and matrices that can have any number of dimensions (i.e. multi-dimensional arrays). They hold data for processing with operations like addition or multiplication.

**Matrix operations:**  Calculations involving matrices, which are two-dimensional arrays, like adding two matrices together or multiplying them.

**Scalar values:**  Single numbers or quantities that only have magnitude, not direction (for example, the number 7 or 3.14).

**Linear algebra:**  An area of mathematics focusing on vector spaces and operations that can be performed on vectors and matrices.


### PyTorch Neural Networks
Neural networks are computational models inspired by the human brain, consisting of interconnected nodes (neurons) organized in layers. Each neuron processes input data and passes its output to the next layer.

**Structure**:
* **Input Layer**: The first layer that receives input data.
* **Hidden Layers**: Intermediate layers where computations occur. There can be multiple hidden layers in a deep neural network.
* **Output Layer**: The final layer that produces the output or prediction based on the processed data.

**Activation Functions**
These functions determine whether a neuron should be activated (i.e., produce an output) based on the input it receives. Common activation functions include ReLU (Rectified Linear Unit) and sigmoid functions.

**Training Process**
* **Forward Propagation**: Input data is passed through the network, layer by layer, to generate an output.
* **Loss Function**: A metric that measures the difference between the predicted output and the actual target value. The goal is to minimize this loss during training.
* **Backpropagation**: A method used to update the weights of the network based on the error calculated from the loss function. This involves calculating gradients and adjusting weights to improve accuracy.

**Applications**
Neural networks are widely used in various applications, including image recognition, natural language processing, and game playing, due to their ability to learn complex patterns from data.

**Code Example**
```python
import torch.nn as nn 

class  MLP(nn.Module):
	def  __init__(self, input_size):
		super(MLP, self).__init__()
		self.hidden_layer = nn.Linear(input_size,  64)
		self.output_layer = nn.Linear(64,  2) 
		self.activation = nn.ReLU()
	
	def  forward(self, x):
		x = self.activation(self.hidden_layer(x))
		return self.output_layer(x)  model = 

MLP(input_size=10)
print(model)

# MLP(  
#	 (hidden_layer): 
#	Linear(in_features=10, out_features=64, bias=True)  
#	 (output_layer):
#	Linear(in_features=64, out_features=2, bias=True)  
# 	(activation):
#	ReLU()
# )

model.forward(torch.rand(10))
# tensor([0.2294, 0.2650], grad_fn=<AddBackward0>)
```


### PyTorch Loss Functions
PyTorch loss functions are essential tools that help in improving the accuracy of a model by measuring errors. These functions come in different forms to tackle various problems, like deciding between categories (classification) or predicting values (regression).

**Purpose of Loss Functions**
Loss functions quantify the difference between the predicted outputs of a model and the actual target values. They are essential for measuring how well the model is performing.

**Common Loss Functions**
-   **Cross-Entropy Loss**: Used primarily for classification tasks, it measures how well the predicted probabilities align with the actual classes. It's particularly effective when classes are mutually exclusive.
-   **Mean Squared Error (MSE)**: Commonly used for regression tasks, it calculates the average of the squared differences between predicted and actual values.

**Minimizing Loss**
The goal during training is to minimize the loss value, which indicates that the model's predictions are becoming more accurate.

**Implementation in PyTorch**
We can also see how to implement these loss functions using PyTorch's `torch.nn` module.

**Importance of Choosing the Right Loss Function**
Selecting an appropriate loss function is crucial as it impacts the model's ability to generalize and perform well on unseen data.

#### Code Examples

##### Cross-Entropy Loss

```python
import torch 
import torch.nn as nn 

loss_function = nn.CrossEntropyLoss()  

# Our dataset contains a single image of a dog, where  
# cat = 0 and dog = 1 (corresponding to index 0 and 1)  
target_tensor = torch.tensor([1])  
target_tensor 
# tensor([1])
```

Prediction: Most likely a dog (index 1 is higher)
```python
# Note that the values do not need to sum to 1  
predicted_tensor = torch.tensor([[2.0,  5.0]])  
loss_value = loss_function(predicted_tensor, target_tensor)  
loss_value 
# tensor(0.0181)
```

Prediction: Slightly more likely a cat (index 0 is higher)
```python
predicted_tensor = torch.tensor([[1.5,  1.1]])  
loss_value = loss_function(predicted_tensor, target_tensor)
loss_value 
# tensor(0.9130)
```

##### Mean Squared Error Loss
```python
# Define the loss function  
loss_function = nn.MSELoss()  

# Define the predicted and actual values as tensors  
predicted_tensor = torch.tensor([320000.0])  
actual_tensor = torch.tensor([300000.0])  

# Compute the MSE loss  
loss_value = loss_function(predicted_tensor, actual_tensor)
print(loss_value.item())  
# Loss value: 20000 * 20000 / 1 = ...  
# 400000000.0
```


### PyTorch Optimizers
PyTorch optimizers are important tools that help improve how a neural network learns from data by adjusting the model's parameters. By using these optimizers, like stochastic gradient descent (SGD) with momentum or Adam, we can quickly get started learning!

**Reinforcement Learning**
RL is a type of machine learning where an agent learns to make decisions by interacting with an environment. The agent receives feedback in the form of rewards or penalties based on its actions.

**Components of RL**
-   **Agent**: The learner or decision-maker.
-   **Environment**: The context within which the agent operates.
-   **Actions**: Choices made by the agent that affect the environment.
-   **Rewards**: Feedback received from the environment, guiding the agent's learning.

**Learning Process**
-   The agent explores different actions to discover which ones yield the highest rewards.
-   Over time, the agent learns to optimize its strategy to maximize cumulative rewards through trial and error.

**Exploration vs. Exploitation**
The agent must balance exploring new actions to find better rewards (exploration) with leveraging known actions that yield high rewards (exploitation).

**Applications of RL**
RL is used in various fields, including robotics, game playing (e.g., AlphaGo), and autonomous vehicles, where decision-making in dynamic environments is crucial.

#### Code Examples

Assuming  `model`  is your defined neural network.
`lr=0.01`  sets the learning rate to 0.01 for either optimizer.

```python
import torch.optim as optim
```

#####  Stochastic Gradient Descent
```python
# momentum=0.9 smoothes out updates and can help training 
optimizer = optim.SGD(
					model.parameters(), 
					lr=0.01, 
					momentum=0.9
					)
```
##### Adam
```python
optimizer = optim.Adam(model.parameters(), lr=0.01)
```


### PyTorch Datasets and Data Loaders

**Data Augmentation**
Data augmentation is a technique used to artificially expand the size of a training dataset by creating modified versions of existing data. This helps improve the model's ability to generalize to new, unseen data.

**Importance**
Augmenting data is crucial when the available dataset is small, as it can help prevent overfitting, where the model learns to perform well on the training data but fails to generalize to new data.

**Common Techniques**
-   **Image Augmentation**: Techniques include rotation, flipping, scaling, cropping, and colour adjustments. These transformations create variations of images while preserving their labels.
-   **Text Augmentation**: Methods may involve synonym replacement, random insertion, or back-translation to generate diverse text samples.

**Benefits**
By increasing the diversity of the training data, data augmentation can lead to improved model performance, robustness, and accuracy in real-world applications.

#### Code Examples

##### Datasets
```python
from torch.utils.data import Dataset 

# Create a toy dataset  
class  NumberProductDataset(Dataset):
	def  __init__(self, data_range=(1,  10)):
		self.numbers = list(range(data_range[0],data_range[1]))
	
	def  __getitem__(self, index):
		number1 = self.numbers[index]
		number2 = self.numbers[index]  +  1
		return  (number1, number2), number1 * number2 
	
	def  __len__(self):
	return  len(self.numbers)  

# Instantiate the dataset  
dataset = NumberProductDataset(
	data_range=(0,  11)
)  
# Access a data sample  
data_sample = dataset[3]
print(data_sample)
# ((3, 4), 12)
```

##### Data Loaders
```python
from torch.utils.data import DataLoader 

# Instantiate the dataset  
dataset = NumberProductDataset(data_range=(0,  5))  

# Create a DataLoader instance  
dataloader = DataLoader(dataset, batch_size=3, shuffle=True)  

# Iterating over batches  
for  (num_pairs, products)  in dataloader:
	print(num_pairs, products)
# [tensor([4, 3, 1]), tensor([5, 4, 2])] tensor([20, 12, 2]) 
# [tensor([2, 0]), tensor([3, 1])] tensor([6, 0])
```


### PyTorch Training Loops
A PyTorch training loop is an essential part of building a neural network model, which helps us teach the computer how to make predictions or decisions based on data. By using this loop, we gradually improve our model's accuracy through a process of learning from its mistakes and adjusting.

The training loop is a cycle that the model goes through multiple times to learn from the data. It involves several key components, including the dataset, model, loss function, and optimizer.

**Epochs and Batches**
-   **Epoch**: One complete pass through the entire training dataset.
-   **Batch**: A subset of the training data used to update the model's weights during each iteration.

**Steps in the Training Loop**
1. Initialize the total loss to zero at the beginning of each epoch.
2. Iterate over batches of data, making predictions with the model.
3. Calculate the loss by comparing the model's predictions to the actual target values.
4. Update the total loss and adjust the model's weights using the optimizer based on the calculated loss.

**Monitoring Progress**
After each epoch, the training loop can print the loss to monitor the model's performance over time, ideally showing a decrease in loss as the model learns.

#### Code Examples

##### Create a Number Sum Dataset

This dataset has two features—a pair of numbers—and a target value—the sum of those two numbers.

Note that this is  _not_  actually a good use of deep learning. At the end of our training loop, the model still doesn't know how to add 3 + 7! The idea here is to use a simple example so it's easy to evaluate the model's performance.
```python
import torch 
import torch.nn as nn 
import torch.optim as optim 
from torch.utils.data import Dataset, DataLoader 

class  NumberSumDataset(Dataset):
	def  __init__(self, data_range=(1,  10)):
		self.numbers =  list(range(data_range[0], data_range[1]))
	
	def  __getitem__(self, index):
		number1 =  float(self.numbers[index //  len(self.numbers)])
		number2 =  float(self.numbers[index %  len(self.numbers)])
		return torch.tensor([number1, number2]), torch.tensor([number1 + number2])
	
	def  __len__(self):
		return  len(self.numbers)  **  2
```

##### Inspect the Dataset
```python
dataset = NumberSumDataset(data_range=(1,  100))

for i in  range(5):
	print(dataset[i])

# (tensor([1., 1.]), tensor([2.]))
# (tensor([1., 2.]), tensor([3.]))  
# (tensor([1., 3.]), tensor([4.]))  
# (tensor([1., 4.]), tensor([5.]))  
# (tensor([1., 5.]), tensor([6.]))
```

##### Define a Simple Model
```python
class  MLP(nn.Module):
	
	def  __init__(self, input_size):
		super(MLP, self).__init__()
		self.hidden_layer = nn.Linear(input_size,  128)
		self.output_layer = nn.Linear(128,  1)
		self.activation = nn.ReLU()
	
	def  forward(self, x):
		x = self.activation(self.hidden_layer(x))
		return self.output_layer(x)
```

##### Instantiate Components Needed for Training
```python
dataset = NumberSumDataset(data_range=(0,  100))
dataloader = DataLoader(dataset, batch_size=100, shuffle=True)
model = MLP(input_size=2)
loss_function = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

##### Create a Training Loop
```python
for epoch in  range(10):
	total_loss =  0.0
	for number_pairs, sums in dataloader:  # Iterate over the batches
		predictions = model(number_pairs)  # Compute the model output
		loss = loss_function(predictions, sums)  # Compute the loss
		loss.backward()  # Perform backpropagation  
		optimizer.step()  # Update the parameters  
		optimizer.zero_grad()  # Zero the gradients  
	
		total_loss += loss.item()  # Add the loss for all batches  
	
	# Print the loss for this epoch  
	print("Epoch {}: Sum of Batch Losses = {:.5f}".format(epoch, total_loss))  

# Epoch 0: Sum of Batch Losses = 118.82360  
# Epoch 1: Sum of Batch Losses = 39.75702  
# Epoch 2: Sum of Batch Losses = 2.16352  
# Epoch 3: Sum of Batch Losses = 0.25178  
# Epoch 4: Sum of Batch Losses = 0.22843  
# Epoch 5: Sum of Batch Losses = 0.19182  
# Epoch 6: Sum of Batch Losses = 0.15507  
# Epoch 7: Sum of Batch Losses = 0.07789  
# Epoch 8: Sum of Batch Losses = 0.06329  
# Epoch 9: Sum of Batch Losses = 0.04936
```

##### Try the Model Out
```python
# Test the model on 3 + 7  
model(torch.tensor([3.0,  7.0]))  

# tensor([10.1067], grad_fn=<AddBackward0>)
```


