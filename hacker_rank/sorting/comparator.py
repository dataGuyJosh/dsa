from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        print("{} {}".format(self.name, self.score))

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0


players = ['amy 100', 'david 100', 'heraldo 50', 'aakansha 75', 'aleksa 150']

data = []

for p in players:
    name, score = p.split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))

for i in data:
    print(i.name, i.score)
