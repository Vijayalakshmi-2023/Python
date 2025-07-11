READ = 1      
WRITE = 2     
EXECUTE = 4   

user_permissions = int(input("Enter user's permission value (1-7): "))

print("\n🔐 Access Rights:")
if user_permissions & READ:
    print("- Read permission: ✅")
else:
    print("- Read permission: ❌")

if user_permissions & WRITE:
    print("- Write permission: ✅")
else:
    print("- Write permission: ❌")

if user_permissions & EXECUTE:
    print("- Execute permission: ✅")
else:
    print("- Execute permission: ❌")
