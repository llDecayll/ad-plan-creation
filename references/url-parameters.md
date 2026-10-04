# URL parameters

## Checks
- Does the site keep query strings? Open `<landing-url>?utm_source=test&gclid=test` and confirm the parameters survive (no redirect that strips them).
- Does the landing page redirect (http→https, www, trailing slash, language)? Use the final URL in ads.
- Is there an existing UTM convention in links (from social profiles, newsletters)? Match it.
- Google Ads auto-tagging (gclid) should stay ON. Do not overwrite gclid with manual tracking.

## Naming convention (recommend)
Lowercase, hyphens, no spaces: `client_platform_objective_location_audience`.
Example campaign: `paintkraft_meta_leads_blr_broad`.

## Meta (Ads Manager > Ad > Tracking > URL parameters)
```
utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&placement={{placement}}
```
Meta dynamic values: `{{campaign.id}}`, `{{campaign.name}}`, `{{adset.id}}`, `{{adset.name}}`, `{{ad.id}}`, `{{ad.name}}`, `{{placement}}`, `{{site_source_name}}`.
For WhatsApp/instant-form campaigns there is no landing page, so UTMs don't apply. Attribute via the campaign/ad names in the lead export and by putting a campaign code in the WhatsApp greeting (e.g. "Hi, I'd like a free quote [PK-BLR1]") so the CRM can tag it.

## Google (Campaign or account > Settings > Tracking template / Final URL suffix)
Final URL suffix:
```
utm_source=google&utm_medium=cpc&utm_campaign={_campaign}&utm_term={keyword}&utm_content={creative}&matchtype={matchtype}&device={device}&network={network}&campaignid={campaignid}&adgroupid={adgroupid}
```
Set a custom parameter `{_campaign}` per campaign, or use `{campaignid}` and map IDs in the CRM.
Useful ValueTrack: `{keyword}`, `{matchtype}`, `{device}`, `{network}`, `{placement}`, `{loc_physical_ms}`, `{campaignid}`, `{adgroupid}`, `{creative}`.

## CRM capture
Tell the user to capture UTM fields and gclid/fbclid in hidden form fields so each lead in the CRM carries its campaign. That is what makes the lead-quality counts per campaign possible later.
