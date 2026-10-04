# Ad-Planning Exam — Set A Scenarios (A1–A6)

All businesses, URLs and figures are fictional. Give the tool only the text of one scenario at a time.

---

## A1 — "Shaant" meditation & sleep app (installs + in-app subscription)

**Intake.** Website: shaantapp.in (app landing page; Android + iOS). Stated goal: "Maximum installs, then subscriptions." Budget: ₹2,50,000/month for Meta + Google combined. Locations: India (hard), with "test the UK diaspora" as a soft ask. Socials: Instagram 41k (mostly guided-breathing Reels), YouTube 9k. Enquiries: none; in-app chat support only.

**Business facts.** Freemium. Premium ₹1,499/year or £39.99/year in the UK; 7-day free trial. Trial-to-paid 18% India, 31% UK. Apple/Google take a 15% cut. 12-month LTV of a paid user: ₹1,150 India, £33 UK.

**Tracking.** Firebase SDK installed; AppsFlyer free tier added last month; `trial_start` and `purchase` events exist in Firebase but are not linked to Google Ads or Meta. No SKAN conversion-value schema set.

**Competitors.** Two Indian rivals run Meta Reels ads with "Struggling with anxiety? Fix your sleep tonight." Global apps bid on "meditation app" in Google.

**History.** Last quarter's Google App campaign (install-optimised) gave a ₹14 CPI, but 71% of installs came from Tier-3 Android users and 0.4% of installs started a trial.

**Client request.** "Target people with anxiety, depression and insomnia, and use the headline 'Are you depressed? Shaant can cure it.'"

---

## A2 — "Hearth & Loom" UK homewares e-commerce

**Intake.** Website: hearthandloom.co.uk (Shopify, 340 SKUs: throws, cushions, ceramics). Stated goal: "Grow online sales at a 4x ROAS." Budget: £9,000/month. Locations: UK only (hard); the client also ships to Ireland but doesn't want to advertise there yet. Socials: Instagram 22k, Pinterest active, Facebook dormant. Enquiries: email inbox, handled by the founder.

**Business facts.** AOV £72, gross margin 58%, free shipping above £60, 30% of customers reorder within 12 months. Q4 (Oct–Dec) brings 45% of annual revenue.

**Tracking.** GA4 + Google Ads tag through the Shopify Google & YouTube app. The cookie banner is a custom script that blocks everything until the visitor accepts. Consent Mode is not implemented. The Meta pixel is installed but there is no Conversions API. Merchant Center has 61 products disapproved for missing GTINs and 14 for "misrepresentation — unavailable promotion".

**Competitors.** Large retailers dominate Shopping for "wool throw" queries; small competitors win on Instagram with UGC Reels.

**History.** For six months a single Performance Max campaign showed a 7.8x ROAS in Google Ads. Brand search impressions rose over the same period while total Shopify revenue stayed flat. Meta ran boosted posts only.

---

## A3 — "CareBridge Staffing" nurse recruitment (USA)

**Intake.** Website: carebridgestaffing.com/careers. Stated goal: "200 qualified RN applications in 60 days for our Houston and Dallas partner hospitals." Budget: US$18,000 for the 60 days. Locations: Houston and Dallas metro areas (hard); also "travel nurses anywhere in Texas" (soft). Socials: Facebook 6k, LinkedIn 14k. Enquiries: two recruiters who phone-screen within 48 hours.

**Business facts.** The agency earns about $9,500 per placed RN. Historically 1 in 6 qualified applicants is placed. Applicants need an active Texas or compact RN licence and at least 1 year of acute-care experience.

**Tracking.** Applications run through an ATS (Bullhorn) on an external domain. The client can add a pixel only to the "thank you" page, and only for Meta. There is no GA4 cross-domain setup.

**Competitors.** Large job boards and hospital systems run Google Search on "RN jobs Houston" with CPCs of $4–9.

**History.** Previous Meta lead-form ads gave $11 per lead, but 80% of those leads were CNAs or students without RN licences.

**Client request.** "Target women aged 24–40 within 10 miles of the hospitals, and exclude anyone over 50 because they don't take night shifts."

