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