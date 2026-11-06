# Call 5: Kabir (Counsellor: Pooja, Hinglish call)

## 1. Call Audit

```json
{
  "scores": {
    "rapport_child_praise": {"score": 3, "evidence": "Kabir ne 'Should homework be banned?' topic par poore 60 seconds bina ek bhi 'umm' bole speech di!"},
    "diagnosing_pain": {"score": 2, "evidence": "Kabir ki grammar strong hai, bas spoken fluency mein woh mental translation ki wajah se rukta hai."},
    "curriculum_pitch": {"score": 2, "evidence": "Isiliye Bambinos mein hum strictly 6-kids small group rakhte hain jahan har bache ko peer audience milti hai"},
    "price_framing": {"score": 2, "evidence": "Rs. 12,000 ki jagah Rs. 10,800 ho jayegi."},
    "objection_handling": {"score": 3, "evidence": "public speaking aur debate akele 1-on-1 kamre mein nahi aati sir, kyunki stage fear tabhi jaata hai"},
    "urgency_trial_close": {"score": 2, "evidence": "aaj sirf 50% yaani Rs. 5,400 dekar Kabir ki Ms. Rhea ke batch mein seat lock kar lijiye"},
    "compliance_professionalism": {"score": 2, "evidence": "Hamari official policy ke andar main aapko 10% scholar discount de sakti hoon"}
  },
  "total_100": 76.7,
  "compliance_flags": [
    {
      "type": "unverified_competitor_price_claim (not in policy)",
      "severity": "medium",
      "quote": "price bhi 1-on-1 se almost half padta hai"
    },
    {
      "type": "unverified_product_feature_claim (Exam Pause / Reschedule button not in policy)",
      "severity": "medium",
      "quote": "exam week mein hamare portal par 'Exam Pause / Reschedule' button hota hai, jisse aapki ek bhi paid class waste nahi hoti."
    }
  ],
  "coaching": {
    "win": "Pooja, you listened well and used Kabir's own 60-second PEEL speech to answer the parent's real worry about spoken English. You also handled the PlanetSpark comparison with a clear peer-audience reason. The 10% discount (Rs. 10,800) and the 50% + 50% at Day 30 plan (Rs. 5,400 each) both match the policy.",
    "fix": "Replace claims the policy does not support, like the 'almost half' price comparison and the Exam Pause button, with confirmed facts. Also state the refund terms, since the parent never heard them.",
    "better_line": "Sir, exam ke time class kaise reschedule hoti hai, woh main confirm karke aapko WhatsApp par bhej dungi. Aur ek baat clear kar doon: pehle 14 din mein (4 classes tak) 100% refund hai, uske baad pro-rata."
  }
}
```

## 2. Cleaned CRM Record
(Add from the CRM output.)

## 3. Routing Status (guardrail result)
- Status: PASSED with 2 medium flags. No hard flags, so no manager hold.
- Medium flags go to the manager's weekly review, and the rep gets the coaching digest.

## 4. WhatsApp Sequence
(Add from the WhatsApp output. Write it in Hinglish to match the parent.)

## 5. Review Notes
- Score: 230/3 = 76.7. No hard flag, so no cap.
- Verify against the policy CSV: the 10% scholar discount (and whether it needs an approval code), the 50% + 50% at Day 30 plan, and the refund terms.
- Verify the Exam Pause / Reschedule feature exists before any message mentions it.
- The refund terms were never stated to the parent, so a follow-up message should add them.