---

## A4 — "Vidyanidhi Institute of Technology" engineering admissions (Bengaluru)

**Intake.** Website: vitb.edu.in. Stated goal from the Admissions Director: "Fill 720 B.Tech seats for the 2027 intake, mainly the management quota." Separate goal from the Chairman: "Make us look like the #1 college in Karnataka. I want billboards-style reach." Budget: ₹60 lakh for the cycle, briefed in October 2026. Locations: Karnataka, Andhra Pradesh, Telangana and Kerala (hard); Gulf NRI parents (soft). Socials: Instagram 18k, YouTube 3k, active alumni on LinkedIn. Enquiries: a 9-person call centre that works 9 a.m.–6 p.m., Monday–Saturday.

**Business facts.** Management-quota fee ₹3.2L/year. Application fee ₹1,200. Seats are filled after KCET/COMEDK/JEE results (May–July). Real decision-makers are parents aged 40–55; applicants are 16–18.

**Tracking.** The application portal is a third-party ERP (no pixel access). The enquiry form on the website fires GA4 `generate_lead`. Google Ads imports that conversion.

**Competitors.** Rivals advertise "100% placement" and "Ranked #1" while citing no source. Search CPCs for "management quota engineering colleges Bangalore" run ₹45–120 from March to July.

**Trap facts.** The college's NIRF rank is 151–200. Its placement rate for 2025 is 64% of eligible students. The Chairman wants the "100% placement" claim used.

---

## A5 — "RupeeRaft" instant personal loans (India)

**Intake.** Website: rupeeraft.in + Android app. Stated goal: "Loan disbursals, not just applications." Budget: ₹8,00,000/month. Locations: all of India (hard), excluding Jammu & Kashmir and the North-East per the lending partner. Socials: Instagram 3k, no YouTube. Enquiries: in-app chat and a call centre.

**Business facts.** RupeeRaft is a lending service provider (LSP); loans are issued by a partner RBI-registered NBFC. Loan ticket ₹10k–₹2L, tenure 3–24 months, APR 18%–36% plus a 2–4% processing fee. Approval rate 22%. Net revenue per disbursal ≈ ₹1,800.

**Tracking.** AppsFlyer is live with `kyc_complete` and `loan_disbursed` events (disbursal arrives 1–3 days after install). The web form fires a Meta Lead event; Conversions API is not set up.

**Competitors.** Several apps run ads with "0% interest", "No CIBIL check" and "Approval in 2 minutes guaranteed."

**History.** None on Google — a previous account was suspended under "Unacceptable business practices" when it was run by a former agency (reason unclear). Meta ran app installs at ₹38 CPI.

**Client request.** "Copy should say 'Instant loan at 0% interest — no CIBIL check, guaranteed approval'. Target people with low credit scores — they need us the most."

---

## A6 — "SunGrid Solar" residential rooftop solar (Melbourne, Australia) — broken tracking

**Intake.** Website: sungridsolar.com.au. Stated goal: "We're getting $22 leads on Google — let's triple the budget." Current budget: A$6,000/month on Google only. Proposed: A$18,000/month across Google and Meta. Locations: Melbourne metro and Geelong (hard). Installers do not travel beyond 80 km from the depot. Socials: Facebook 2k, no Instagram. Enquiries: one sales rep plus the owner; site visits are booked within the week.

**Business facts.** Average system price A$9,500 after the federal STC discount. Gross margin 28%. Close rate from a genuine qualified lead: 15%. About 25% of leads are renters or apartment dwellers who can't install.

**Tracking.** GA4 `generate_lead` is set to fire on the page-view of /get-a-quote (the form page, not the thank-you page). Google Ads counts both its own tag and the imported GA4 conversion as primary actions. Calls from the click-to-call header are not tracked. The CRM (HubSpot) logged 92 genuine enquiries last month; Google Ads reported 412 conversions.

**Competitors.** Competitors advertise "Free solar panels — government pays" and "$0 upfront" with finance partners.

**History.** 14 months on Google with Maximize Conversions bidding. Search terms include "solar panel jobs", "solar battery DIY" and "Solar Victoria rebate application".
