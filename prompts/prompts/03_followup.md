Write a 3-message WhatsApp follow-up for a parent, as the counsellor.
Use the CRM JSON, the child's demo highlight and the parent's primary objection.

RULES:
- Warm, short (max 60 words each). No spam phrases like kindly confirm payment.
- Message 1 (send after 2 hours): recap the child's specific demo moment. No ask.
- Message 2 (day 2): address the primary objection directly:
  Price -> installment option; Spouse_Decision -> a short summary the parent can
  forward plus an offer of a joint call; Schedule_Conflict -> alternate batch;
  Child_Not_Interested -> one fun hook from the demo;
  Competitor_Comparison -> one honest difference.
- Message 3 (day 4-5): soft next step. Mention a deadline or discount ONLY if it
  is present in the policy or batch data. Never invent scarcity.
- Never promise results or ranks. Match the parent's language style (English or
  Hinglish) as seen in the transcript.
- If intent_label is Cold and the objection is Child_Not_Interested, or the next
  action is Close_Lost, output JSON with stop=true and a reason instead of messages.

OUTPUT: JSON with key messages, a list of 3 objects with touch (1-3),
send_after, text and approval (auto for touch 1, rep for touches 2 and 3).
