# Call 6: Ananya / Swathi (Counsellor: Karan, Chess)

## 1. Call Audit

```json
{
  "scores": {
    "rapport_child_praise": {"score": 1, "evidence": "Ananya did fantastic in the demo class! She is a natural Grandmaster!"},
    "diagnosing_pain": {"score": 0, "evidence": "Discovery Question 2—What is Ananya's biggest weakness?"},
    "curriculum_pitch": {"score": 0, "evidence": "Chess improves IQ, memory, concentration, and maths scores by 40%!"},
    "price_framing": {"score": 1, "evidence": "Let us lock her seat in the 6-month Unbox Chess Beginners batch for Rs. 11,000 today!"},
    "objection_handling": {"score": 0, "evidence": "Ma'am kids always make excuses!"},
    "urgency_trial_close": {"score": 0, "evidence": "I am also offering our official 10% discount so it is Rs. 9,900 if you pay before 6 PM today"},
    "compliance_professionalism": {"score": 0, "evidence": "that covers my urgency trial close!"}
  },
  "total_100": 6.7,
  "compliance_flags": [
    {
      "type": "false_product_claim_and_guaranteed_outcome (40% maths score improvement is not in policy)",
      "severity": "hard",
      "quote": "Chess improves IQ, memory, concentration, and maths scores by 40%!"
    },
    {
      "type": "policy_violation_pushed_standard_6_kid_batch_on_overwhelmed_5_6_year_old (policy 401 requires a 1-on-1 bridge session or Age 5-6 Micro-Batch) and false statement that no other batch exists",
      "severity": "hard",
      "quote": "Ma'am all batches are standard 6 kids, just pay Rs. 9,900 on the link and Ops team will see later."
    },
    {
      "type": "fake_deadline_and_pressure_tactic (no payment deadline exists in policy)",
      "severity": "hard",
      "quote": "I am also offering our official 10% discount so it is Rs. 9,900 if you pay before 6 PM today"
    },
    {
      "type": "pressuring_and_dismissive_tone_toward_parent_and_child",
      "severity": "medium",
      "quote": "Ma'am kids always make excuses! Once you pay Rs. 11,000 and force her to sit in the 6-kid batch for 3 weeks, she will automatically adjust."
    },
    {
      "type": "false_child_praise_contradicted_by_parent",
      "severity": "medium",
      "quote": "Ananya did fantastic in the demo class! She is a natural Grandmaster!"
    },
    {
      "type": "refund_terms_incomplete_vs_policy (omits the 4-class limit and the pro-rata refund after 14 days)",
      "severity": "medium",
      "quote": "Also please note our official 14-day 100% refund policy and 6-kids batch structure!"
    },
    {
      "type": "unprofessional_scripted_delivery_ignoring_parent",
      "severity": "medium",
      "quote": "Let me quickly complete my mandatory call checklist: Discovery Question 1—What is your primary goal for Ananya?"
    }
  ],
  "coaching": {
    "win": "Karan, you quoted the correct fee of Rs. 11,000 for Unbox Chess Beginners, and the 10% discount (Rs. 9,900) stays within the policy cap, so your pricing knowledge is a solid base to build on.",
    "fix": "Swathi told you clearly that Ananya felt overwhelmed by older kids, and the policy gives you a ready answer: a complimentary 1-on-1 bridge session or an Age 5-6 Micro-Batch (max 3 kids). Next time, pause, listen to the parent's concern, and offer that option or escalate to the academic team instead of pushing payment. Please also avoid outcome claims like '40%' and deadlines that are not in the policy.",
    "better_line": "Thank you for telling me that, ma'am, and I'm sorry Ananya felt overwhelmed. Coach Arvind's suggestion is right: for a 6-year-old we can arrange a complimentary 1-on-1 bridge session or an age 5-6 micro-batch. Let me confirm that with our academic team before you decide anything."
  }
}
```

## 2. Cleaned CRM Record
(Add from the CRM output. Expected: next_best_action = Escalate_To_Manager, primary objection = Child_Not_Interested or Schedule/fit-related depending on the transcript.)

## 3. Routing Status (guardrail result)
- Status: ESCALATED. 3 hard compliance flags. Manager alerted.
- No automated parent messages are sent. The academic team contacts the parent to offer the 1-on-1 bridge session or Age 5-6 Micro-Batch.
- Counsellor receives a coaching digest. The call is added to the manager review queue.

## 4. WhatsApp Sequence
(Add from the WhatsApp output. It must be held for manager approval and must not repeat the 40% claim, the 6 PM deadline or the 6-kid-only statement.)

## 5. Review Notes
- Score: 20/3 = 6.7. Hard-flag cap of 50 does not change it.
- Verify against the policy CSV: policy 401 (bridge session and micro-batch), the 10% discount cap, and the refund terms.
- The counsellor's pricing (Rs. 11,000, 10% off = Rs. 9,900) is correct. The failure is in diagnosis, claims and pressure, not the numbers.
