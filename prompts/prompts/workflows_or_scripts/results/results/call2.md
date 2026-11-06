# Call 2: Zoya / Amina (Counsellor: Sneha, Dubai)

## 1. Call Audit

```json
{
  "scores": {
    "rapport_child_praise": {"score": 1, "evidence": "How did you find the class?"},
    "diagnosing_pain": {"score": 0, "evidence": "Which package would you like to enroll Zoya in today?"},
    "curriculum_pitch": {"score": 1, "evidence": "Yes ma'am, don't worry, our curriculum covers fractions, decimals, geometry, and word problems also."},
    "price_framing": {"score": 1, "evidence": "For the 6-month package of 48 classes it is AED 1,200"},
    "objection_handling": {"score": 1, "evidence": "Building tuition is just old-fashioned rote learning where many kids sit together."},
    "urgency_trial_close": {"score": 0, "evidence": "the discount link expires in 30 minutes because batch seats fill very fast in Dubai."},
    "compliance_professionalism": {"score": 0, "evidence": "please click and pay in 30 minutes."}
  },
  "total_100": 18.3,
  "compliance_flags": [
    {
      "type": "price_quoted_before_value_explained (policy 205: no price dump before Bar-Model vs rote tuition explanation)",
      "severity": "hard",
      "quote": "So let me quickly tell you our fee structure for Dubai students. For the 6-month package of 48 classes it is AED 1,200"
    },
    {
      "type": "fake_scarcity_and_invented_deadline",
      "severity": "hard",
      "quote": "the discount link expires in 30 minutes because batch seats fill very fast in Dubai."
    },
    {
      "type": "pressuring_tone",
      "severity": "hard",
      "quote": "if you complete the payment right now on this call, I can generate a special AED 100 instant discount link"
    },
    {
      "type": "price_not_in_policy_(12-month_package)",
      "severity": "medium",
      "quote": "for the 12-month package of 96 classes it is AED 2,100."
    },
    {
      "type": "unverified_product_claims",
      "severity": "medium",
      "quote": "Bambinos is a global company featured on Shark Tank India and we have top 1% certified teachers."
    },
    {
      "type": "disparaging_competitor_and_misrepresenting_parents_tutor",
      "severity": "medium",
      "quote": "Building tuition is just old-fashioned rote learning where many kids sit together."
    },
    {
      "type": "unverified_claim_about_demo_session",
      "severity": "medium",
      "quote": "Uh, let me check... yes, the teacher gave her some puzzles and she did well."
    }
  ],
  "coaching": {
    "win": "Sneha, you opened by asking how the class went, and the Zing quizzes and monthly parent reports you mentioned are relevant to a parent who wants to track progress.",
    "fix": "Amina told you her real worry (word-problem panic in exams) and compared you to a local tutor, but fees and a discount came before any diagnosis. Next time, quote the price only after explaining how visual Bar-Model problem solving differs from worksheet tuition, and check with the teacher before answering what happened in the demo.",
    "better_line": "Thank you for sharing that, ma'am. Word problems are exactly where visual Bar-Model thinking helps, so let me check with Mr. Vikram how Zoya approached them today and call you back with specifics before we talk about fees."
  }
}
```

## 2. Cleaned CRM Record

```json
{
  "intent_label": "Warm",
  "intent_score": 4,
  "primary_objection": "Competitor_Comparison",
  "secondary_objection": "Price",
  "objection_evidence": "Right here in our building in Karama, a retired school teacher takes offline maths tuition 3 days a week for AED 350",
  "child_demo_highlight": "Enjoyed the interactive on-screen puzzles, which she told her mother felt like a game rather than a boring class (parent-reported).",
  "learning_gap": "Zoya gets full marks on straight number questions like 45 x 18, but panics, guesses the wrong operation or leaves 4-line story problems (fractions, ratios) blank in her British curriculum exams.",
  "next_best_action": "Escalate_To_Manager",
  "follow_up_by": null,
  "confidence": "Medium",
  "cleaned_note": "Parent was unconvinced after the counsellor quoted AED 1,200 and pushed a pay-now AED 100 discount without answering her word-problem concern, and asked for curriculum details on WhatsApp so she can discuss it with her local tutor."
}
```

## 3. Routing Status (guardrail result)

- Status: HELD. Hard compliance flags detected (3). Manager alerted.
- All WhatsApp messages below are blocked until a manager reviews the call and approves them.
- Touch 1 auto-send is disabled for this lead because of the hard flags.

## 4. WhatsApp Sequence (draft, held for manager approval)

```json
{
  "stop": false,
  "status": "held_for_manager_review",
  "messages": [
    {
      "touch": 1,
      "send_after": "2 hours",
      "text": "Hi Amina ma'am, Sneha from Bambinos.live 😊 Thank you for your time today. I loved hearing that Zoya felt the puzzles were more like a game than a boring class. I'm checking with Mr. Vikram on how she approached the problems and will share his notes with you.",
      "approval": "manager"
    },
    {
      "touch": 2,
      "send_after": "Day 2",
      "text": "Hi ma'am, I'm sorry I rushed you on our call. Your concern is Zoya's word problems in her exams, not just the fee, and that's the right thing to ask. Our Brainiac track uses visual Bar-Model problem solving, which is different from worksheet practice. I'll share Mr. Vikram's notes so you can compare calmly.",
      "approval": "manager"
    },
    {
      "touch": 3,
      "send_after": "Day 4-5",
      "text": "Hi ma'am, hope the details were helpful. No pressure at all. If you decide to go ahead, the fee can be paid 50% now and 50% at Day 30, and the 14-day refund applies (up to 4 classes attended). Happy to answer any questions you or Zoya's tutor may have.",
      "approval": "manager"
    }
  ]
}
```

## 5. Review Notes
- Score: 55/3 = 18.3. Hard-flag cap of 50 does not change it.
- Needs manager decision: whether pay-now discounts with an expiry are allowed at all (the policy does not support them).
- Needs verification: the Shark Tank India and top 1% teacher claims, the 12-month AED 2,100 package, and what actually happened in the demo (confirm with Mr. Vikram).
- The AED 100 discount is within the 10% cap (max AED 120). The flags are for the pay-now condition and the 30-minute expiry.
- Touch 3 payment plan and refund wording come from the policy; confirm they apply to this course.
- Rep coaching should be framed supportively: one win, one fix, one better line.
