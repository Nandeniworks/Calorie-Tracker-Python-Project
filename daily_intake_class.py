import csv
from datetime import date

class DailyIntake:
    def __init__(self):
        self.date = date.today().isoformat()
        self.total_calories = 0
        self.meals = []

    def log_meal(self, meal, portion, calories):
        meal_data = {
            "date": self.date,
            "meal": meal,
            "portion": portion,
            "calories": calories
        }
        self.meals.append(meal_data)
        self.total_calories += calories

    def daily_total(self):
        return self.total_calories

    def goal_progress(self, goal):
        if self.total_calories <= goal:
            return "You are within your calorie goal!"
        else:
            return "You have exceeded your calorie goal!"

    def save_nutrition_log(self):
        file_name = "nutrition_log.csv"

        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)

     
            if file.tell() == 0:
                writer.writerow(["date", "meal", "portion", "calories"])

            for meal in self.meals:
                writer.writerow([
                    meal["date"],
                    meal["meal"],
                    meal["portion"],
                    meal["calories"]
                ])
                