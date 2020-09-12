
class TrieNode:    
    def __init__(self, letter):
        self.children = {}
        self.isWord = False
        self.parentNode = None
        self.letter = letter
        self.prefix = self.letter
        
    def isLeaf(self):
        return False if (len(self.children) > 0) else True
    
    def setParent(self, node):
        self.parentNode = node
        
    def addChild(self, letter):
        newNode = TrieNode(letter)
        newNode.setParent(self)
        self.children[letter] = newNode
        
    def getChild(self, letter):
        return self.children[letter]
    
    def findWord(self, word):
        keepSearching, found = True, False
        currNode = self
        for letter in word:
            if (keepSearching):
                if (letter in currNode.children.keys()):
                    currNode = currNode.children[letter]
                else:
                    keepSearching = False
        if (keepSearching and currNode.isWord):
            found = True
        nodeFound = currNode if found else None
        results = {
            "found": found,
            "nodeFound": nodeFound
            }
        return results
    
    def addWord(self, word):
        currNode = self
        prefix = ""
        for letter in word:
            if not (letter in currNode.children.keys()):
                currNode.addChild(letter)
            prefix += letter
            currNode = currNode.getChild(letter)
        currNode.prefix = prefix
        currNode.isWord = True
        
    def removeWord(self, word):
        currNode = self
        for letter in word:
            if (letter in currNode.children.keys()):
                if ( currNode.children[letter].isLeaf() ):
                    del currNode.children[letter]
                else:
                    currNode = currNode.children[letter]
                    
    def info(self):
        if (self.isWord):
            print(self.prefix)
            if (self.isLeaf()): 
                return
        childNodes = self.children
        for child in childNodes.keys():
            childNode = childNodes[child]
            if (childNode != None):
                childNode.info()


trie = TrieNode('')
wordList = [
    "pack", "pad", "panic", "pant", "pants", "panel",
    "apple", "able", "ancient", "allergy", "all", "application",
    "take", "task", "tar", "tangle", "ton", "tongue", "the", "there"
    ]

for word in wordList:
    trie.addWord(word)
trie.removeWord("pack")
trie.info()
