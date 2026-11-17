class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        resultado = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # a até

            for c in s:
                count[ord(c) - ord("a")] += 1 # pega o cod da tabela ascii e subtrai pelo valor de a

            resultado[tuple(count)].append(s)

        return list(resultado.values())


    