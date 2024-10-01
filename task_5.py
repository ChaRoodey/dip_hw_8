import csv


def count_csv(name_csv: str) -> None:
    with open(name_csv, 'r') as f:
        csv_data = csv.DictReader(f)
        total_sales = {}
        for row in csv_data:
            if row['product'] in total_sales:
                total_sales[row['product']] += int(row['quantity']) * float(row['price'])
            else:
                total_sales[row['product']] = int(row['quantity']) * float(row['price'])

    with open('zad_4/total_sales.csv', 'w') as f:
        fieldnames = ['название продукта', 'выручка']
        total_data = csv.DictWriter(f, fieldnames=fieldnames)
        total_data.writeheader()

        for product, tot_s in total_sales.items():
            total_data.writerow({'название продукта': product, 'выручка': tot_s})


if __name__ == '__main__':
    count_csv('zad_5/sales.csv')