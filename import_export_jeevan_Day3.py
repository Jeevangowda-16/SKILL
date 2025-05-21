import csv, os

FILES = {
    'imported': 'imported.csv',
    'exported': 'exported.csv',
    'bill': 'bill.csv',
    'suggestions': 'dealer_suggestions.csv'
}

HEADERS = {
    'imported': ['ItemID', 'ItemName', 'Quantity', 'Price'],
    'exported': ['ItemID', 'ItemName', 'Quantity', 'Price'],
    'bill': ['BuyerName', 'ItemID', 'ItemName', 'Quantity', 'Price', 'Total'],
    'suggestions': ['DealerName', 'ItemName', 'Quantity', 'Price']
}

def create_csvs():
    for key in FILES:
        if not os.path.exists(FILES[key]):
            with open(FILES[key], 'w', newline='') as f:
                csv.writer(f).writerow(HEADERS[key])

def print_stock(file_key, title):
    if not os.path.exists(FILES[file_key]):
        print(f"\n--- {title} ---\nNo stock.")
        return
    with open(FILES[file_key], 'r') as f:
        rows = list(csv.DictReader(f))
        if not rows:
            print(f"\n--- {title} ---\nNo stock.")
            return
        print(f"\n--- {title} ---")
        print(f"{'ID':<6}{'Name':<15}{'Qty':<8}{'Price'}")
        for r in rows:
            print(f"{r['ItemID']:<6}{r['ItemName']:<15}{r['Quantity']:<8}₹{r['Price']}")

def add_imported():
    i = input("Item ID: "); n = input("Name: ")
    q = int(input("Qty: ")); p = float(input("Price: "))
    with open(FILES['imported'], 'a', newline='') as f:
        csv.writer(f).writerow([i, n, q, p])
    print("Item added to imported stock.")

def export_item():
    i = input("Enter Item ID to export: ")
    rows, found = [], False
    with open(FILES['imported'], 'r') as f:
        for r in csv.DictReader(f):
            if r['ItemID'] == i:
                with open(FILES['exported'], 'a', newline='') as e:
                    csv.writer(e).writerow([r[k] for k in HEADERS['exported']])
                print("Item exported.")
                found = True
            else:
                rows.append(r)
    with open(FILES['imported'], 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=HEADERS['imported'])
        w.writeheader(); w.writerows(rows)
    if not found: print("Item not found.")

def view_stock():
    print_stock('imported', "Imported Stock")
    print_stock('exported', "Exported Stock")

def view_suggestions():
    if not os.path.exists(FILES['suggestions']):
        print("\nNo suggestions.")
        return
    with open(FILES['suggestions'], 'r') as f:
        s = list(csv.DictReader(f))
    if not s:
        print("\nNo suggestions.")
        return
    print(f"\n{'ID':<5}{'Dealer':<15}{'Item':<20}{'Qty':<8}{'Price'}")
    for i, r in enumerate(s, 1):
        print(f"{i:<5}{r['DealerName']:<15}{r['ItemName']:<20}{r['Quantity']:<8}₹{r['Price']}")

def accept_suggestion():
    view_suggestions()
    if not os.path.exists(FILES['suggestions']):
        return
    with open(FILES['suggestions'], 'r') as f:
        sugg = list(csv.DictReader(f))
    if not sugg: return
    try:
        sel = int(input("Enter suggestion ID to accept: "))
        if 1 <= sel <= len(sugg):
            r = sugg[sel - 1]
            iid = input("Enter new Item ID: ")
            row = [iid, r['ItemName'], r['Quantity'], r['Price']]
            for key in ['imported', 'exported']:
                with open(FILES[key], 'a', newline='') as f:
                    csv.writer(f).writerow(row)
            print("Item added to imported/exported stock.")
        else: print("Invalid ID.")
    except: print("Invalid input.")

def send_suggestion():
    d = input("Dealer Name: ")
    n = input("Item Name: ")
    try:
        q = int(input("Quantity: "))
        p = float(input("Price: "))
        with open(FILES['suggestions'], 'a', newline='') as f:
            csv.writer(f).writerow([d, n, q, p])
        print("Suggestion sent.")
    except:
        print("Invalid quantity or price.")

def buy():
    name = input("Buyer Name: "); cart = []
    with open(FILES['exported'], 'r') as f:
        stock = {r['ItemID']: r for r in csv.DictReader(f)}
    if not stock:
        print("No items to buy."); return
    print(f"\n{'ID':<6}{'Name':<15}{'Qty':<8}{'Price'}")
    for r in stock.values():
        print(f"{r['ItemID']:<6}{r['ItemName']:<15}{r['Quantity']:<8}₹{r['Price']}")
    while True:
        e = input("\nEnter 'ItemID Qty' or 'done': ").strip()
        if e.lower() == 'done': break
        try:
            iid, qty = e.split(); qty = int(qty)
            if iid not in stock: print("Invalid ID."); continue
            if qty > int(stock[iid]['Quantity']): print("Not enough stock."); continue
            p = float(stock[iid]['Price'])
            cart.append([name, iid, stock[iid]['ItemName'], qty, p, qty * p])
            stock[iid]['Quantity'] = str(int(stock[iid]['Quantity']) - qty)
            print(f"Added {qty} x {stock[iid]['ItemName']}")
        except: print("Invalid input.")
    if not cart: return
    with open(FILES['bill'], 'a', newline='') as f:
        csv.writer(f).writerows(cart)
    with open(FILES['exported'], 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=HEADERS['exported'])
        w.writeheader(); w.writerows(stock.values())
    total = sum([x[-1] for x in cart])
    print(f"\nBill for {name}:")
    for x in cart: print(f"{x[3]} x {x[2]} @ ₹{x[4]} = ₹{x[5]}")
    print(f"TOTAL: ₹{total}\n✓ Thank you!\n")

def main():
    create_csvs()
    while True:
        print("\nLogin as:\n1. Owner\n2. Dealer\n3. Buyer\n4. Exit")
        c = input("Choice: ")
        if c == '1':
            while True:
                print("\nOWNER MENU\n1. Add Item\n2. Export Item\n3. View Stock\n4. View Suggestions\n5. Accept Suggestion\n6. Back")
                o = input("Choice: ")
                if o == '1': add_imported()
                elif o == '2': export_item()
                elif o == '3': view_stock()
                elif o == '4': view_suggestions()
                elif o == '5': accept_suggestion()
                elif o == '6': break
                else: print("Invalid.")
        elif c == '2':
            while True:
                print("\nDEALER MENU\n1. View Stock\n2. Suggest Item\n3. Back")
                d = input("Choice: ")
                if d == '1': view_stock()
                elif d == '2': send_suggestion()
                elif d == '3': break
                else: print("Invalid.")
        elif c == '3': buy()
        elif c == '4': print("Goodbye!"); break
        else: print("Invalid input.")

if __name__ == '__main__':
    main()
