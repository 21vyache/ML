#13 Пакет мобільного зв’язку передбачає 100 хвилин і 30 смс на місяць при фіксованій абонплаті у 30 гривень.
# Надалі дзвінки тарифікуються по 30 копійок за хвилину, а смс по 25 копійок за одиницю.
# Дано кількість хвилин й смс по номеру за місяць. Розрахувати загальну вартість послуг.

def total_cost_services(minutes, sms):
    """Calculation of the total cost of mobile services"""

    #As part of the mobile plan
    minutes_per_month  = 100
    sms_per_month = 30
    tariff = 30
    #Payment in excess of plan
    overpay_min = 0.3
    overpay_sms = 0.25

    cost_ext_min = 0
    if minutes > minutes_per_month:
        cost_ext_min = (minutes - minutes_per_month) * overpay_min

    cost_ext_sms = 0
    if sms > sms_per_month:
        cost_ext_sms = (sms - sms_per_month) * overpay_sms

    return tariff + cost_ext_min + cost_ext_sms


try:
    minutes = int(input("Enter the number of minutes used per month: "))
    sms = int(input("Enter the number of used sms per month: "))
    if minutes >= 0 and sms >= 0:
        total_pay = total_cost_services(minutes, sms)
        print(f"Total cost of mobile services per month {total_pay}")
    else:
        print("Incorrect data")

except ValueError as err:
    print(err)


#test
assert (total_cost_services(100, 30) == 30)
assert (total_cost_services(200, 60) == 67.5)