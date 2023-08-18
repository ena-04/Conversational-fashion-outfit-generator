input_text = 'Sure, here is a Karva Chauth outfit idea for a 35 year old woman from Muzaffarpur who prefers pink, black, and purple colors:\n\n* Anarkali suit in pink, black, and purple with a matching salwar.\n* Pumps in black or purple.\n* Traditional jewelry such as a necklace, earrings, and bangles.\n* A bindi and mehndi to complete the look.\n\nThis outfit is traditional and elegant, and it is sure to make you feel confident and beautiful on Karva Chauth.\n\n'

output = []
lines = input_text.split('\n')

for line in lines:
    line = line.strip()
    if line.startswith('*'):
        output.append(line.split('*')[1].strip())

print(output)
