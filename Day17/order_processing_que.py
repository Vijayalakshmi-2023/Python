def order_processor(orders):
    total_processed = 0
    paused = False
    i = 0
    
    while i < len(orders):
        if paused:
            command = yield  # Wait for resume signal
            if command == "resume":
                paused = False
        else:
            command = yield orders[i]
            print(f"Processing order: {orders[i]}")
            total_processed += 1
            i += 1
            if command == "pause":
                paused = True
    
    return f"All {total_processed} orders processed."
order_queue = [
    "Order #1001",
    "Order #1002",
    "Order #1003",
    "Order #1004",
    "Order #1005"
]
processor = order_processor(order_queue)
next(processor)  # Prime the generator

try:
    while True:
        # Simulate some external control
        order = processor.send(None)
        print(">>", order)
        
        # Pause after 2nd order
        if order == "Order #1002":
            print("-- Pausing --")
            processor.send("pause")
        
        # Resume after pause
        if order == "Order #1002":
            print("-- Resuming --")
            processor.send("resume")
except StopIteration as e:
    print("\nProcessing Complete.")
    print("Summary:", e.value)
