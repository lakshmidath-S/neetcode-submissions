class Node:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()

            node = node.children[ch]

        node.end = True

    def search(self, word: str) -> bool:

        def search_from(node, index):

            if index == len(word):
                return node.end

            ch = word[index]

            # Normal character
            if ch != '.':
                if ch not in node.children:
                    return False

                return search_from(node.children[ch], index + 1)

            # '.': try every possible character
            for child in node.children.values():
                if search_from(child, index + 1):
                    return True

            return False

        return search_from(self.root, 0)