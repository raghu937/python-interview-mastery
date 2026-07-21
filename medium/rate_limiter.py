import time
class RateLimiter:
    def __init__(self,max_calls,period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []

    def allow(self):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < self.period]
        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True
        return False
        

rl = RateLimiter(3,2)
rl.allow()
rl.allow()

print(rl.allow())



# import time

# class RateLimiter:
#     def __init__(self, max_calls, period):
#         self.max_calls = max_calls
#         self.period = period
#         self.calls = []

#     def allow(self):
#         now = time.time()
#         self.calls = [t for t in self.calls if now - t < self.period]
#         print(self.calls)
#         # if len(self.calls) < self.max_calls:
#         #     self.calls.append(now)
#         #     return True
#         # return False

# rl = RateLimiter(2, 1)
# print(rl.allow())  # True
# print(rl.allow())  # True
# print(rl.allow())  # False