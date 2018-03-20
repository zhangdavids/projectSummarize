def calculator(salary):
    """
    税后工资计算器 
    :param salary: 
    :return: 
    """

    point = 3500
    aged_rate = 0.08
    hospital_rate = 0.02
    unemployment_rate = 0.01
    fund_rate = 0.10
    five_one_money = salary * (aged_rate + hospital_rate + unemployment_rate + fund_rate)
    company_extra = salary * (0.20 + 0.10 + 0.015 + 0.012 + 0.008 + 0.10)
    rest_money = salary - five_one_money - point
    res_money = salary - five_one_money
    company_total = salary + company_extra
    if rest_money <= 1500:
        res_money -= rest_money * 0.03
    elif 1500 < rest_money <= 4500:
        tax_money = rest_money * 0.1
        res_money -= (tax_money - 105)
    elif 4500 < rest_money <= 9000:
        tax_money = rest_money * 0.2
        res_money -= (tax_money - 555)
    elif 9000 < rest_money <= 35000:
        tax_money = rest_money * 0.25
        res_money -= (tax_money - 1005)
    elif 35000 < rest_money <= 55000:
        tax_money = rest_money * 0.3
        res_money -= (tax_money - 2755)
    elif 55000 < rest_money <= 80000:
        tax_money = rest_money * 0.35
        res_money -= (tax_money - 5505)
    else:
        tax_money = rest_money * 0.45
        res_money -= (tax_money - 13505)
    print("税前工资为：{0}, 税后工资为：{1}, "
          "公司实际支付：{2}".format(salary, res_money, company_total))


if __name__ == '__main__':
    salary_list = [10000, 14000, 15000, 16000,
                   18000, 25000, 80000, 100000]
    for one_salary in salary_list:
        calculator(one_salary)
