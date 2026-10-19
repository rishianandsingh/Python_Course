import weather_desk


city = input()
base_price = float(input())
orders_last_hr = int(input())
riders_online = int(input())

temp, rain = weather_desk.weather_now(city)
pressure = orders_last_hr/riders_online

print(f"Temperature: {temp} C")
print(f"Rain: {rain:.1f} mm")
print(f"Orders per rider: {pressure:.1f}")


if temp == -1 or rain == -1:
    print("could not reach sky.... either service is down or city name is not supported")
elif rain > 0 and pressure > 3:
    surge = 1.5
    print("Surge: ", surge)
    print("Reason: raining AND every rider is buried in orders")
elif rain > 0:
    surge: 1.3
    print("Surge: ", surge)
    print("Reason: raining AND every rider is buried in orders")
elif temp >= 33 and pressure > 3:
    surge = 1.4
    print("Surge: ", surge)
    print("Reason: heat wave AND riders are stretched thin")
elif temp>=33:
    surge = 1.2
    print("Surge: ", surge)
    print("Reason: heat wave - nobody wants to step outside")
elif pressure>4:
    surge = 1.25
    print("Surge: ", surge)
    print("Reason: dry and pleasant, but demand is running ahead of riders")
else:
    surge = 1.0
    print("Surge: ", surge)
    print("Reason: calm hour - charge the normal price")

price = base_price*surge
print("Price: ", price)

