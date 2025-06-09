
Batch normalization and dropout are techniques used in neural networks to improve training stability and prevent overfitting.

### **Batch Normalization**
Batch normalization normalizes the inputs of each layer by adjusting the mean and variance of activations. This helps stabilize training and speeds up convergence. It works by:
1. **Calculating Mean & Variance** of activations over a batch.
2. **Normalizing Values** using these statistics.
3. **Scaling & Shifting** the normalized values with learnable parameters to maintain expressiveness.

- Neural networks can have issues with inconsistent learning rates across layers, making training slow or unstable.  
- Batch normalization helps by normalizing the activations of each layer, ensuring stable learning.  
- It reduces internal covariate shift, making the optimization process more efficient and allowing deeper networks to train faster.
  
**Benefits:**
- Improves training speed.
- Reduces dependence on careful initialization.
- Helps prevent vanishing/exploding gradients.

### **Dropout**
Dropout randomly deactivates neurons during training, forcing the network to learn more robust features. 
This prevents over-reliance on specific neurons and enhances generalization.

- Overfitting occurs when a model memorizes training data instead of generalizing patterns.  
- Dropout randomly deactivates neurons during training, forcing the network to learn more robust features rather than relying on specific pathways.  
- This prevents dependencies on individual neurons, improving generalization and reducing overfitting.  

**How it Works:**
- At each training step, a fraction of neurons are "dropped" (set to zero).
- The remaining neurons process the data as usual.
- During inference (prediction), all neurons are active.

**Benefits:**
- Reduces overfitting.
- Encourages diverse feature learning.
- Improves generalization in deep networks.

Both techniques complement each other—batch normalization stabilizes training, while dropout ensures robustness. 

