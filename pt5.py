import random

random.seed(2026)
N=random.randint(15,25)

Category=["Drink","Food","General","Cloth"]
Shop=["S01","S02","S03","S04","S05"]
Inventory=[]
#6
for i in range(1,N+1):
    item={
        "CODE":f"P{i:03d}",
        "CATEGORY":random.choice(Category),
        "SHOP":"S%02d" % random.randint(1,5),
        "PRICE":random.randint(10,300),
        "STOCK":random.randint(1,20),
        "SOLD":0,
        "GOVE_SPEND":0
    }
    Inventory.append(item)
print("-------PART1---------")
#7
print("#7 Expensive per CAT")
print(f"{'CODE':<10}{'CATEGORY':<10}{'SHOP':<10}{'PRICE':<10}{'STOCK':<10}")
for cat in Category:
    temp=[p for p in Inventory if p["CATEGORY"]==cat]
    if temp:
        Expensive=sorted(temp,key=lambda x:(-x["PRICE"],x["CODE"]))[0]
    print(f"{Expensive['CODE']:<10}{Expensive['CATEGORY']:<10}{Expensive['SHOP']:<10}{Expensive['PRICE']:<10}{Expensive['STOCK']:<10}")

#8
print("#7 Cheapest Products")
print(f"{'CODE':<10}{'CATEGORY':<10}{'SHOP':<10}{'PRICE':<10}{'STOCK':<10}")
Cheapest=sorted(Inventory,key=lambda x:(x["PRICE"],x["CODE"]))[0]
print(f"{Cheapest['CODE']:<10}{Cheapest['CATEGORY']:<10}{Cheapest['SHOP']:<10}{Cheapest['PRICE']:<10}{Cheapest['STOCK']:<10}")

#9
print("#9 Output Sort Products")
for cat in Category:
    print(f"{cat}")
    print(f"{'CODE':<10}{'CATEGORY':<10}{'SHOP':<10}{'PRICE':<10}{'STOCK':<10}")
    for p in Inventory:
        if(p["CATEGORY"]==cat):
            print(f"{p['CODE']:<10}{p['CATEGORY']:<10}{p['SHOP']:<10}{p['PRICE']:<10}{p['STOCK']:<10}")

#10
print("#10 Sumarry Shop output")
for s in Shop:
    count_item=0
    total_price=0
    total_stock=0
    print(f"Shop {s}")
    print(f"{'Total_Item'}{' '*10}{'Total_Stock'}{' '*10}{'Total_Price'}")
    for p in Inventory:
        if(p["SHOP"]==s):
            count_item+=1
            total_stock+=p['STOCK']
            total_price+=p['STOCK']*p['PRICE']
    print(f"{count_item}{' '*23}{total_stock}{' '*17}{total_price}")
#Part 1 Finish in 44 min

#Part2
print("-------PART2---------")
#11
A=3
CAP_DAY=200
CAP_SHOP=60
Customer_data=[]

