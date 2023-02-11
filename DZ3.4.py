products = []
for w in range(1, 4):
    print(f"Заполняем информацию по {w}-му товару")
    product_name = input("Название: ")
    product_price = int(input("Цена: "))
    product_count = int(input("Кол-во: "))
    product_measure = input("Единица измерения: ")
    products.append(
        (w, {'название': product_name, 'цена': product_price, 'кол-во': product_count, 'eд': product_measure}))

print(f"Исходный список товаров: \n{products}")

product_names = []
product_prices = []
product_counts = []
product_measures = []
for w in products:
    product_names.append(w[1].get('название'))
    product_prices.append(w[1].get('цена'))
    product_counts.append(w[1].get('кол-во'))
    product_measures.append(w[1].get('eд'))

report = {
    'название': list(set(product_names)),
    'цена': list(set(product_prices)),
    'кол-во': list(set(product_counts)),
    'eд': list(set(product_measures))
}

print(f"Общий отчет по списку товаров: \n{report}")
