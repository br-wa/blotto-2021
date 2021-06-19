import pandas as pd
import argparse
import math
from round0 import round0
from round1 import round1
from round2 import round2
from round3 import round3
from round4 import round4

comps = [round0, round1, round2, round3, round4]

parser = argparse.ArgumentParser()
parser.add_argument("infile")
parser.add_argument("tiebreak")
parser.add_argument("scorecol_label")
parser.add_argument("round", type=int)
args = parser.parse_args()

infile = args.infile
tiebreak = args.tiebreak
scorecol_label = args.scorecol_label
comp = comps[args.round]

df = pd.read_csv(infile, low_memory=False)
with open(tiebreak, 'r') as tb:
    tiebreak_arr = tb.read().split('\n')

n_players = df.shape[0]
score = [0] * n_players
for i in range(n_players):
    for j in range(i):
        x, y = comp(df['Submission'][i], df['Submission'][j])
        score[i] += x
        score[j] += y

df['Score'] = score 
tiebreak_nums = [n_players + 1] * n_players

for i in range(len(tiebreak_arr)):
    line = tiebreak_arr[i]
    names = line.split(',')
    for j in range(n_players):
        if df['Name'][j] in names:
            tiebreak_nums[j] = i 

df['Tiebreak'] = tiebreak_nums

df = df.sort_values('Tiebreak').reset_index(drop=True)
df = df.sort_values('Score', kind='mergesort', ascending=False).reset_index(drop=True) #need to use stable sort here
eps = 1e-6
ranks = []

tb = open(tiebreak, 'w')
current_list = ""
for i in range(n_players):
    if i > 0 and df['Tiebreak'][i] == df['Tiebreak'][i-1] and abs(df['Score'][i] - df['Score'][i-1]) < eps:
        ranks.append(ranks[i-1])
        current_list += (',' + df['Name'][i])
    else:
        ranks.append(i+1)
        if i > 0:
            tb.write(current_list + '\n')
        current_list=df['Name'][i]
if len(current_list) > 0:
    tb.write(current_list)
tb.close()

df['Rank'] = ranks

print(
    "\\begin{center}",
    "\t\\begin{tabular}{c c c c} \\\\",
    f"\t\t& Name & Submission & {scorecol_label} \\\\ \hline",
    sep='\n'
)

for idx, row in df.iterrows():
    rank, name, score, sub = row['Rank'], row['Name'], row['Score'], row['Submission']
    if rank <= math.ceil(0.5 * n_players):
        print(f"\t\t{rank} & \\textbf{{{name}}} & {sub} & {score} \\\\")
    else:
        print(f"\t\t{rank} & & {sub} & {score} \\\\")

print(
    "\t\\end{tabular}",
    "\\end{center}",
    sep='\n'
)
