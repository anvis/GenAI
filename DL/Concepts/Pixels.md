***Concept of Pixels***

A pixel (short for picture element) is the smallest unit of a digital image. Think of it as a tiny square of color. When you zoom into any image far enough, you’ll see a grid of these squares — each one holding a specific color value.
- A pixel doesn’t have physical size — its size depends on the resolution and display.
- It represents intensity (in grayscale) or color (in RGB or other formats).

---

Each pixel stores numerical values that define its appearance:

**Grayscale Image (Black & White)**
   
- Each pixel holds a single intensity value.
- Typically ranges from 0 to 255:
- 0 → black
- 255 → white
- Values in between → shades of gray

**Color Image (RGB)**
   
- Each pixel holds three values:
- R (Red), G (Green), B (Blue)
- Each channel ranges from 0 to 255
- Example: (255, 0, 0) → pure red
  
So a color pixel is a triplet of values, while a grayscale pixel is a single value.

---

An image of 1920×1080 has:
- Width = 1920 pixels
- Height = 1080 pixels
- Total = 2,073,600 pixels

---

In memory, images are stored as 2D arrays (grayscale) or 3D arrays (color):

GreyScale:

``` python
[[  0,  50, 100],
 [150, 200, 255]]
```

RGB:

``` python
[[[255, 0, 0], [0, 255, 0]],
 [[0, 0, 255], [255, 255, 0]]]

Each [R, G, B] triplet is one pixel.

```

---

- In convolution, you apply filters to local pixel neighborhoods.
- In segmentation, you classify each pixel.
- In GANs, you generate pixel values from noise.
  
Pixels are the raw material of visual intelligence.
