from abc import ABC, abstractmethod


class Memento(ABC):
    @abstractmethod
    def get_saved_state(self): pass


class ConcreteMemento(Memento, object):
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state


class Originator:
    _state = ""

    def set(self, state):
        self._state = state
        print("Originator: Setting state to", self._state)

    def save_to_memento(self):
        print("Originator: Saving to Memento.")
        return ConcreteMemento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()
        print("Originator: State after restoring from Memento:", self._state)


if __name__ == "__main__":
    saved_states = []
    originator = Originator()
    originator.set("State-1")
    originator.set("State-2")
    saved_states.append(originator.save_to_memento())

    originator.set("State-3")
    saved_states.append(originator.save_to_memento())

    originator.set("State-4")

    originator.restore_from_memento(saved_states[0])
