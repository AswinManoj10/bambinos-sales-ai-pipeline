# bambinos-sales-ai-pipeline
# Bambinos.live: AI Post-Demo Call Intelligence Pipeline (Sales Track)

An AI pipeline that audits counselling calls, cleans CRM fields and drafts
hyper-personalised parent follow-ups.

## What is in this repo
- prompts/ : the 3 prompts (call audit, CRM extract, WhatsApp follow-up)
- results/ : audit, CRM record and WhatsApp output for the 6 sample calls
- workflows_or_scripts/run_pipeline.py : script that automates the same steps
- Case report PDF : scorecard, CRM taxonomy, workflow, funnel math, rollout

## How results were generated
The prompts were run in Claude (chat) on each transcript with the policy CSV.
The script automates the same steps (needs ANTHROPIC_API_KEY).

## Key design choices
- Strict CRM taxonomy with allowed values only
- Every score backed by a verbatim transcript quote
- Hard compliance flags cap the score and escalate to a manager
- Opt-out requests override follow-up cadence
- Payment status verified in the payment system, never from call text

## Known limitations
- The script has a TODO: it does not yet join the CRM and demo CSVs
- Some outputs were fixed by hand (JSON formatting, quote checks)
- Calls 5 and 6: CRM/WhatsApp outputs pending (delete this line if done)
