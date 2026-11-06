# Call 4: Meera / Neha (Counsellor: Rohan, US West Coast)

## 1. Call Audit

```json
{
  "scores": {
    "rapport_child_praise": {"score": 3, "evidence": "Meera's question—'Why did Arjuna feel overwhelmed before the event even started?'—was the most thoughtful question of the week."},
    "diagnosing_pain": {"score": 2, "evidence": "How did Meera feel after the class ended?"},
    "curriculum_pitch": {"score": 3, "evidence": "we teach the 8 Gunas—focus, resilience, gratitude, emotional regulation—through interactive stories and reflection, never dry rote memorization."},
    "price_framing": {"score": 2, "evidence": "Yes, USD 265 all-inclusive for 48 live classes, digital storybooks, and parent reflection guides"},
    "objection_handling": {"score": 3, "evidence": "Acharya Aditi leads a dedicated US West Coast batch on Saturdays and Sundays at 9:30 AM PST."},
    "urgency_trial_close": {"score": 2, "evidence": "Just sent it on your WhatsApp, Neha! Welcome to the Bambinos family in advance"},
    "compliance_professionalism": {"score": 2, "evidence": "backed by our 14-day 100% refund policy."}
  },
  "total_100": 81.7,
  "compliance_flags": [
    {
      "type": "refund_terms_incomplete_vs_policy (omits the 4-class limit and pro-rata refund after 14 days)",
      "severity": "medium",
      "quote": "backed by our 14-day 100% refund policy."
    }
  ],
  "coaching": {
    "win": "Rohan, you solved the Tuesday/Thursday gymnastics clash on the spot by checking the roster and finding Acharya Aditi's weekend batch, and you tied the 8 Gunas to what Meera did in class. Neha said it was 'literally perfect'.",
    "fix": "State the refund terms in full when you mention them, including the 4-class limit and the pro-rata refund after 14 days. Also close the loop on the call: agree a time to confirm the payment and the batch, and update the CRM stage once she pays.",
    "better_line": "The USD 265 covers all 48 live classes, and our refund is 100% within the first 14 days (up to 4 classes attended), then pro-rata. I'll check in after your meeting to confirm the Saturday-Sunday 9:30 AM batch is locked in."
  }
}
```

## 2. Cleaned CRM Record

```json
{
  "intent_label": "Hot",
  "intent_score": 10,
  "primary_objection": "Schedule_Conflict",
  "secondary_objection": null,
  "objection_evidence": "Meera has her competitive gymnastics team practice every Tuesday and Thursday from 4:30 PM to 6:30 PM PST",
  "child_demo_highlight": "Wrote down the meaning of the 'Samatvam' shloka in her personal diary after Acharya Aditi linked it to her gymnastics balance-beam routine (parent-reported).",
  "learning_gap": "Meera rolls her eyes when her parents share Indian mythological stories or values at home and treats it as a parent lecture.",
  "next_best_action": "Onboard_Paid",
  "crm_stage_fix": "Change stage from Payment_Link_Sent to Enrolled_Paid after verifying the payment (Order #99404) in the payment system.",
  "follow_up_by": "11:30 AM PST on the call day (parent's stated payment time)",
  "confidence": "High",
  "cleaned_note": "Mother was ready to enrol Meera in Little Yogi, the weekday gymnastics clash was solved with the Sat-Sun 9:30 AM PST batch, and a payment of USD 265 is recorded while the CRM stage still shows Payment_Link_Sent."
}
```

## 3. Routing Status (guardrail result)

- Status: PASSED with 1 medium flag. No hard flags, so no manager hold.
- Payment status came from a note inside the call data, not from the payment system. It must be verified in Stripe before the stage is changed.
- Rep coaching digest sent: 1 win, 1 fix, 1 better line.

## 4. WhatsApp Sequence (adapted for a paid lead: reassurance, no payment ask)

```json
{
  "stop": false,
  "messages": [
    {
      "touch": 1,
      "send_after": "2 hours",
      "text": "Hi Neha, Rohan here from Bambinos.live 😊 I keep thinking about Meera writing the meaning of the 'Samatvam' shloka in her diary after Acharya Aditi linked it to her balance-beam routine. Acharya Aditi also called her question about Arjuna the most thoughtful of the week!",
      "approval": "auto"
    },
    {
      "touch": 2,
      "send_after": "Day 2",
      "text": "Hi Neha, a quick note on timing. Meera's batch with Acharya Aditi is Saturdays and Sundays at 9:30 AM PST, so it stays clear of her Tuesday and Thursday gymnastics practice. If anything about the schedule needs a second look, just message me and I'll sort it out.",
      "approval": "rep"
    },
    {
      "touch": 3,
      "send_after": "Day 4-5",
      "text": "Hi Neha, hope Meera is looking forward to her weekend classes! One small clarification from our call: our 100% refund covers the first 14 days (up to 4 classes attended), with a pro-rata refund after that. Happy to help with anything else.",
      "approval": "rep"
    }
  ]
}
```

## 5. Review Notes
- Verify Order #99404 in the payment system before moving the CRM stage to Enrolled_Paid.
- Taxonomy change: added next_best_action value Onboard_Paid for leads who have already paid.
- Check against the policy and roster: the digital storybooks and parent guides, the Sat-Sun 9:30 AM PST batch, and the 4-kids-enrolled claim.
- No fake scarcity, no unauthorised discount, no guarantees. Refund statement incomplete (medium).
- Score: 245/3 = 81.7. No hard flag, so no cap.
