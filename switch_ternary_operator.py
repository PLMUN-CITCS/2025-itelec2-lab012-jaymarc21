day_messages = {
    "monday": "Today is Monday.",
    "tuesday": "Today is Tuesday.",
    "wednesday": "Today is Wednesday.",
    "thursday": "Today is Thursday.",
    "friday": "Today is Friday.",
    "saturday": "Today is Saturday.",
    "sunday": "Today is Sunday."
}day = input("Tuesday : ").strip().lower()
message = day_messages.get(day, "day_type.")
day_type = "Weekend" if day in ("saturday", "sunday") else "Weekday"
print(message)
print("It's a", day_type  + "!:")