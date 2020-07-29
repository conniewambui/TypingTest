import matplotlib.pyplot as plb
import time as t

times = []
errors = 0

print("This program will help you type faster. You will have to type 'coding' as fast as you can for four times")
print(input("Press enter to continue : "))

while len(times) < 4:
    start = t.time()
    word = input ("Type the word: ")
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)

    if (word.lower () != "coding"):
        errors += 1

print( "You made " + str(errors) + " errors.")
print("Let's see your speed")

t.sleep(5)

x = [1,2,3,4]
y = times
plb.plot(x,y)
plb.show()