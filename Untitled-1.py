print("___Welcome to the pro remote control car store!!___")
print("Here is the products")
product_list = ["1 traxxas Max Slash $1000 ", "2 Arrma Kraton $2000 " , "3 mjx/hyper go 20208 brushless truck $500 ", "4 haiboxing 18859a $150 ", "5 walmart cheap rcs $40"]
product_price = ["1000", "2000" , "500", "150", "40"]

for item in product_list:
    print( item)
question = "yes"
total_cost = 0

while question == "yes":
    sequence_num = int(input("enter the number of the product you want to buy from 1-5"))
    qty = input("how many do you want to buy")
    unit_price = product_price[sequence_num-1]
    qty = int(qty)
    unit_price = float(unit_price)
    total_cost += qty * unit_price
    print(product_list[sequence_num-1])
  
    question=(input("yes/no" "would you like to buy anymore products?"))

cif_student = input("are you a member of our CIF program?(yes/no)")
if cif_student == "yes":
    total_cost = total_cost*(1-0.5) 
    print("you got 50% dizcount")
else:
    print("too bad you did not join CIF")
    
print("your price is")
print(total_cost)
print("thank you for shopping in this store. hope you enjoy your experince, come again soon to waste your money! also leave a review")
star_review = input("please write a review")
print(star_review)

