# .csv comma separated values


with open('README.md', 'w') as file:
    file.write('basic python')

with open('README.md', 'r') as file:
   read = file.read()
   print(read)