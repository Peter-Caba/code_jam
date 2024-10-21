import time 

count = 17
while True:
    print(f"Bullets: {count}")
    if count > 0:
       count -= 1
       time.sleep(0.1)
    else:
        count: 17 
        print("reload...")
        time.sleep(2)
        break