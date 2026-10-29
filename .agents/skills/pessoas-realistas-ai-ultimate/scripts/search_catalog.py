"""Offline lexical search; exact retrieval never edits prompt text."""
import argparse,json,re,unicodedata
from pathlib import Path
CATALOG=Path(__file__).resolve().parents[1]/'assets/prompt-catalog.json'
def normalize(s):
 s=''.join(c for c in unicodedata.normalize('NFKD',s.lower()) if not unicodedata.combining(c))
 return ' '.join(re.findall(r'[a-z0-9]+',s))
ALIASES={'ruiva':'ruiv','ruivo':'ruiv','idosa':'idos','idoso':'idos','loira':'loir','loiro':'loir','morena':'moren','moreno':'moren','mulheres':'mulher','homens':'homem','branca':'branc','branco':'branc','negra':'negr','negro':'negr','tatuada':'tatuad','tatuado':'tatuad','macro':'texturas'}
STOP={'quero','um','uma','o','a','de','do','da','com','para','prompt','prompts','me','mostre','realista','realistas','por','favor','rosto','rostos','versao'}
def tokens(s):return [ALIASES.get(t,t) for t in normalize(s).split() if t not in STOP]
def search(rows,query):
 n=normalize(query)
 for row in rows:
  if n in (normalize(row['id']),normalize(row['title'])):return [row]
 ts=tokens(query)
 if not ts:return []
 scored=[]
 for row in rows:
  hay=set(tokens(row['title']+' '+row['collection']+' '+row['tool']))
  if all(t in hay for t in ts):
   score=sum(t in tokens(row['title']) for t in ts);scored.append((score,row))
 return [row for score,row in sorted(scored,key=lambda x:(-x[0],x[1]['id']))]
def main():
 p=argparse.ArgumentParser();p.add_argument('query');p.add_argument('--original',action='store_true');a=p.parse_args()
 rows=search(json.loads(CATALOG.read_text(encoding='utf-8')),a.query)
 if a.original:
  if len(rows)!=1:p.error('Use a unique ID/title; multiple or no matches')
  print(rows[0]['prompt'],end='')
 else:print(json.dumps([{k:r[k] for k in ('id','title','collection','tool')} for r in rows],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
