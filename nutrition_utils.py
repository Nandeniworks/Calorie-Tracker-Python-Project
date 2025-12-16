def validate_calories(func):
    def wrapper(meal, portion, calories):
        if calories <= 0:
            print("Calories must be greater than zero.")
            return None
        return func(meal, portion, calories)
    return wrapper



calculate_calories = lambda calories: calories

#---List of High Calorie Foods---#
def high_calorie_foods(meal_list, limit=500):
    high_cal = [meal for meal in meal_list if meal["calories"] > limit]
    return high_cal