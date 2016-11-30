spam = 42  # global


def tutu():
    global spam
    spam = 45  # local


tutu()
print(spam)
