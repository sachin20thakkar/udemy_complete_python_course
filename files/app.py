my_file = open('data.txt', 'r')
file_contents = my_file.read()

my_file.close()
print(file_contents)

user_name = input('Enter your name: ')
my_file_write = open('data.txt', 'w')
my_file_write.write(f"Hello {user_name}")
my_file_write.close()
