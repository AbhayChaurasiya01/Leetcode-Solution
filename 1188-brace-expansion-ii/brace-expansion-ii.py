class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        union = set()
        product_set = {''}
        
        for char in expression:
            if char.isalpha():
                product_set = {s + char for s in product_set}
            elif char == '{':
                stack.append(union)
                stack.append(product_set)
                union, product_set = set(), {''}
            elif char == '}':
                prev_product = stack.pop()
                prev_union = stack.pop()
                
                inner = union | product_set
                product_set = {p + i for p in prev_product for i in inner}
                union = prev_union
            elif char == ',':
                union |= product_set
                product_set = {''}
        
        return sorted(union | product_set)