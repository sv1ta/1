from random import *
s1 = randrange(1,9)*100
s2 = randrange(1,9)*10
s3 = randrange(1,9)
s = s1 + s2 +s3 #число, которое сохраняет путь, пройденный каждым туристом
print(s)
k1 = s/100 #прошел первый турист
k2 = s/10%10 #прошел второй турист
k3 = s%10 #прошел третий турист
k = k1 + k2 + k3 #общий путь, который они прошли
print('общий путь, который прошли туристы =', k)
