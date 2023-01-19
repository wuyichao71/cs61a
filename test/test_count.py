def count():
    def counted():
        counted.call_count += 1
    counted.call_count = 0
    return counted


a = count()
print(a.call_count)
a()
print(a.call_count)
