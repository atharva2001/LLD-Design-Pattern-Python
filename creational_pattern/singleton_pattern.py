class AppState:
    _instance = None 
    
    def __init__(self):
        if AppState._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AppState._instance = self
            self.isLoggedIn = False 

    @staticmethod
    def getAppState():
        if AppState._instance is None:
            AppState._instance = AppState()
        return AppState._instance
    
obj0 = AppState()
print(obj0.isLoggedIn)
obj1 = AppState.getAppState()
obj2 = AppState.getAppState()
obj1.isLoggedIn = True 
print(obj1.isLoggedIn) # True
print(obj2.isLoggedIn) # True
print(obj0.isLoggedIn)

obj3 = AppState()
print(obj3.isLoggedIn) 