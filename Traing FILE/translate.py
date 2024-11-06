#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {99:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))