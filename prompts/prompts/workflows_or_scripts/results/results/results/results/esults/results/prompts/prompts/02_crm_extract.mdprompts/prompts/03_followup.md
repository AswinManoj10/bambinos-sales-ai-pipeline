Write a 3-message WhatsApp follow-up for a parent, as the counsellor.
Use the CRM JSON, the child's demo highlight and the parent's primary objection.

RULES:
- Warm, short (max 60 words each). No spam phrases like kindly confirm payment.
- Touch 1 (after 2 hours): recap the child's specific demo moment. No ask.
  approval: auto
- Touch 2 (day 2): address the primary objection directly:
  Price -> installment option; Spouse_Decision -> a short summary the parent can
  forward plus an offer of a joint call; Schedule_Conflict -> alternate batch;
  Child_Not_Interested -> one fun hook from the demo;
  Competitor_Comparison -> one honest difference. approval: rep
- Touch 3 (day 4-5): soft next step. Mention a deadline or discount ONLY if it is
  in the policy. Never invent scarcity. approval: rep
- If any hard compliance flag exists, every message needs approval: manager.
- If the call contained false promises, correct them gently using the official
  policy terms. Never repeat them.
- Use only facts from the transcript or policy. Never promise results.
- Match the parent's language style (English or Hinglish).
- If the lead is Cold or Close_Lost, output stop=true with a reason instead.

OUTPUT: JSON with key messages, a list of 3 objects with touch (1-3),
send_after, text and approval. Use straight quotes only.
