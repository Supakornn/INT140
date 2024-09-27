# W7c05_iteration_thuW7
# 041 Supakorn Ieamgomol
# 043 Somchai Wantaeng
# 050 Sirinda Charoenwai
# 051 Siriyakon Sangkaew

def song(n :int) -> str: 
    if  n < 0 or n > 9 :
        raise ValueError("n must be more than 0 and less than 9")
    
    result = ""
    for i in range(1, n+1): 
        for j in range(i, n+1):
            result += str(j)
        result += "\n"
    return result

n = int(input("Enter n: "))
print(song(n))



# def song(n):
#     if n < 0 or n > 9:

#         raise ValueError("n must be more than 0 and less than 9")
#     i = 1
#     while i <= n:
#         j = i
#         while j <= n:
#             print(j, end="")
#             j += 1
#         print()
#         i += 1

# song(8)

