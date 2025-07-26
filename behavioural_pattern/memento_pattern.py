# Memento
class EditorMemento:
    def __init__(self, content):
        self._content = content

    def get_saved_content(self):
        return self._content

# Originator
class Editor:
    def __init__(self):
        self._content = ""

    def type(self, words):
        self._content += words

    def save(self):
        return EditorMemento(self._content)

    def restore(self, memento):
        self._content = memento.get_saved_content()

# Caretaker
class History:
    def __init__(self):
        self._history = []

    def push(self, memento):
        self._history.append(memento)

    def pop(self):
        return self._history.pop()

# Usage
editor = Editor()
history = History()

editor.type("Hello ")
history.push(editor.save())

editor.type("World!")
history.push(editor.save())

editor.type(" More text...")

print("Current Content:", editor._content)

editor.restore(history.pop())  # Undo
print("After Undo:", editor._content)

editor.restore(history.pop())  # Undo again
print("After Second Undo:", editor._content)
