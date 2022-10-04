import random
import csv

"ценная бумага"

sec_code = 'RU000A1013N6'

"вводим среднюю цену"

avg_price = 100

"вводим начальный сред"

start_spread_buy = 1
start_spread_sell = 1

max_spread = 5

max_qty = 500

"ищем цены на ПРОДАЖУ от и до"

from_sell_price = (avg_price + (avg_price * start_spread_sell / 100))
to_sell_price = avg_price + (avg_price * max_spread / 200)

"ищем цены на ПОКУПКУ от и до"

from_buy_price = (avg_price - (avg_price * start_spread_buy / 100))
to_buy_price = avg_price - (avg_price * max_spread / 200)

"узнаем спред между покупкой и продажей"
spread = round((to_sell_price - to_buy_price) / to_sell_price * 100, 2)


'Находим рандомные объемы заявок на продажу и на покупку'

def get_random_order_vol():
    orders_vol = []
    max_value = 1
    while max_value < max_qty:
        i = random.randint(1, 80)
        max_value = max_value + i
        orders_vol.append(i)

    return orders_vol


sell_orders_vol = get_random_order_vol()
buy_orders_vol = get_random_order_vol()


'Находим рандомные цены заявок на продажу и на покупку'

def get_random_order_price(is_sell):
    if is_sell:
        sell_orders_price = []
        for i in range(len(sell_orders_vol)):
            i = round(random.uniform(from_sell_price, to_sell_price), 2)
            sell_orders_price.append(i)

        return sell_orders_price
    else:
        buy_orders_price = []
        for i in range(len(sell_orders_vol)):
            i = round(random.uniform(from_buy_price, to_buy_price), 2)
            buy_orders_price.append(i)

        return buy_orders_price


sell_orders_price = get_random_order_price(True)
buy_orders_price = get_random_order_price(False)



print('Заявки на продажу')
print('От ', from_sell_price)
print('До ', to_sell_price)

"функция считающая кол-во элементов в объекте"
def get_sum(obj):
    qty = 0
    for i in range(len(obj)):
        qty += 1

    return qty

sum_on_sell = get_sum(sell_orders_vol)

print('Кол-во заявок на продажу', sum_on_sell)
print('Объем на продажу', sum(sell_orders_vol))

print('Заявки на покупку')
print('От ', from_buy_price)
print('До ', to_buy_price)

sum_on_buy = get_sum(buy_orders_vol)

print('Кол-во заявок на покупку', sum_on_buy)
print('Объем на покупку', sum(buy_orders_vol))

print('Спред =', spread)

"печать в файл"

with open("mm_orders2.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
    file_writer.writerow(["SECCODE", "SECBOARD", "TRDACCFIRMID", 'ACCOUNT', "BUYSELL", "MKTLIMIT", "PRICE", "QUANTITY",
                          "HIDDEN", "ORDERVALUE", "CLIENTCODE", "BROKERREF", "ACTIVATIONTIME", "SPLITFLAG", "IMMCANCEL",
                          "PRICEYIELDENTERTYPE", "MMORDER", "ACTIVATIONTYPE", "LIQUIDITYTYPE"])
    for i in range(len(buy_orders_vol)):
        file_writer.writerow([sec_code, "TQCB", "GC0294900000", "S01+00000F00", "B", "L", buy_orders_price[i],
                              buy_orders_vol[i], "", "", "", "", "", "S"," ", "P", "M", " ", ""])
    for i in range(len(sell_orders_vol)):
        file_writer.writerow(
            [sec_code, "TQCB", "GC0294900000", "S01+00000F00", "S", "L", sell_orders_price[i], sell_orders_vol[i], "",
             "", "", "", "", "S", " ", "P", "M", " ", ""])