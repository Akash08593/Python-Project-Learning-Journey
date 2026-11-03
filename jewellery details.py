price=[7000,5000,6000]
address=("Kalyan jewellers","Chennai")
product={"name":"Gold Necklace","purity":"22k","price":7000}
categories={"gold","diamond","gold"}
def jewellery_details(price,discounts):
    final_price=price-(price*discounts/100)
    return final_price
result=jewellery_details(7000,10)
print("Product:",product["name"])
print("Price:",result)
print("Categories:",categories)