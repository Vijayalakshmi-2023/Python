import json

def json_stream_processor(filepath, stop_key="status", stop_value="stop"):
    with open(filepath, 'r') as f:
        for line in f:
            if not line.strip():
                continue  # skip empty lines
            try:
                obj = json.loads(line)
                yield obj
                if obj.get(stop_key) == stop_value:
                    break
            except json.JSONDecodeError:
                continue  # skip malformed lines
# Create a sample JSON file
with open("data.json", "w") as file:
    file.write('{"id": 1, "status": "ok"}\n')
    file.write('{"id": 2, "status": "error"}\n')
    file.write('{"id": 3, "status": "ok"}\n')
    file.write('{"id": 4, "status": "stop"}\n')

# Use the generator
for entry in json_stream_processor("data.json"):
    print(entry)
