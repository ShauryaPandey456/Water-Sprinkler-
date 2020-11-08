# Initiation for connection to water sprinkler 
import time
i = 0
while True: 
    time.sleep(1)
    print(time.strftime('%I:%M:%S'))
    if i == 4:
        import Client
        i = 0

    else:
        i = i + 1
   
