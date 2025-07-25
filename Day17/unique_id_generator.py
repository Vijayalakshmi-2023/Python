def unique_id_generator(prefix="TRX", start=1, stop_after=1000):
    counter = start
    while True:
        if counter > stop_after:
            return f"{prefix}{counter - 1:03d}"  # for demo, return last ID
        new_start = yield f"{prefix}{counter:03d}"
        if new_start is not None:
            counter = new_start
        else:
            counter += 1
gen = unique_id_generator()

try:
    for _ in range(5):
        print(next(gen))  # Get next ID

    print("🔁 Resetting to TRX500")
    print(gen.send(500))  # Reset to TRX500

    for _ in range(3):
        print(next(gen))

except StopIteration as e:
    print("✅ Generator stopped after 1000 IDs. Last ID was:", e.value)
