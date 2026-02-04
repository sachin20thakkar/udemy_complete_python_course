class Club:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __len__(self):
        return len(self.members)

    def __getitem__(self, index):
        return self.members[index]
    
    def __repr__(self):
        return f"Club({self.name}, Members: {len(self.members)})"

    def __str__(self):
        return f"Club: {self.name} with Members: {len(self.members)}"

    def add_member(self, member):
        self.members.append(member)

    def show_members(self):
        for member in self.members:
            print(member.get_info())


club = Club("Chess Club")
club.add_member("Alice")
club.add_member("Bob")
club.add_member("Charlie")

print(club)  # Output: Club: Chess Club with Members: 3
