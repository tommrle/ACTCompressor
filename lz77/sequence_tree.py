class sequence_tree(object):
  def __init__(self):
    self.children = {}
    self.data = None
    self.index = None
    self.depth = 0

  def search(self, phrase, index):
    if phrase == "":
      return False

    if self.data is not None:
      relevantPhrase = phrase[0:1]
    else:
      relevantPhrase = phrase[:3]

    if self.data is None:
      if relevantPhrase in self.children.keys():
        return self.children[relevantPhrase].index
      else:
        self.children[relevantPhrase] = sequence_tree()
        self.children[relevantPhrase].index = index
        return False

    if relevantPhrase == self.data:
      if len(phase) > len(self.data):
        if phrase[len(self.data):len(self.data)+1] in self.children.getKeys():
          return self.children[phrase[len(self.data):len(self.data)+1]].search(phrase[len(self.data):], index)
        else:
          self.children[phrase[len(self.data):len(self.data)+1]].data = phrase[len(self.data):len(self.data)+1]
          self.children[phrase[len(self.data):len(self.data)+1]].data.index = index
          self.children[phrase[len(self.data):len(self.data)+1]].search(phrase[len(self.data)+1:], index)
      return self.index
    else:
      return False


  