from datetime import datetime

hour = datetime.now().hour

name = (input("Enter your name: "))

if hour < 12:
    print(f"Good Morning, {name}")
elif hour < 18:
    print(f"Good Afternoon, {name}")


else:
    print(f"Good Evening, {name}")        