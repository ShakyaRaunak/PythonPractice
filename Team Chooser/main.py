# https://codeclubprojects.org/en-GB/python/team-chooser/
from random import choice

file = open('players.txt', 'r')
players = file.read().splitlines()
print(players)
print("------------------------------------")

teamNames = open('team-names.txt', 'r').read().splitlines()
teamA = []
teamB = []
teamC = []

while len(players) > 0:
    playerA = choice(players)
    print("Chosen for team A : ", playerA)
    teamA.append(playerA)
    players.remove(playerA)
    print("Players left : %s" % players)

    if not players:
        break

    playerB = choice(players)
    print("Chosen for team B : ", playerB)
    teamB.append(playerB)
    players.remove(playerB)
    print("Players left : %s" % players)

    if not players:
        break

    playerC = choice(players)
    print("Chosen for team C : ", playerC)
    teamC.append(playerC)
    players.remove(playerC)
    print("Players left : %s" % players)

print("------------------------------------")

print("Here are your teams :")
teamAName = choice(teamNames)
print("Team {} : {}".format(teamAName, teamA))
teamNames.remove(teamAName)
teamBName = choice(teamNames)
print("Team {} : {}".format(teamBName, teamB))
teamNames.remove(teamBName)
teamCName = choice(teamNames)
print("Team {} : {}".format(teamCName, teamC))
