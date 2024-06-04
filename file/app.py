

filename="fibo"

fibo=[0,1]

## Append

# with open(f"{filename}.txt","a") as file:
#     for i in range(1,100):
#       a=i-1
#       b=i
#       no=fibo[a]+fibo[b]
#       print(no)
#       fibo.append(no)
#       file.write(f"{no}\n")

with open("fibo.txt","r")as file:
    for line in file:
        with open("fibo2.txt","a") as file:
            file.write(f"Python did this.{line} \n")