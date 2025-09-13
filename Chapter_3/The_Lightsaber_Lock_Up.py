
import os
import time

W = 100
hiltL, hiltR = "[||", "||]"
blue = "\033[94m"; red = "\033[91m"; reset = "\033[0m"
steps = (W - len(hiltL) - len(hiltR)) // 2

# extend blades
for i in range(steps + 1):
    os.system('cls' if os.name=='nt' else 'clear')
    left  = blue + "="*i + reset
    right = red  + "="*i + reset
    gap = W - len(hiltL) - len(hiltR) - 2*i
    print(hiltL + left + " "*max(0, gap) + right + hiltR)
    time.sleep(0.05)

# clash sparkle (now with a simple while loop)
spark_chars = "✦✧✱✹*"
k = 0
cycles = 10
while cycles > 0:
    os.system('cls' if os.name=='nt' else 'clear')
    spark = (spark_chars[k % len(spark_chars)]) * 3
    print(hiltL + blue + "="*steps + reset + spark + red + "="*steps 
          + reset + hiltR)
    time.sleep(0.08)
    k += 1
    cycles -= 1