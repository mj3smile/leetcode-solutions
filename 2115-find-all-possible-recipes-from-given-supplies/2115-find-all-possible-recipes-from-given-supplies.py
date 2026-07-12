class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        recipes_index = dict()
        for i in range(len(recipes)):
            recipes_index[recipes[i]] = i

        result = []
        cache = dict()
        def doRecipe(index, need_from):
            if index in cache:
                return cache[index]

            for ing in ingredients[index]:
                if ing in supplies:
                    continue
                
                if ing in recipes_index:
                    if ing in need_from:
                        return False

                    need_from.add(recipes[index])    
                    print("need:", ing)
                    r = doRecipe(recipes_index[ing], need_from)
                    need_from.remove(recipes[index])
                    if not r:
                        cache[index] = False
                        return False
                    print("need done:", ing)
                    continue
                
                cache[index] = False
                return False
            
            cache[index] = True
            return True
        
        for i in range(len(recipes)):
            print("============", recipes[i])
            if doRecipe(i, set()):
                result.append(recipes[i])
            print("done", recipes[i])
        
        return result