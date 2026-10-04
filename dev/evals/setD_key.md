# Ad-Planning Exam — Set D Grading Key (D1–D6)

Score each checkpoint as Pass (1), Partial (0.5) or Fail (0). Checkpoints marked **[TRAP]** test whether the tool spots something wrong in the brief; failing a trap is a red flag regardless of total. Total: 59 points (D1 10, D2 10, D3 9, D4 10, D5 10, D6 10).

---

## D1 — FreshCrate quick-commerce (INR)

1. **[TRAP]** Contribution maths. Per order: 14% × 520 = ₹72.8, minus ₹50 delivery and picking = ₹22.8. First order with ₹150 discount = about -₹127. Over 12 months 7.5 × 22.8 = ₹171, minus ₹150 discount = about ₹21 per customer before ad cost. Breakeven CAC is about ₹21, so "₹60 CAC" loses about ₹39 per customer at best.
2. **[TRAP]** Re-reads history. ₹38 CPI with 21% ordering = about ₹181 per ordering customer, which is about 9x breakeven. 34% non-serviceable installs are waste. At about ₹181, ₹12L buys about 6,600 customers, not 20,000.
3. Honest outcome. Names what must change (discount size, basket-building, min order, repeat flow) and recommends a smaller pilot with low confidence rather than promising the target.
4. **[TRAP]** Refuses "10 minutes, guaranteed". Only 22% arrive in 10 minutes and the median is 17. It is a misleading claim (ASCI/consumer law); uses a true claim ("median 17 minutes", "under 15 for most orders") or sets the claim per store.
5. Geo. Pincode or store-radius targeting around the 9 stores (3 km hard), exclusion of non-serviceable areas, store-weighted budget. Hyderabad stays out until stores are live (pre-launch waitlist at most).
6. Tracking. Send first-order and repeat-order events from the app to Meta/Google (app events or CAPI), optimise for first order, not installs. Pincode on events.
7. Resolves the stakeholder conflict. Agreed metric is contribution per new customer (or cost per repeat customer), with marketing, finance and ops sign-off. Records who decides.
8. Operations. Dayparting ads away from 7–9 pm stockouts; pause ads around a store when stock or rider capacity is short.
9. Channel split with reasoning (Google App campaigns for intent, Meta for local reach and retargeting of non-orderers, CRM/push for the second order). Notes competitors' ₹100–200 offers and CPC ₹14–22.
10. Test plan. 4 weeks in 2–3 stores; kill/scale on cost per first order and 30-day repeat rate; scale only when CAC is under about ₹25-60 with a retention path.

---

## D2 — Gulf Motors Select used cars (AED)

1. **[TRAP]** Economics. Enquiry to sale is 20% × 18% = 3.6%. Gross profit per car is about AED 3,452 (3,200 + 28% × 900), or about AED 3,052 after sales commission. Value per enquiry is about AED 124 (about 110 net). 400 enquiries at AED 100 gives 14.4 sales, about AED 44–50k profit on AED 40k spend, roughly break-even before overhead. Allowable cost per enquiry is about AED 40–50. Recommends measuring cost per sale.
2. **[TRAP]** Re-reads history. Portals: AED 2,000 per sale. Meta: AED 2,800 per sale, with 38% unreachable. Both are near gross profit, so volume at AED 100 is no win.
3. **[TRAP]** Stale feed. Sold cars are advertised (38%), a bait-and-switch risk. Fix the feed (auto-remove sold stock) before any dynamic or inventory ads.
4. **[TRAP]** Refuses "accident-free, certified" blanket claim. Only claims backed per car by the report; discloses finance terms (20% down, rate, balloon) with "from AED 899/month".
5. Tracking. Call tracking per showroom, WhatsApp click events, UTM, lead source made mandatory in the dealer system, and sale/visit stages uploaded as offline conversions.
6. Platform split with reasoning. Google Search/vehicle listing for model-level intent, portal listings kept for high-intent, Meta for finance-led and showroom-visit offers; budget guided by cost per showroom visit.
7. Geo. Showroom radius (60 km hard), budget weighted by stock and capacity, and Ajman checked for overlap with Sharjah. Oman/Saudi export buyers only after export documentation is confirmed.
8. Lead handling. Speed-to-lead (5 minutes), WhatsApp automation, showroom visit booking, 38% unreachable leads fixed with verification.
9. Stakeholder and unit clarity. Defines "enquiry" (qualified, reachable) and gets sales and marketing to agree on cost per visit or sale.
10. Test plan. 4 weeks at 2 showrooms; scale on cost per sale under about AED 1,500–1,800.

