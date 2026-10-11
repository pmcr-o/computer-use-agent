import argparse,json,hashlib,pathlib
p=argparse.ArgumentParser();p.add_argument('--steps',required=True);p.add_argument('--trails',required=True);p.add_argument('--id',required=True);p.add_argument('--adapter-route',default='');p.add_argument('--output',required=True);a=p.parse_args()
steps=json.loads(pathlib.Path(a.steps).read_text());trails=json.loads(pathlib.Path(a.trails).read_text());allowed={'open','navigate','click','type','select','submit','wait','capture','read','terminal'}
if not isinstance(steps,list) or not steps:raise SystemExit('steps must be nonempty list')
for i,s in enumerate(steps):
 if s.get('action') not in allowed:raise SystemExit(f'unsupported action at {i}')
 if any(k.lower() in {'password','secret','token','apikey','api_key'} for k in s):raise SystemExit('secret-bearing step fields forbidden')
body={'schema':'pmcro.computer-use-procedure/v1','id':a.id,'status':'CANDIDATE','adapterRoute':a.adapter_route,'adapterStatus':'NOT-YET-VERIFIED','trailRefs':trails,'steps':steps}
body['procedureDigest']=hashlib.sha256(json.dumps(body,sort_keys=True,separators=(',',':')).encode()).hexdigest();pathlib.Path(a.output).write_text(json.dumps(body,indent=2)+'\n');print(a.output)
