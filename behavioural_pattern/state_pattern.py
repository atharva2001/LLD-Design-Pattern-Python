from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self):
        pass


class WalkingState(State):
    def handle(self):
        print("User is Walking!!!")

class RunningState(State):
    def handle(self):
        print("User is Running!!!")

class Human:
    def __init__(self):
        self._state = WalkingState()

    def set_state(self, state: State):
        self._state = state

    def show_state(self):
        self._state.handle()


human = Human()
human.show_state()
human.set_state(RunningState())
human.show_state()
human.set_state(WalkingState())
human.show_state()