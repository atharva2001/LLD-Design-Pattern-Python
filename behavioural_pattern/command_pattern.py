class Worker:
    def cleaning(self):
        print("Cleaning Started")

    def cooking(self):
        print("Cooking Started")

    def practice(self):
        print("Practice Started")


class Command:
    def execute(self):
        pass 

class Cleaning(Command):
    def __init__(self, worker: Worker):
        self.worker = worker

    def execute(self):
        self.worker.cleaning()


class Cooking(Command):
    def __init__(self, worker: Worker):
        self.worker = worker

    def execute(self):
        self.worker.cooking()

class Pracitce(Command):
    def __init__(self, worker: Worker):
        self.worker = worker

    def execute(self):
        self.worker.practice()


class King:
    def order(self, command: Command):
        command.execute()


worker = Worker()
cleaner = Cleaning(worker)
cook = Cooking(worker)
practice = Pracitce(worker)

king = King()
king.order(cleaner)
king.order(cook)
king.order(practice)

