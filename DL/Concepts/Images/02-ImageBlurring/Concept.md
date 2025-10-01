
***Image blurring***

Image blurring is a technique used to reduce image detail and noise. 
It smooths out rapid changes in pixel intensity, making edges less sharp and the image appear softer.

Blurring is typically achieved using low-pass filters in convolution operations:
- Low-pass filter: Allows low-frequency components (smooth areas) to pass through while attenuating high-frequency components (edges and noise).
- Kernel (Filter): A small matrix (e.g., 3×3 or 5×5) used to average pixel values in a neighborhood.

Usually 9 side by side pixels were converted to one pixel by taking average value of each pixel, as we know each pixel represent color value.

Sample Filter

<img width="346" height="240" alt="image" src="https://github.com/user-attachments/assets/1fca2a06-cc01-409e-bcb2-64d7dd2af899" />

