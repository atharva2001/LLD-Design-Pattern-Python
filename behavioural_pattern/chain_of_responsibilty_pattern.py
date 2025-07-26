class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler  # for chaining

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None


class LowLevelSupport(Handler):
    def handle(self, request):
        if request == "low":
            return "LowLevelSupport handled the request"
        return super().handle(request)


class MidLevelSupport(Handler):
    def handle(self, request):
        if request == "medium":
            return "MidLevelSupport handled the request"
        return super().handle(request)


class HighLevelSupport(Handler):
    def handle(self, request):
        if request == "high":
            return "HighLevelSupport handled the request"
        return super().handle(request)


# Building the chain
low = LowLevelSupport()
mid = MidLevelSupport()
high = HighLevelSupport()

low.set_next(mid).set_next(high)

# Test it
print(low.handle("medium"))  # Output: MidLevelSupport handled the request
print(low.handle("high"))    # Output: HighLevelSupport handled the request
print(low.handle("unknown")) # Output: None