---

## D3 — HiveSG coworking (SGD)

1. **[TRAP]** Rejects "fill 300 desks": only 243 are vacant (640 × 38% = 243, with 397 occupied). A realistic target is 100–150 desks over 3 months with low confidence, weighted to Tai Seng and Jurong.
2. **[TRAP]** Margin and mix. Contribution per desk-month: hot S$220, dedicated S$460, private office about S$390 per desk. Lifetime contribution: hot about S$1,540, dedicated S$6,440, office about S$31,200 per office. Pushes dedicated desks and private offices, not hot-desk volume. Notes the unit ambiguity (an office is 4 desks).
3. **[TRAP]** Refuses "Singapore's #1" (no source) and the "30% cheaper than WeWork" comparison, which is hot desk vs dedicated desk. A fair comparison uses like-for-like plans, or none at all (ASAS code).
4. **[TRAP]** Refuses cold WhatsApp/SMS to the scraped list. PDPA and DNC registry rules apply; uses opt-in, or LinkedIn/Google targeting and compliant outreach.
5. Tracking. Tag the tour scheduler, use WhatsApp click events, push signup value from Stripe to Google and Meta as offline conversions, and record plan type.
6. Resolves founder/ops conflict. Raffles Place at 85% needs little paid support (waitlist and premium private offices only). Budget leans on Tai Seng (100 vacant) and Jurong (112 vacant), with a decision recorded.
7. Economics check. Cost per tour about S$100 and per signup about S$400. Allowable is higher for dedicated desks/offices (LTV much higher) and tighter for hot desks (about S$1,540 LTV).
8. Platform split. Google Search by location and plan ("private office Tai Seng"), Meta/LinkedIn for SMEs and team leads, retargeting; calendar for Jan budget season.
9. Test plan. 6 weeks; judge on tours, signups and plan mix; scale when cost per dedicated/office signup is acceptable.

---

## D4 — Paws & Co vet and e-store (AUD)

1. **[TRAP]** Corrects the ROAS. Duplicate purchase events inflate revenue by about 35%, so the real ROAS is about 4.5x (6.1 ÷ 1.35). Fix the tag before judging.
2. **[TRAP]** Margin maths. Contribution per order is 68 × 0.32 − 6 = about A$15.8 (23%), so breakeven ROAS is about 4.3x. 8x on all revenue is not realistic. At 30% off, price A$47.6 is below cost (cost about A$46.2, minus A$6 shipping) and loses about A$4.6 per order. Advise a smaller discount or non-food items/bundles only.
3. **[TRAP]** Refuses "cures arthritis" and "vet-recommended" without substantiation (ACL, state vet board and supplement regulations; check APVMA/board rules and testimonials). Compliant wording is "supports joint health" with evidence.
4. **[TRAP]** Privacy. The booking confirmation URL carries name and email, so the pixel must not fire on it. Use clean URLs or hashed conversions with consent. Clinic remarketing uses non-personal pages only.
5. Revenue goal. A$38k to A$100k is a 2.6x jump; not achievable on A$9k budget. States realistic growth and what ROAS the budget supports.
6. Clinic economics. New patient value A$520 × 45% = A$234; allowable CAC is about A$78; history A$65 per patient is good, so protect it with brand and "vet near me" search.
7. Geo. Clinics at 20 km (hard). The store ships nationally, but WA/NT/remote orders at A$18 shipping lose money, so exclude them or set a minimum.
8. Budget split. Reasoned, with a split of about 55% clinics and 45% store, since both managers have a claim. Records the decision owner.
9. Competitors. Defends "Paws & Co" brand terms against bidders; autoship/subscription offers to raise repeat purchases.
10. Test plan. 4–6 weeks after the tag fix; kill/scale on true ROAS and cost per new patient.

