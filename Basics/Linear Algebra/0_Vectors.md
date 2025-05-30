
## Vectors

- [Introduction](#introduction)
- [Types of Vectors](#Types-of-Vectors)
- [2D and 3D Space in Vectors](#2D-and-3D-Space-in-Vectors)
- [Dot and Cross Products on Vectors](#Dot-and-Cross-Products-on-Vectors)
- [License](#license)

## Introduction
Vectors are not just mathematical abstractions; they represent quantities that have both magnitude and direction, making them essential in various fields such as physics, engineering, computer science, and data analysis.

A vector is a mathematical object that has both magnitude and direction. In a geometric context, a vector can be visualized as an arrow pointing from one point to another in space. 

## Types of Vectors

Vectors can be categorized into three types:

1. Geometric Vectors:

   Geometric vectors are directed line segments that illustrate quantities in physical space.
   
   ![image](https://github.com/user-attachments/assets/eeb1bb1a-2ff2-4254-85a2-93c247b0643b)

    Characteristics:
   
    Magnitude: The length of the vector, which can be measured in units such as meters or kilograms.
   
    Direction: The angle at which the vector points, which can be defined with other vectors or reference axes.

    ![image](https://github.com/user-attachments/assets/057dd3e4-d8af-488b-911d-de1e734ffefb)

3.  Polynomials
     Polynomials are mathematical expressions consisting of variables and coefficients, combined using addition, subtraction, and multiplication. They play a     crucial role in algebra, calculus, and machine learning applications.
    
    ![image](https://github.com/user-attachments/assets/9a2199c8-d7e4-430e-ab63-22cb60b65371)

  Degree of polynomial is determined by the highest exponent or power of the variable in the expression. It represents the highest degree term in the polynomial.

  ![image](https://github.com/user-attachments/assets/1b28e0a4-8784-4df6-9de1-b22240c7180a)

In a polynomial, we classify various terms into like terms and unlike terms.

Like terms are the terms that have the same variable and with same exponent.
Unlike terms are terms that have different variables or different powers(even with the same variable).

![image](https://github.com/user-attachments/assets/02605f06-e9a1-4a24-960e-9760678d5b20)

![image](https://github.com/user-attachments/assets/6954aad6-1615-4818-8d18-32b2c269d86e)


3. Ordered set of real numbers
     We learnt in Intro.md about this kind of vector, row vector and column vector.

     Zero Vector: A zero vector is a vector whose components are all zeros.
     Unit Vector: A unit vector is a vector that has a magnitude of one.
     Sparse Vector: A sparse vector is a vector in which most of the elements are zero.
     Basis Vectors: In a vector space, basis vectors are linearly independent vectors that span the space. For instance, in R3, the standard basis vectors are:
     Two vectors are orthogonal if their dot product is zero. For example, in R2:
   

![image](https://github.com/user-attachments/assets/6f2b627b-5503-4871-850b-d35964b7a084)


Normal Vector: A normal is an object that is perpendicular to a given object. It is a line or vector that intersects another object at a right angle. A normal vector is a vector that is perpendicular to a given surface or curve at a specific point. A unit normal vector is a normal vector whose length is 1

![image](https://github.com/user-attachments/assets/678da19a-b2fd-4000-959e-0721c8fd16cc)



## 2D and 3D Space in Vectors

2-dimensional Cartesian plane and 3-dimensional space in vectors

A **2D Cartesian plane** consists of two perpendicular axes:

- X-axis (horizontal)
- Y-axis (vertical)
A vector in 2D is represented as ( v = (x, y) ), where:
- ( x ) is the horizontal component.
- ( y ) is the vertical component.

Example in AI & Graphics:
- Image transformations like translation and rotation use 2D vectors.
- In physics, velocity is often represented as a 2D vector.

- Graphics, physics, machine learning

**3-Dimensional Space (ℝ³)**

A 3D space has three perpendicular axes:
- X-axis (left-right)
- Y-axis (up-down)
- Z-axis (depth)
A vector in 3D is represented as ( v = (x, y, z) ), where:
- ( x ), ( y ), and ( z ) define movement in three directions.
Example in AI & Physics:
- 3D object positioning in gaming and simulations.
- Machine learning applications involving spatial data (e.g., LiDAR).

- Gaming, robotics, spatial data analysis


## Dot and Cross Products on Vectors

Vectors can be multiplied in two ways:

- Scalar Product (Dot Product)
- Vector Product (Cross Product)

The result of the scalar product/dot product of two vectors is always a scalar quantity. This operation is useful for finding the angle between vectors and determining orthogonality.

![image](https://github.com/user-attachments/assets/9427bcf2-9a28-4260-b860-99083121a4ae)

- It is commutative: a⋅b = b⋅a
- It is distributive: a⋅(b+c) = a⋅b + a⋅c
- The dot product can provide a way to calculate the angle θ between two non-zero vectors a and b using the relationship:
  
  ![image](https://github.com/user-attachments/assets/fedbbbc2-b795-4d94-9190-427002605359)

   Where ∥a∥ and ∥b∥ are the magnitudes (lengths) of the respective vectors.


The **cross product**, also known as the vector product, is a way to combine two vectors in three-dimensional space. It is represented by the symbol “×”. When you have two vectors, a and b, that are not in the same direction (meaning they are linearly independent), the cross product a × b gives you a new vector that is perpendicular to both a and b, meaning it forms a right angle (90 degrees) with both of them.

![image](https://github.com/user-attachments/assets/2cca87ee-a00f-4fbe-a1af-2f378e88a0f9)

If A and B are two independent vectors, then the result of the cross product of these two vectors (A x B) is perpendicular to both the vectors and normal to the plane that contains both vectors. We say that 2 vectors are **orthogonal** if they are perpendicular to each other.

Note: If the two vectors are not independent (for example, if they are parallel or one is a multiple of the other), the cross product a × b will be zero. This means there is no unique vector that is perpendicular to both, as they lie along the same line.

![image](https://github.com/user-attachments/assets/af3115aa-327f-4276-a77d-bb1ced85be55)

- Not commutative: A×B = −(B×A)
- Distributive: A×(B+C)= A×B + A×C

  
