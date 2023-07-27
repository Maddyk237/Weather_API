import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Failed to fetch weather data.")
        return []


def get_temp_by_date(weather_data, date):
    for entry in weather_data:
        if entry["dt_txt"].startswith(date):
            return entry["main"]["temp"]
    return None


def get_wind_speed_by_date(weather_data, date):
    for entry in weather_data:
        if entry["dt_txt"].startswith(date):
            return entry["wind"]["speed"]
    return None


def get_pressure_by_date(weather_data, date):
    for entry in weather_data:
        if entry["dt_txt"].startswith(date):
            return entry["main"]["pressure"]
    return None


def main():
    weather_data = get_weather_data()

    while True:
        print("Options:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            date = input("Enter the date (yyyy-mm-dd): ")
            temp = get_temp_by_date(weather_data, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp}°C")
            else:
                print("Data not available for the input date.")

        elif option == "2":
            date = input("Enter the date (yyyy-mm-dd): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not available for the input date.")

        elif option == "3":
            date = input("Enter the date (yyyy-mm-dd): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available for the input date.")

        elif option == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
