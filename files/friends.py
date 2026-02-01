friends = input("Enter your friends' names, separated by commas: ").split(',')
friends = [friend.strip() for friend in friends]
people = open('people.txt', 'r')
people_list = people.readlines()

people.close()

friends_set = set(friends)
people_set = set(person.strip() for person in people_list)
nearby_friends_set = friends_set.intersection(people_set)
print("Common friends found in the file:")

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in nearby_friends_set:
    print(f"{friend} is nearby.")
    nearby_friends_file.write(friend + '\n')

nearby_friends_file.close()