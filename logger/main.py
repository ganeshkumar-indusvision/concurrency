import logging

class Service:
    def __init__(self):
        self.logger = logging.getLogger("") 
        if not self.logger.handlers:
            self.logger.addHandler(logging.FileHandler("shared.log"))

    def __del__(self):
        for h in self.logger.handlers[:]:
            self.logger.removeHandler(h)
            h.close()

s1 = Service()    # creates "shared" handler
s2 = Service()    # reuses the same handler

del s1             # ← removes the handler from the SHARED logger
# s2 tries to log... nothing happens. The handler is gone.

s2.logger.warning("from a1")