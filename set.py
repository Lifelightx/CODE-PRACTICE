#Q1.
my_set = {"Jeebanjyoti","Mallik"}
a = list(my_set)
f_name = a[0]
print(f_name)
#Q2.
#FIND THE LENGTH OF THE BELOW LIST
li = ["a", "b", "b","d", "e", "f", "a"]
print(len(li))
#Q3
li = ['a','b', 'b', 'd','e', 'f', 'a']
z = li.count('b')
print(z)
#Q4
z1 = input("Enter an word: ")
m1 = z1[::]
m = z1[::-1]
if m1 == m:
    print("The word is palindrom")
else:
    print("The word is not palindrom")
#Q6
L = ['a','b',['cc','dd', ['eee','fff']],'g','h'] 
x = L[2]
m = x[2]
n = m[0]
print(n)
#Q5
cryptowallet = {'makeerCommision':0, 'takerCommission':0, 'buyerCommission':0, 'sellerCommission':0,'canTrade':True,'canWidthdraw':False, 'candeposite':True, 'accountType':['SPOT','ONLINE'],'balances':[{'assset':'BTC','free':'₹100','locked':2.0},{'assset':'BNB','free':'₹150','locked':1.0},{'assset':'USD','free':'₹500','locked':0.0},{'assset':'ETH','free':'₹100','locked':2.0}]}
print(cryptowallet['accountType'])
x = cryptowallet['balances']
y = x[3]
print(y['free'])