for Customer in range(1,A+1):
    print(f"Customer :{Customer}")
    print(f"{'SHOP':<10}{'CODE':<10}{'CATEGORY':<10}{'PRICE':<10}{'GvPaid':<10}{'CustPay':<10}")
    cart=[]
    Customer_Cap=CAP_DAY
    SHOP_CAP=[]
    Gross=0
    GovUsed=0
    total_disc=0
    for i in range(1,6):
        item={
            f"S{i:02d}":CAP_SHOP
        }
        SHOP_CAP.append(item)
    K=random.randint(1,10)
    for _ in range(K):
        pid=random.randint(1,N)
        item=Inventory[pid-1]
        if item['STOCK']==0:
            new_item=[t for t in Inventory if t["SHOP"]==item["SHOP"] and t["CATEGORY"]==item["CATEGORY"]]
            
            if new_item:
                item=min(new_item,key=lambda x:(x['PRICE'],x['CODE']))
            else:
                continue
        GovBase=item["PRICE"]//2
        GovPaid=0
        if Customer_Cap<=0:
            GovPaid=0
        else:
            for s in SHOP_CAP:
                if(item["SHOP"] in s ):
                    if(s[item["SHOP"]]>GovBase):
                        GovPaid=GovBase
                        s[item["SHOP"]]-=GovBase
                    else:
                        if s[item["SHOP"]]>0:
                            GovPaid=s[item["SHOP"]]
                        s[item["SHOP"]]=0
            Customer_Cap-=GovBase
        cust_pay=item["PRICE"]-GovPaid
        item["STOCK"]-=1
        item["SOLD"]+=1
        item["GOVE_SPEND"]+=GovPaid
        Gross+=item["PRICE"]
        GovUsed+=GovPaid
        cart.append({"SHOP":item["SHOP"],"CODE":item["CODE"],"CATEGORY":item["CATEGORY"],"PRICE":item["PRICE"],"GOV":GovPaid,"CUST":cust_pay,"CUSTOMER":Customer})
        receipt_sorted=sorted(cart,key=lambda x:(x["SHOP"],x["CODE"]))
        for s in Shop:
            discount=0
            item_shop = [t for t in receipt_sorted if t["SHOP"]==s]
            if not item_shop:
                continue
            shop_cust_sum=sum(t["CUST"] for t in item_shop)
            if len(item_shop) >= 3:
                discount = int(shop_cust_sum * 0.05)
            else:
                discount = 0
            total_disc += discount
    cart=sorted(cart,key=lambda x:(x["SHOP"],x["CODE"]))
    for item in cart:
        print(f"{item["SHOP"]:<10}{item["CODE"]:<10}{item["CATEGORY"]:<10}{item["PRICE"]:<10}{item["GOV"]:<10}{item["CUST"]:<10}")
    Customer_data.append({"no":Customer,"GROSS":Gross,"GOV":GovUsed,"DISC":total_disc,"NET":Gross-GovUsed-total_disc})
    print(f"Gross:{Gross:<10}GovUsed:{GovUsed:<10}ShopDisc:{total_disc:<10}NET:{Gross-GovUsed-total_disc}")

print("----------------------PART 3-------------")
print("\nTop 3 BestSell:")
BestSoldT3=sorted(Inventory,key=lambda x:(-x["SOLD"],x["CODE"]))[:3]
print(f"{'CODE':<10}{'CATEGORY':<10}{'SHOP':<10}{'PRICE':<10}{'STOCK':<10}{'GOVE_SPEND':<10}")
for p in BestSoldT3:
    print(f"{p["CODE"]:<10}{p["CATEGORY"]:<10}{p["SHOP"]:<10}{p["PRICE"]:<10}{p["SOLD"]:<10}{p["GOVE_SPEND"]:<10}")

shop_analytics = []
for s_code in [f"S{i:02d}" for i in range(1, 6)]:
    gov_total = sum(it['GOVE_SPEND'] for it in Inventory if it['SHOP'] == s_code)
    shop_analytics.append({"SHOP": s_code, "gov": gov_total})
top2_shops = sorted(shop_analytics, key=lambda x: (-x['gov'], x['SHOP']))[:2]
print("\nTop 2 Shops (Gov Total):")
for s in top2_shops:
    print(f" - {s['SHOP']} GovTotal: {s['gov']}")

if Customer_data:
    best_saver = max(Customer_data, key=lambda x: (x['GOV']/x['GROSS'] if x['GROSS'] > 0 else 0, -x['no']))
    rate = (best_saver['GOV']/best_saver['GROSS']) if best_saver['GROSS'] > 0 else 0
    print(f"\nBest Saver: Customer {best_saver['no']} (Rate: {rate:.2%})")
#Low Stock: สินคาที่เหลือ STOCK <= 2 เรียงตาม STOCK, SHOP, CODE 
for p in sorted(Inventory, key=lambda x: (x['STOCK'], x['SHOP'], x['CODE'])):
    if p['STOCK'] <= 2:
        print(f"Low Stock: {p['CODE']} STOCK: {p['STOCK']} SHOP: {p['SHOP']}")

#Integrity Check:
sum_gross = sum(c['GROSS'] for c in Customer_data)
sum_gov = sum(c['GOV'] for c in Customer_data)
sum_disc = sum(c['DISC'] for c in Customer_data)
sum_net = sum(c['NET'] for c in Customer_data)
print(f"\nIntegrity Check: Net({sum_net}) == {sum_gross} - {sum_gov} - {sum_disc}")