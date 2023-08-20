input_text = 'Sure, here is a wedding outfit suggestion for a male guest:\n\n* Navy blue blazer\n[Image of Navy blue blazer men wedding outfit]\n* *Bottom:* Charcoal gray dress pants\n[Image of Charcoal gray dress pants men wedding outfit]\n* *Shoes:* Black leather oxfords\n[Image of Black leather oxfords men wedding outfit]\n* *Jewelry:* Silver watch and cufflinks\n[Image of Silver watch and cufflinks men wedding outfit]\n* *Accessories:* Pocket square\n[Image of Pocket square men wedding outfit]\n\nThis outfit is classic and elegant, and it is perfect for a formal wedding. The navy blue blazer and charcoal gray dress pants are a timeless combination, and the black leather oxfords will give you a polished look. The silver watch and cufflinks will add a touch of luxury, and the pocket square will add a pop of color.\n\nI hope this helps!'

output = []
lines = input_text.split('\n')

for line in lines:
    line = line.strip()
    if line.startswith('*'):
        # output.append(line)
        item_parts = line.split(':*')
        if len(item_parts) > 1:
            output.append(item_parts[1].strip())
        else:
            output.append(line.split('*')[1].strip())

print(output)
