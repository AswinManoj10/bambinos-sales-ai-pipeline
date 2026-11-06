# Call 1: Aarav / Divya (Counsellor: Rohan)

## 1. Call Audit

```json
{
  "scores": {
    "rapport_child_praise": {"score": 3, "evidence": "did you see that huge smile on his face at the end when he finished his space superhero story?"},
    "diagnosing_pain": {"score": 3, "evidence": "what is the #1 question he usually asks before saying yes to a program for Aarav?"},
    "curriculum_pitch": {"score": 3, "evidence": "Over 48 sessions, we move him from story prompts to impromptu speaking, debate, and voice modulation."},
    "price_framing": {"score": 2, "evidence": "Rs. 12,000 total—that comes to Rs. 250 per live session."},
    "objection_handling": {"score": 2, "evidence": "If I send you a crisp 60-second summary on WhatsApp showing Ms. Rhea's exact feedback on Aarav's 'asteroid' story today"},
    "urgency_trial_close": {"score": 2, "evidence": "I'll provisionally hold that 6th seat in Ms. Rhea's Tue-Thu 6 PM batch until 11:00 AM tomorrow."},
    "compliance_professionalism": {"score": 2, "evidence": "And it's backed by our official 14-day, 100% risk-free refund policy."}
  },
  "total_100": 82,
  "compliance_flags": [
    {
      "type": "refund_claim_incomplete_vs_policy",
      "severity": "medium",
      "quote": "And it's backed by our official 14-day, 100% risk-free refund policy."
    }
  ],
  "coaching": {
    "win": "Rohan, you built excellent rapport by opening with Aarav's smile and tying Ms. Rhea's specific feedback ('asteroid', the Superhero Hook) to the mother's own worry about his shyness.",
    "fix": "The parent's real objection was needing her husband's buy-in, and you only promised to send a summary. Next time, offer a short three-way call and mention the instalment option (50% down, 50% at Day 30) while the husband is still deciding. Also state the refund terms precisely, including the 4-class limit.",
    "better_line": "Ma'am, would it help if I joined a quick 5-minute call with you and your husband at 8:30 tonight? And just so you both know, the refund covers the first 14 days or up to 4 classes, and you can pay 50% now and 50% at Day 30."
  }
}
```

## 2. Cleaned CRM Record

```json
{
  "intent_label": "Warm",
  "intent_score": 7,
  "primary_objection": "Spouse_Decision",
  "secondary_objection": null,
  "objection_evidence": "my husband wasn't home during the Zoom demo today, and we always decide together on Aarav's classes.",
  "child_demo_highlight": "Unmuted at minute 18 and spoke for 45 seconds with full hand gestures using the 3-step 'Superhero Hook' structure.",
  "learning_gap": "Aarav writes great answers in his notebook but never raises his hand in class and hides behind his mother when relatives ask him something; he freezes when put on the spot.",
  "next_best_action": "Send_Demo_Recap",
  "follow_up_by": "tomorrow 11:00 AM",
  "confidence": "High",
  "cleaned_note": "Mother liked the trial, fee and Tue-Thu 6 PM batch, but needs her husband's approval after he sees a WhatsApp demo recap; the counsellor tentatively held the last seat and the parent agreed to a follow-up call at 11 AM tomorrow."
}
```

## 3. WhatsApp Follow-Up Sequence

```json
{
  "stop": false,
  "messages": [
    {
      "touch": 1,
      "send_after": "2 hours",
      "text": "Hi Divya ma'am, Rohan here from Bambinos.live 😊 Just wanted to share one lovely moment from today: Aarav unmuted and spoke for 45 seconds with full hand gestures, using Ms. Rhea's 'Superhero Hook' (Beginning, Problem, Rescue). It was a joy to see!",
      "approval": "auto"
    },
    {
      "touch": 2,
      "send_after": "Day 2",
      "text": "Hi ma'am, about your husband's question on whether this is just another grammar class: it isn't. Young Communicators is live speaking practice in small groups of max 6 kids, with a Stage Showcase every 4th week where parents watch live. Happy to join a quick call with you both, whenever suits.",
      "approval": "rep"
    },
    {
      "touch": 3,
      "send_after": "Day 4-5",
      "text": "Hi ma'am, hope you and sir got a chance to talk about Aarav's class. No rush at all. For reference, fees can be paid 50% now and 50% at Day 30, and the 14-day refund applies (up to 4 classes attended). Shall I check the Tue-Thu 6 PM batch for you?",
      "approval": "rep"
    }
  ]
}
```

## 4. Review Notes
- Total score: 81.67 rounded to 82.
- Compliance: medium flag for an incomplete refund statement. No hard flags.
- Items to verify against the policy CSV: the seat hold, the refund terms, and the 50/50 payment plan.
