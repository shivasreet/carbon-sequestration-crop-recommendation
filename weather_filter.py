def filter_by_weather(crops, weather):

    if weather is None:
        return crops

    temperature = weather["temperature"]

    filtered = crops[
        (crops["Temp_Min_C"] <= temperature) &
        (crops["Temp_Max_C"] >= temperature)
    ]

    # If no crops match, return the original list
    if filtered.empty:
        return crops

    return filtered