
s1="Welcome to Python World Game."
#請使用str.split以空格做分割。
s2="Can you can a can as a canner can can a can?"
#請使用str.count 算出有幾個'a'
s3="Few free fruit flies fly from flames."
#4 請使用str.find 或str.index 找出"fly" 第一次出現的位子
s4="Czngrxtulxtizns, yzu hxve pxssed the czmpetitizn."
#請使用str.replace 把'z' 替換成 'o'，以及把'x'替換成'a'

print(s1)
print(s1.split())

print(s2)
print(s2.count("a"))

print(s3)
print(s3.find("fly"))

print(s4)
s5=s4.replace("z","o")
print(s5.replace("x","a")) #亦可print(s4.replace("z","o").replace("x","a"))
