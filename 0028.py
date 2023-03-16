team_name = []
team_score = []
score = [0, 0, 0, 0]
result = 0
team = []

for i in range(4):
    team_name.append(input())
for i in range(4):
    team_score.append(list(map(int, input().split())))
    team.append({
        "name": team_name[i],
        "score": 0,
        "hit": 0,
        "_hit": 0
    })

for i in range(len(team_score)):
    for j in range(len(team_score[i])):
        if j > i:

            team[i]['hit'] += team_score[i][j]
            team[j]['_hit'] += team_score[i][j]

            team[i]['_hit'] += team_score[j][i]
            team[j]['hit'] += team_score[j][i]

            if team_score[i][j] > team_score[j][i]:
                team[i]['score'] += 3
            elif team_score[j][i] > team_score[i][j]:
                team[j]['score'] += 3
            elif team_score[i][j] == team_score[j][i]:
                team[i]['score'] += 1
                team[j]['score'] += 1

newlist = sorted(
    team, key=lambda d: (d['score'], (d['hit'] - d["_hit"]), d['hit']), reverse=True)

# print(newlist)

for e in newlist:
    print(e['name'], e['score'])
