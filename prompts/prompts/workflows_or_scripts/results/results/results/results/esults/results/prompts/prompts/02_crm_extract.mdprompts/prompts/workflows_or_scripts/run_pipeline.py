import os, json, glob
import anthropic

client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY
MODEL = 'claude-sonnet-4-6'      # check the docs for the current model name

def read(p):
    return open(p, encoding='utf-8').read()

def ask(system, user):
    r = client.messages.create(model=MODEL, max_tokens=2000, temperature=0,
        system=system, messages=[{'role': 'user', 'content': user}])
    text = r.content[0].text
    text = text[text.find('{'): text.rfind('}') + 1]
    return json.loads(text)

def unverified_quotes(obj, transcript):
    t = ' '.join(transcript.lower().split())
    bad = []
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ('evidence', 'quote', 'objection_evidence') and v:
                    if ' '.join(str(v).lower().split()) not in t:
                        bad.append(v)
                else:
                    walk(v)
        elif isinstance(o, list):
            for i in o:
                walk(i)
    walk(obj)
    return bad

policy = read('sales/data/reference_courses_pricing_and_compliance_policy.csv')
os.makedirs('results', exist_ok=True)

for path in sorted(glob.glob('sales/call_transcripts/*')):
    name = os.path.splitext(os.path.basename(path))[0]
    transcript = read(path)
    ctx = 'POLICY:\n' + policy + '\n\nTRANSCRIPT:\n' + transcript
    # TODO: load 1_crm_leads.csv and 2_demo_class_evaluations.csv with pandas,
    # find the row for this lead_id and append it to ctx

    audit = ask(read('prompts/01_audit.md'), ctx)
    crm = ask(read('prompts/02_crm_extract.md'), ctx)
    follow = ask(read('prompts/03_followup.md'),
                 'CRM JSON:\n' + json.dumps(crm) + '\n\n' + ctx)

    audit['unverified_quotes'] = unverified_quotes(audit, transcript)
    crm['unverified_quotes'] = unverified_quotes(crm, transcript)
    with open('results/' + name + '.json', 'w', encoding='utf-8') as f:
        json.dump({'audit': audit, 'crm': crm, 'followup': follow}, f,
                  indent=2, ensure_ascii=False)
    print('done', name, audit.get('total_100'), len(audit.get('compliance_flags', [])))
