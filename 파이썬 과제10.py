import os
import pickle
from datetime import datetime

def save(a):
  with open(filename, 'wb') as file:
    pickle.dump(a, file)
def load():
  with open (filename,'rb') as file:
    a = pickle.load(file)
  return a

def input_scores():
  scores = []
  print('[점수입력]')
  cnt = 1
  while True:
    score = int(input(f'#{cnt}? '))
    if score < 0:
      break
    else:
      scores.append(score)
    cnt += 1
  print('')
  return scores

def get_average(lst):
  hap = 0
  for i in range(len(lst)):
    hap += scores[i]
  return hap / len(lst)

def show_scores(lst):
  print('[점수 출력]')
  print('개인점수: ',end=' ')
  for i in range(len(lst)):
    print(lst[i], end=' ')

# 주 프로그램 부
filename = 'score.bin'

if os.path.exists(filename):
  print('[파일 읽기]\n')
  scores = load()
  show_scores(scores)
  print(f'\n평균: {get_average(scores):.1f}')
  save(scores)
else:
  scores = input_scores()
  show_scores(scores)
  print(f'\n평균: {get_average(scores):.1f}')
  save(scores)
