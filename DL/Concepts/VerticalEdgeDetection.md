***Vertical edge detection***

Vertical edge detection is the process of identifying sharp changes in pixel intensity along the horizontal direction, which correspond to vertical lines or boundaries in an image.

We use a convolutional kernel (filter) designed to highlight vertical changes. The most common one is the Sobel operator or a simple difference kernel.

🔧 Example Kernel for Vertical Edges:

[-1,  0,  1]
[-2,  0,  2]
[-1,  0,  1]

Imagine a vertical black line on a white background:

[255, 255, 0, 0, 0, 255, 255]

The pixel intensity drops sharply from white (255) to black (0). A vertical edge detector will catch this change by comparing left and right neighbors.

The Vertical Edge Detection helps us to identify if the shade of the image is moving from light to dark or dark to light.

- Light to Dark --> Pixel will Decrease
- Dark to Light --> Pixel will Increase

- For Black and White Images it is easy as each pixel holds only 0 or 255, when Number changes we can identify the difference. 
- For RGB Image we need to identify with the help of kernel or a filter to idntify how shade is changing.

We have different filters available for vertical, horizantal, circles, shapes etc..,
**All boils down to convolution, where we use filter to identify the edges, patterns in the image by using filter / kernel.**

