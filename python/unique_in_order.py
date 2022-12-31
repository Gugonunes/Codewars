"""
Implement the function unique_in_order which takes as argument a sequence and returns a list 
of items without any elements with the same value next to each other and preserving the original order of elements.
"""

def unique_in_order(iterable):
    uniques = []
    if len(iterable)>0:
        uniques.append(iterable[0])
        
        for i in iterable:
            if i != uniques[-1]:
                uniques.append(i)

    return uniques

print(unique_in_order('AAAABBBCCDAABBB'))