class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        k = []
        for i in range(1,len(searchWord)+1):
            t = searchWord[:i]
            l = []
            for j in products:
                if j[:i] == t:
                    l.append(j)
            k.append(l[:3])
        return k
            
