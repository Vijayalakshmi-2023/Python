start = int(input("Enter a number to start counting down from: "))

while start >= 1:
    print(start)
    start -= 1
    if start == 0:
        break  # Stop the loop when number becomes zero

print("⏹️ Countdown complete!")
