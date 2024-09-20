
class TrieNode:
    def __init__(self):
        self.children = {}                # maps char & their Node pointers
        self.word_end = False             # whether this node holds pointer to last char for a word

    def insert(self, word: str) -> None:
        current_node = self

        for char in word:
            if char not in current_node.children:
                new_node = TrieNode()
                current_node.children[char] = new_node
            current_node = new_node  # update pointer to add new char
        current_node.word_end = True  # mark end of the word in Trie

    def search(self, word: str) -> bool:
        current_node = self

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # return true if the word exists as a word & not just as prefix
        return current_node.word_end


if __name__ == "__main__":
    words = ["andy", "john"]
    trie = TrieNode()
    trie.insert(word="andy")
    trie.insert(word="john")
    print(trie.search("and"))      # False
    print(trie.search("alis"))     # False
    print(trie.search("andy"))     # True
