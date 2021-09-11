def verify(name):
    if len(name) <= 10 and name.count(' ') < 5:
        return True
    else:
        return False
# may add the filter
