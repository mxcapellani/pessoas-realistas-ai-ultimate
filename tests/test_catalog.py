import unittest,importlib.util,json,tempfile,shutil,subprocess,sys
from pathlib import Path
from validate_catalog import validate,B
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('search',R/B/'scripts/search_catalog.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
ROWS=json.loads((R/B/'assets/prompt-catalog.json').read_text())
class SearchTests(unittest.TestCase):
 def test_id(self):self.assertEqual(m.search(ROWS,'p001')[0]['title'],'Rosto Realista Ruiva')
 def test_title(self):self.assertEqual(m.search(ROWS,'ROSTO REALISTA MULHER MEIA IDADE')[0]['id'],'P010')
 def test_elderly_man(self):self.assertEqual([r['id'] for r in m.search(ROWS,'Quero um homem idoso realista')],['P019'])
 def test_ambiguous_brunette(self):self.assertEqual([r['id'] for r in m.search(ROWS,'morena')],['P003','P004','P005'])
 def test_unknown(self):self.assertEqual(m.search(ROWS,'astronauta robô'),[])
 def test_tool_variant(self):self.assertEqual(len(m.search(ROWS,'fundo neutro Seedream')),5)
 def test_duplicates_preserved(self):self.assertEqual(ROWS[31]['prompt'],ROWS[33]['prompt']);self.assertNotEqual(ROWS[31]['id'],ROWS[33]['id'])
 def test_cli_literal(self):
  r=subprocess.run([sys.executable,str(R/B/'scripts/search_catalog.py'),'P001','--original'],capture_output=True,text=True,check=True);self.assertEqual(r.stdout,ROWS[0]['prompt'])
 def test_cli_ambiguous_fails(self):
  r=subprocess.run([sys.executable,str(R/B/'scripts/search_catalog.py'),'morena','--original'],capture_output=True,text=True);self.assertNotEqual(r.returncode,0)
class IntegrityTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.r=Path(t.name)/'package';shutil.copytree(R,self.r)
 def test_valid(self):self.assertEqual(validate(self.r),[])
 def test_original_mutation_detected(self):
  p=self.r/B/'assets/prompt-catalog.json';d=json.loads(p.read_text());d[0]['prompt']+='Modified';p.write_text(json.dumps(d));self.assertTrue(validate(self.r))
 def test_missing_reference(self):
  (self.r/B/'references/rostos-realistas.md').unlink();self.assertTrue(validate(self.r))
 def test_missing_record(self):
  p=self.r/B/'assets/prompt-catalog.json';d=json.loads(p.read_text());d.pop();p.write_text(json.dumps(d));self.assertTrue(validate(self.r))
 def test_wrong_name(self):
  p=self.r/B/'SKILL.md';p.write_text(p.read_text().replace('name: pessoas-realistas-ai-ultimate','name: other',1));self.assertTrue(validate(self.r))
 def test_signed_url_detected(self):
  p=self.r/'docs/SOURCE_CATALOG.md';p.write_text(p.read_text()+'\nsignature=temporary');self.assertTrue(validate(self.r))
if __name__=='__main__':unittest.main()
