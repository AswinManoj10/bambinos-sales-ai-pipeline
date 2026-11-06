## 2. Cleaned CRM Record

```json
{
  "intent_label": "Cold",
  "intent_score": 1,
  "primary_objection": "Trust_Concern",
  "secondary_objection": null,
  "objection_evidence": "That sounds like a fake sales promise.",
  "child_demo_highlight": "Read the word 'train' as 'truck' at the start of the class (parent-reported).",
  "learning_gap": "Father is worried about adding screen time for a 7-year-old who already watches cartoons on the iPad, and about Vihaan reading 'train' as 'truck'.",
  "next_best_action": "Escalate_To_Manager",
  "follow_up_by": null,
  "confidence": "High",
  "cleaned_note": "Father ended the call and asked not to be contacted again after the counsellor promised Rank 1 and Harry Potter reading in 30 days, an unauthorised discount and refund, and threatened to blacklist the child if he did not pay in 5 minutes."
}
```

## 3. Routing Status (guardrail result)

- Status: ESCALATED. 6 hard compliance flags. Manager alerted immediately.
- Score is 0/100 and capped by the hard-flag rule.
- Opt-out rule applied: the father said not to contact him again, so all automated WhatsApp messages are stopped. The opt-out overrides the follow-up cadence.
- Manager actions: review the recording, decide whether to send ONE apology and correction, cancel any live payment link (the link showed Rs. 5,500 against the policy fee of Rs. 9,500), and run an internal review of the counsellor.

## 4. WhatsApp Sequence

```json
{
  "stop": true,
  "reason": "The lead is Cold and the father said 'Do not call me again!', so no automated follow-up should go out. All six hard compliance flags (guaranteed outcomes, false refund promise, unauthorised discount, misquoted price, false 1-on-1 claim, blacklist threat) have been escalated to a manager.",
  "messages": []
}
```

If the manager approves a single apology and correction, it may only use official terms: the Rs. 9,500 fee, no guaranteed results, a 100% refund within 14 days (up to 4 classes attended) then pro-rata, a maximum 10% discount, and no blacklisting.

## 5. Review Notes
- Messages withheld: the opt-out request overrides the manager-approval cadence. A manager decides whether to send one apology.
- Taxonomy change: added the primary_objection value Trust_Concern, because none of the original values fitted a trust and screen-time concern.
- Check the system for the Rs. 5,500 payment link, the order and any discount code, and cancel any live link.
- The 'train' and 'truck' detail and the father's praise for Ms. Simran come from the parent only.
- Counsellor claims about hacking a manager's quota and bypassing the website policy need a separate internal review.
