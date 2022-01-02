with open("input.txt") as f:
    input = list(map(int,f.readline().split(',')))
count = 0

input.sort()

if (len(input)% 2 == 0):
    median = int((input[int(len(input)/2)] + input[int(len(input)/2) - 1])/2)
else:
    median = input[int(len(input)/2)]

fuel = 0
sum = 0
for each in input: 
    sum += each
avg = round(sum / len(input), 0)
print(f"avg exacte: {sum/len(input)}")

for each in input:
    tmp = (abs(each - avg) + 1)/2 * abs(each - avg)
    fuel += tmp

print(f"median: {median}, average: {avg}, fuel required: {fuel}")