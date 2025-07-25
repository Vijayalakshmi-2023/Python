class WeatherLogReader:
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.file.readline()
            if not line:
                self.file.close()
                raise StopIteration
            try:
                temp = float(line.strip())
                if temp > 30:
                    return temp
            except ValueError:
                continue  # Skip invalid lines
reader = WeatherLogReader('weather_log.txt')

print("🌡️ Temperatures above 30°C:")
for temp in reader:
    print(temp)
