class Diary:
    def __init__(self, title):
        self.title = title
        self.entries = []

    def addentry(self, entry):
        self._entries.append(entry)

    def _lastentry(self):
        return self._entries[-1]

mydiary = Diary("Don't read this!!!!")
