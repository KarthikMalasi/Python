#calorie tracker

print("****Daily Calorie Tracker****\n")


meals=[]
calories=[]

x= int(input("how many meals did you eat today?  "))

for i in range(x):
    meal = input(f"Enter name of meal {i+1}: ")
    cal_str= input(f"Enter calories for {meal}: ")  
    print()
    calorie = float(cal_str)  
    meals.append(meal)
    calories.append(calorie)


total_cal = 0
for c in calories:
    total_cal += c

average_cal = total_cal/x
cal_left = 2000-total_cal

print("\n***** Daily Calorie Report *****")
for i in range(len(meals)):
    print(f"{meals[i]}: {calories[i]} kcal")

print()
print(f"Total Calories: {total_cal:.2f} kcal")
print(f"Average Calories: {average_cal:.2f} kcal")

if total_cal > 2000:
    print("Warning Daily Calorie limit exceeded!")
else:
    print(f"Daily calories left is: {cal_left:.2f}")













