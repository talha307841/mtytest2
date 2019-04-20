import nltk
import re
Dicop={"<subtarction operator = ->":"-","<addition operator = +>":"+","<multiplication op = *>":"*","<division op = />":"/","<not op = !>":"!","<and op = &&>":"&&","<or op = ||>":"||","<equal op = ==>":"==","<Question mark op = ?>":"?","<open round bracket = (>":"(","<closs round bracket=)>":")","<open curly bracket = {>":"{","<close curly bracket = }>":"}",",at the rate op = @>":"@","<hash = #>":"#","<remider op =%>":"%","<exponent op = ^>":"^","<assignment operator = =>":"=","<Address op = &>":"&","<dollar = $>":"$","<under score = _ >":"_","<semi colon = ;>":";","<comma= ,>":",","<colon = :>":":","<shift right = >> >":">>","<shift left = << >":"<<","<increment operator = ++ >":"++","<decrement operator = -- >":"--","<less than equal to operator = <= >":"<=","<greater than and equal to operator = >= >":">="}

print(type(Dicop))
op = input("enter your operator: ")

if op in Dicop.values():
    print(list(Dicop.keys())[list(Dicop.values()).index(op)])
     
else:
    print("your input is not in the dictionary")
           
Dickw={"<integer= int>":"int","<float = float>":"float","<character = char>":"char","<string = string>":"string","<boolean = bool>":"bool","<key word =Goto>":"goto","<for loop = for>":"for"}
print(type(Dickw))

kw = input("enter any key word: ")

if kw in Dickw.values():
    print(list(Dickw.keys())[list(Dickw.values()).index(kw)])
else:
    print("the key word you entered is not in dictionary do you wanna add it")

Dicva={"<variable = variable>":"i"}

def input_type(userInput):
    if userInput in ("true","false"):
        return "boolean"
    elif re.match("^\d+?\.\d+?$",userInput):
        return "float"
    elif userInput.isdigit():
        return "int"
    else:
        return "string"
res = input("enter any number or string to find its data type: ")
print(input_type(res))
x=input("enter your string to split: ")
y=x.split()
print(y)


i = 0;
for i in range(0,100):
    
    if y[i] in Dicop.values():
        print(list(Dicop.keys())[list(Dicop.values()).index(y[i])])
    elif y[i] in Dickw.values():
        print(list(Dickw.keys())[list(Dickw.values()).index(y[i])])
    elif y[i] in Dicva.vales():
        print(list(Dicva.keys())[list(Dicva.values()).index(y[i])])
    else:
        print("synta error")


