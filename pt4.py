import random

category =["Drink","Food","General","Cloth"]
shop=["S01","S02","S03","S04","S05",]
product=[]

random.seed(166)
N=random.randint(15,25)

for i in range (1,N+1):
    item={
        "ID":i,
        "CODE":f"P{i:03d}",
        "CATEGORY":random.choice(category),
        "SHOP":random.choice(shop),
        "PRICE":random.randint(10,300),
        "STOCK":random.randint(1,20)
    }
    product.append(item)

#OUTPUT PART1 
#1 High Price per Category
print("="*60)
print("Most Expensive item Per Category")
print("="*60)
print(f"{'ID':<10}{'CODE':<10}{'CATEGORY':<10}{'SHOP':<10}{'PRICE':<10}{'STOCK':<10}")
for cat in category:
    temp=[]
    for p in product:
        if cat==p["CATEGORY"]:
            temp.append(p)
    Expensive=max(temp,key=lambda x:x["PRICE"])
    for p in temp:
        if(p["PRICE"]==Expensive["PRICE"]):
            print(f"{p['ID']:<10}{p['CODE']:<10}{p['CATEGORY']:<10}{p['SHOP']:<10}{p['PRICE']:<10}{p['STOCK']:<10}")
print("="*60)
#2 Cheapest item all product
print("Most Cheapest item")
print("="*60)
print(f"{'ID':<10}{'CODE':<10}{'CATEGORY':<10}{'SHOP':<10}{'PRICE':<10}{'STOCK':<10}")
cheap=min(product,key=lambda x:x["PRICE"])
for p in product:
    if p["ID"]==cheap["ID"]:
        print(f"{p['ID']:<10}{p['CODE']:<10}{p['CATEGORY']:<10}{p['SHOP']:<10}{p['PRICE']:<10}{p['STOCK']:<10}")
print("="*60)
#3 Count item per CATEGORY
print("QTY item Per Category")
print("="*60)
print(f"{'ID':<10}{'CODE':<10}{'CATEGORY':<10}{'SHOP':<10}{'PRICE':<10}{'STOCK':<10}")
for cat in category:
    temp=[]
    for p in product:
        if p["CATEGORY"]==cat:
            temp.append(p)
    for p in temp:
        print(f"{p['ID']:<10}{p['CODE']:<10}{p['CATEGORY']:<10}{p['SHOP']:<10}{p['PRICE']:<10}{p['STOCK']:<10}")
    print("-"*60)
    print(f"QTY : {len(temp)} items")
    print("-"*60)
print("="*60)           #อยากสวยเหมือนคนอื่นบ้างครับ
#4 Summarize Shop
print("Summarize Shop")
print("="*60)  

for s in shop:
    
    print(f"SHOP : {s}")
    print(f"{'Total_Item'}{' '*10}{'Total_Stock'}{' '*10}{'Total_Price'}")
    count_item=0
    total_price=0
    total_stock=0
    for p in product:
        if s==p["SHOP"]:
            count_item+=1
            total_stock+=p['STOCK']
            total_price+=p['STOCK']*p['PRICE']
    print(f"{count_item}{' '*23}{total_stock}{' '*17}{total_price}")
    print("-"*60)  

#PART 2 OUTPUT
N=25 #จำนวนชิ้นสูงสุด
K=10 #จำนวนรายการ
M=3 #จำนวนลูกค้า
CAP_DAY=200
CAP_SHOP=2000
#2.1 STOCK+Replacement

for customer in range (M):
    CAP_LEFT_DAY=CAP_DAY
    CAP_LEFT_SHOP={s: CAP_SHOP for s in shop}
    num_item_buy=random.randint(1,K)
    bill_items=[]
    for _ in range (num_item_buy):
        target_p=random.choice(product)
        if(target_p["STOCK"]<=0):
            replacement_p = [p for p in product if p["CATEGORY"]==target_p["CATEGORY"] and p["SHOP"]==target_p["SHOP"] and p["STOCK"]>0]
            if not replacement_p:
                continue
            target_p=sorted(replacement_p,key=lambda x:(x["PRICE"],x["CODE"]))[0]
        target_p["STOCK"]-=1
        if target_p:
            #2.2 & 2.3
            gov_pay=target_p["PRICE"]//2
            if target_p['CATEGORY']=="Cloth":
                gov_pay=min(gov_pay,30)
            if target_p['CATEGORY']=="General" and target_p['PRICE']>200:
                gov_pay=0
            actual_gov_pay=min(gov_pay,CAP_LEFT_DAY,CAP_LEFT_SHOP[target_p['SHOP']])
            cust_pay=target_p["PRICE"]-actual_gov_pay
            bill_items.append({'SHOP':target_p['SHOP'],'CODE':target_p['CODE'],
                               'CATEGORY':target_p['CATEGORY'],'PRICE':target_p['PRICE'],
                               'Gov':actual_gov_pay,'Cust':cust_pay})
            CAP_LEFT_DAY-=actual_gov_pay
            CAP_LEFT_SHOP[target_p['SHOP']]-=actual_gov_pay
    


    print(f"Customer: {customer}")
    print(f"{'SHOP'}{' '*6}{'CODE'}{' '*6}{'CATE'}{' '*6}{'PRICE'}{' '*5}{'GovePaid'}{' '*2}{'CustPay'}")
    bill_items.sort(key=lambda x:(x['SHOP'],x['CODE']))
    for item in bill_items:
        print(f"{item['SHOP']:<10}{item['CODE']:<10}{item['CATEGORY']:<10}{item['PRICE']:<10}{item['Gov']:<10}{item['Cust']:<10}")
    
