from daily_intake_class import DailyIntake
from nutrition_utils import validate_calories
import matplotlib.pyplot as plt


tracker = DailyIntake()

print("Daily Calorie Intake Tracker")
print("-----------------------------")


count = int(input("How many meals do you want to log today? "))


@validate_calories
def add_meal(meal, portion, calories):
    tracker.log_meal(meal, portion, calories)


for i in range(count):
    print("\nEnter details for meal", i + 1)

    meal = input("Meal name (breakfast/lunch/dinner/snack): ")
    portion = input("Portion size (example: 1 bowl, 2 rotis): ")
    calories = int(input("Calories: "))

    add_meal(meal, portion, calories)


tracker.save_nutrition_log()


total = tracker.daily_total()
print("\nTotal calories consumed today:", total)


goal = int(input("Enter your daily calorie goal: "))
print(tracker.goal_progress(goal))

# -------- BAR CHART --------

meal_names = []
meal_calories = []

for meal in tracker.meals:
    meal_names.append(meal["meal"])
    meal_calories.append(meal["calories"])

plt.bar(meal_names, meal_calories)
plt.xlabel("Meal")
plt.ylabel("Calories")
plt.title("Calories by Meal")

plt.show()
