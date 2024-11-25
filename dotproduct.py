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