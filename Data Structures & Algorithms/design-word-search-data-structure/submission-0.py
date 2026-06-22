class WordDictionary:

    def __init__(self):
        self.wordDic = []

    def addWord(self, word: str) -> None:
        self.wordDic.append(word)
        

    def search(self, word: str) -> bool:
        for wd in self.wordDic:
            if len(wd) != len(word):
                continue

            match = True

            for j in range(len(word)):
                if word[j] == '.':
                    continue
                if word[j] != wd[j]:
                    match = False
                    break
            
            if match:
                return True
        
        return False
