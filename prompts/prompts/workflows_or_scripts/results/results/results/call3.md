# Call 3: Vihaan / Kiran (Counsellor: Amitabh)

## 1. Call Audit

```json
{
  "scores": {
    "rapport_child_praise": {"score": 0, "evidence": "Congratulations sir! Vihaan has been shortlisted for our super-exclusive Elite Phonics Accelerator batch!"},
    "diagnosing_pain": {"score": 0, "evidence": "Sir, forget about screen time and forget about 'train' or 'truck'! That is nothing!"},
    "curriculum_pitch": {"score": 0, "evidence": "not observed: no curriculum explanation; the counsellor spoke about company awards instead"},
    "price_framing": {"score": 0, "evidence": "flat Rs. 4,000 off! And I will even make it a 1-on-1 private class for the price of a group batch!"},
    "objection_handling": {"score": 0, "evidence": "Sir, forget about screen time and forget about 'train' or 'truck'! That is nothing!"},
    "urgency_trial_close": {"score": 0, "evidence": "you must do the UPI payment in the next 5 minutes while staying on this call"},
    "compliance_professionalism": {"score": 0, "evidence": "our system will permanently blacklist Vihaan's student ID forever!"}
  },
  "total_100": 0,
  "compliance_flags": [
    {"type": "guaranteed_outcome_exam_rank_and_reading_level", "severity": "hard", "quote": "in just 30 days Vihaan will read thick 300-page Harry Potter novels by himself and he will come Rank 1 in his school English exam!"},
    {"type": "false_refund_promise_contradicting_policy", "severity": "hard", "quote": "I am giving you a 100% no-questions-asked full refund anytime in 6 months! Even if Vihaan attends all 48 classes"},
    {"type": "discount_beyond_policy_limit_without_approval_code", "severity": "hard", "quote": "flat Rs. 4,000 off!"},
    {"type": "misquoted_price_in_payment_link_vs_policy (said by parent)", "severity": "hard", "quote": "why is the link you just sent me on WhatsApp showing Rs. 5,500 when you said the fee is Rs. 9,500?"},
    {"type": "false_product_claim_1_on_1_for_group_price", "severity": "hard", "quote": "I will even make it a 1-on-1 private class for the price of a group batch!"},
    {"type": "threat_of_blacklisting_child_and_5_minute_pressure", "severity": "hard", "quote": "you must do the UPI payment in the next 5 minutes while staying on this call, otherwise our system will permanently blacklist Vihaan's student ID forever!"},
    {"type": "fake_scarcity_false_exclusivity", "severity": "medium", "quote": "Vihaan has been shortlisted for our super-exclusive Elite Phonics Accelerator batch!"},
    {"type": "unverified_company_claims", "severity": "medium", "quote": "we are backed by Shark Tank India, we have taught 50,000+ kids across 25 countries"},
    {"type": "dismissive_tone_and_advising_to_bypass_policy", "severity": "medium", "quote": "Sir, between you and me, off the record, don't look at the website policy"},
    {"type": "unauthorised_claim_of_hacking_manager_quota", "severity": "medium", "quote": "Because I hacked my manager's VIP scholarship quota just for you, sir—flat Rs. 4,000 off!"}
  ],
  "coaching": {
    "win": "Amitabh, you quoted the correct standard fee of Rs. 9,500 for Phonics & Early Reading Champions, which matches the policy, and that is a solid base to build on.",
    "fix": "Kiran gave you two clear concerns (screen time and Vihaan reading 'train' as 'truck'), but they were dismissed and replaced with guarantees and pressure. Next time, listen to each doubt, answer it honestly with what the demo showed, and keep to the official refund and discount terms.",
    "better_line": "Those are fair doubts, sir. At 7, 'train' and 'truck' mix-ups are common while blending is still developing, and Ms. Simran's live practice is designed to build it step by step. Can I share what she noted today, and explain how our 14-day refund works?"
  }
}
```

## 2. Routing Status (guardrail result)

- Status: ESCALATED. 6 hard compliance flags detected. Manager alerted immediately.
- Score is 0/100 and capped by the hard-flag rule.
- No automated parent messages are sent. A manager contacts the parent to correct the false refund, discount and guarantee claims.
- Recommended manager actions: review the recording, correct the record with the parent in writing, and coach the counsellor.

## 3. Cleaned CRM Record
(Add from the CRM prompt output.)

## 4. WhatsApp Sequence
(Add from the WhatsApp prompt output, held for manager approval.)

## 5. Review Notes
- This is the strongest example of the guardrails working: multiple hard flags, score 0, escalation and a message hold.
- Verify the refund terms and discount cap against the policy CSV before quoting them to the parent.
