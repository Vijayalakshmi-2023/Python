# Generator 1: raw data source
def raw_data():
    for i in range(1, 21):
        yield i

# Generator 2: filters only even numbers
def filter_data(data_stream):
    for item in data_stream:
        if item % 2 == 0:
            yield item

# Generator 3: transforms (squares) the data
def transform_data(filtered_stream):
    for item in filtered_stream:
        yield item ** 2
# Pipeline chain
raw = raw_data()
filtered = filter_data(raw)
transformed = transform_data(filtered)

for result in transformed:
    print(result)