---

## D5 — Lingomart tutor marketplace (USD)

1. **[TRAP]** Unit economics. Net take per pack is 25% × 110 − 3% × 110 = US$24.2. Per buyer (3.1 packs) is about US$75. Per trial student: 38% × 75 − US$4 trial loss = about US$24.5. Allowable cost per trial booked is about US$8 (3:1). Goal: 10,000 signups × 14% = 1,400 trials, so US$30k means about US$21 per trial, about 2.7x over. Honest outcome: far fewer trials or a lower target.
2. **[TRAP]** Changes the target. Signups are a vanity metric. Optimise for trial booked and pack purchased. CFO and CMO agree on net take per ad dollar.
3. **[TRAP]** Refuses "Fluent in 30 days — guaranteed" (unsubstantiated outcome claim) and "50,000+ learners" (31,000 registered; 9,800 active). Uses accurate figures such as "31,000 learners".
4. **[TRAP]** Refuses teen targeting (13–17). Meta and TikTok restrict ads to minors; under-16 accounts are parent-managed, so ads target parents (18+) for kids' lessons.
5. Supply match. Do not buy Japanese/Korean demand with 9 and 7 tutors (31% unmatched); cap spend or recruit tutors first. Prioritise languages with deep supply.
6. Tracking. Trial-booked and pack-paid events from web and apps (SDK/MMP), Stripe to ad platforms, and iOS measurement limits acknowledged. Primary event is a trial booked.
7. Geo. US, UK, CA, AU, DE hard with local-currency pricing and local language ads. Brazil/India small soft tests at lower prices with margin check. Russia excluded (sanctions, payments).
8. Trial economics. The US$4 loss per trial; reconsider trial price (for example US$7–9) or limit trials per user.
9. Channels. Google Search on "learn [language] online", YouTube/Meta for lookalikes of pack buyers, referral and brand search defence against large apps.
10. Test plan. 4 weeks by language and market; kill/scale on cost per trial under about US$8–10.

---

## D6 — Frames & Vows wedding photography (INR)

1. **[TRAP]** Capacity vs goal. There are 26 open team-dates (two teams) before Feb 2027, so 60 bookings are impossible for this season. Splits the goal: fill the 26 dates, then early-book the 2027–28 season. Needs a realistic target.
2. **[TRAP]** Unit ambiguity. A "booking" must be defined: ₹10k token or confirmed. 28% of tokens are cancelled, so 60 tokens are about 43 confirmed. Re-reads history: 190 chats, 8 tokens (4.2%) at ₹7,500 per token, about ₹10,400 per confirmed booking, against gross profit of ₹1.0L per wedding. Economics are healthy, so the constraint is capacity.
3. **[TRAP]** Refuses "1,000+ weddings" (412), "5.0 rating" (4.6 from 38) and "Official photographer of Aravali Palace" (shot one wedding; implies endorsement and trademark use). Uses true figures.
4. **[TRAP]** Consent for images. 40% of old contracts lack usage rights; guests' faces too (privacy under DPDP). Uses only images with written releases, and updates future contracts.
5. Tracking. The owner's personal WhatsApp is the only inbox. Sets up a business WhatsApp number or API, logs chats in a sheet/CRM with UTM/source, and uploads token and confirmed events as offline conversions.
6. Seasonality. Current-season dates are mostly gone; the plan promotes remaining dates and weekday or smaller packages, and early-bird 2027–28 offers. Scales spend down for peak months when the team is fully booked.
7. Stakeholder conflict. Photography gross profit about ₹1.0L vs venue commission about ₹48k. The plan sets a split (for example 70/30) and gets the owner and sibling to agree. Venue leads are accepted only when dates fit.
8. Geo. Jaipur and Udaipur (hard). Delhi NCR as soft with the ₹45k travel fee shown. Budget weighted to Jaipur, where teams are based.
9. Channels. Instagram Reels and click-to-WhatsApp as the core with Google Search on "wedding photographer Jaipur" at CPC ₹40–90 for high intent; reviews and Google Business Profile built honestly.
10. Test plan. 4 weeks; kill/scale on cost per confirmed booking and response time to WhatsApp (under 15 minutes).
