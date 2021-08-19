#6 Дано розмір кредиту й одноразові відсотки по ньому.
#Знайти загальну суму з відсотками й розмір переплати.

def total_sum(credit, percentages):
    """Calculation of the total amount with interest"""
    return credit + (credit * percentages / 100)

def overpayment(total, credit):
    """Calculation of overpayments"""
    return total - credit


try:
    credit = int(input("Credit amount: "))
    percentages = int(input("Percentages: "))

    total = total_sum(credit, percentages)
    print(f"Total sum with interest: {total}")

    over = overpayment(total, credit)
    print(f"Overpayment is {over}")

except ValueError as err:
    print(err)


#test
assert (total_sum(1000, 10) == 1100 and overpayment(1100, 1000) == 100)