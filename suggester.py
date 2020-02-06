#!/usr/local/bin/python3
import getopt
import sys
import re
from functools import reduce
import operator


# You will need to perform L lookups on the average for each
# of the W words in the set.The complexity of creating structure is O(W*L),
# where W is the number of words, and L is an average length of the word:
# Same with searching: you perform L steps for each of the W words.

def get_by_path(root, items):
    return reduce(operator.getitem, items, root)


def del_by_path(root, items):
    return reduce(operator.delitem, items, root)


class AutoSuggester:
    def __init__(self):
        self.tree = {}
        self.end = "%"

    def add_word(self, word):
        node = self.tree
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = self.end

    def remove_word(self, word):
        chars = list(word)
        node = self.tree
        for i in range(0, len(chars)):
            path = chars[:-i]
            if len(get_by_path(node, path)) == 2:
                del_by_path(node, path)

    def suggest_words(self, prefix):
        node = self.tree
        for c in prefix:
            if c not in node:
                return []
            node = node[c]
        ans = []
        self._suggest_words_internal(node, prefix, ans)
        return ans

    def _suggest_words_internal(self, node, prefix, ans):
        for k in node:
            if k == self.end:
                ans.append(prefix)
                continue
            self._suggest_words_internal(node[k], prefix + k, ans)


def usage():
    usage = """
  Mandatory arguments:
  -f, --filename
  -p, --pattern
  """
    print(usage)


def main():
    filename = None
    pattern = None
    # Parse commandline arguments
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "f:p:h",
            ["filename=", "pattern=", "help"]
        )
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-f", "--filename"):
            filename = a
        elif o in ("-p", "--pattern"):
            pattern = a
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"
            sys.exit(1)

    if filename is None or pattern is None:
        usage()
        sys.exit(1)

    # Try to open file
    try:
        body = open(filename, "r")
    except FileNotFoundError:
        print("No such file or directory")
        exit(1)

    # Read file as a list
    dictionary = body.read().split()
    # Close filestream
    body.close()
    # Convert words to downcase
    dictionary = map(lambda x: x.lower(), dictionary)
    # Remove non a-z characters
    regex = re.compile('[^a-zA-Z]')
    dictionary = map(lambda x: regex.sub('', x), dictionary)

    # Create an instance of AutoSuggester
    suggester = AutoSuggester()

    # Add words from dictionary
    for i in dictionary:
        suggester.add_word(i)

    print(suggester.suggest_words(pattern))


if __name__ == "__main__":
    main()
