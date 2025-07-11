import math

# Circle area function
def area_circle(*args):
    if len(args) != 1 or args[0] <= 0:
        return "❌ Invalid radius for circle."
    radius = args[0]
    area = (lambda r: math.pi * r * r)(radius)
    return round(area, 2)

# Rectangle area function
def area_rectangle(*args):
    if len(args) != 2 or args[0] <= 0 or args[1] <= 0:
        return "❌ Invalid dimensions for rectangle."
    area = (lambda l, w: l * w)(*args)
    return area

# Square area function
def area_square(*args):
    if len(args) != 1 or args[0] <= 0:
        return "❌ Invalid side for square."
    area = (lambda s: s * s)(args[0])
    return area

# --- Example Usage ---
print("📐 Shape Area Calculator")
shape = input("Enter shape (circle/rectangle/square): ").strip().lower()

if shape == "circle":
    r = float(input("Enter radius: "))
    print("Area:", area_circle(r))

elif shape == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", area_rectangle(l, w))

elif shape == "square":
    s = float(input("Enter side: "))
    print("Area:", area_square(s))

else:
    print("❌ Unsupported shape.")
