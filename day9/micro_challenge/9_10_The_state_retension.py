# Goal: Write a generator that calculates a "Running Average". 
# Deep dive: The generator remembers the total and count variables between yields. This
#            elimanites the need for global variables or class attibutes.

def running_avg():
    total = 0
    counter = 0
    while True:
        val = yield total, counter
        total = val + total
        counter = counter + 1

avg = running_avg()

next(avg)

print(avg.send(5))
print(avg.send(10))

cal = avg.send(20)

print(cal[0]/cal[1])


