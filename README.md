# Markdown assignment 
## Daksh Mittal 
### 2023ucp1581 

In this article we will learn about:
- [x] What is a vector? 
- [ ] Different types of vectors 
- [ ] Dot product 
- [ ] Cross product 
- [ ] More 

**What is a vector?** 
A vector is a quantity that has both magnitude and direction. It is typically represented 
as an arrow, where the length of the arrow indicates the magnitude (size or amount) and 
the direction of the arrow shows the direction of the vector. 

>Vector is different from scalar. 
![Dot Product of Two 
vectors](https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/dot-product
of-vectors-1626103027.png) 
Link to this image: [Click 
here](https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/dot-product-of
vectors-1626103027.png) 
**Types of vectors:** - 2 dimensional - 3 dimensional - n dimensional 
**Magnitude of vector:** 
$$\| \mathbf{v} \| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$$ 
*Dot product* 
The dot product of two vectors is the product of the magnitude of the two vectors and 
the cos of the angle between them. 
>[!NOTE] 
>a.b=|a||b| cosθ 
*Cross product* 
The cross product (also called the vector product) is a mathematical operation between 
two vectors in three-dimensional space that produces a new vector that is 
perpendicular to both of the original vectors. 
>[!NOTE] 
>a x b=|a||b| sinθ 
Here is the code for implementing dot product[^1]. 
[^1]: import numpy as np  
Taking two scalar values  
a=5+2i 
b=7+9i 
print(np.dot(a, b)) 
### Table showing difference between dot and cross product: 
|Dot product|Cross product| 
|:---:|:---:| 
|Produces a scalar (single number)|Produces a vector| 
|No direction|Direction is defined| 
|Finding projections, angles, and work done|Computing torque, angular momentum, 
and normals to planes| 
***Code:*** 
``` 
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    
    return sum(a * b for a, b in zip(vector1, vector2))

# Example usage
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
result = dot_product(vector1, vector2)
print("Dot Product:", result)

#Modified This File 
#By Adding Parallelism
#FIXED THE BUG 
``` 
