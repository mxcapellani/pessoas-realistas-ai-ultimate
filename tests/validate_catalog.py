from pathlib import Path
import re,json,hashlib,collections,sys,yaml
B=Path('.agents/skills/pessoas-realistas-ai-ultimate')
class Unique(yaml.SafeLoader):pass
def unique(loader,node,deep=False):
 d={}
 for k,v in node.value:
  key=loader.construct_object(k,deep=deep)
  if key in d:raise ValueError('duplicate YAML key')
  d[key]=loader.construct_object(v,deep=deep)
 return d
Unique.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique)
def validate(root):
 root=Path(root);e=[]
 for p in ('README.md','LICENSE','NOTICE.md','docs/SOURCE_CATALOG.md','docs/catalog-manifest.json',str(B/'SKILL.md'),str(B/'assets/prompt-catalog.json')):
  if not (root/p).is_file() or not (root/p).read_text().strip():e.append('missing '+p)
 if e:return e
 t=(root/B/'SKILL.md').read_text()
 try:
  assert t.startswith('---\n');d=yaml.load(t.split('---',2)[1],Loader=Unique);assert set(d)=={'name','description'} and d['name']=='pessoas-realistas-ai-ultimate' and len(d['description'])>60
 except Exception:e.append('invalid metadata')
 try:
  rows=json.loads((root/B/'assets/prompt-catalog.json').read_text());manifest=json.loads((root/'docs/catalog-manifest.json').read_text());s=(root/'docs/SOURCE_CATALOG.md').read_text();originals=re.findall(r'```text\n(.*?)```',s,re.S)
  assert len(rows)==len(originals)==manifest['prompt_count']==39
  assert [r['id'] for r in rows]==[f'P{i:03d}' for i in range(1,40)]
  assert dict(collections.Counter(r['collection'] for r in rows))==manifest['collections']
  assert list(manifest['collections'].values())==[20,9,2,4,4]
  refs='\n'.join(p.read_text() for p in (root/B/'references').glob('*.md'))
  for row,orig,m in zip(rows,originals,manifest['prompts']):
   assert row['prompt']==orig
   assert hashlib.sha256(orig.encode()).hexdigest()==row['prompt_sha256']==m['prompt_sha256']
   assert row['id']==m['id'] and row['title']==m['title']
   assert row['prompt'] in refs and row['id'] in t and row['tool']
 except Exception:e.append('catalog integrity/count/hash/source mismatch')
 for p in root.rglob('*'):
  if not p.is_file() or '__pycache__' in p.parts:continue
  if p.suffix in ('.md','.json') and ('signature=' in p.read_text() or 'expirationTimestamp=' in p.read_text()):e.append('temporary signed URL present')
 for p in root.rglob('*.md'):
  for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if '://' in link or link.startswith('#'):continue
   target=(p.parent/link.split('#')[0]).resolve()
   if not target.is_relative_to(root.resolve()) or not target.exists():e.append('bad link '+link)
 return e
if __name__=='__main__':
 e=validate(Path(__file__).resolve().parents[1]);print('\n'.join(e) if e else 'PASS: YAML, 39 exact originals, counts, hashes, references and no temporary signed URLs');sys.exit(bool(e))
