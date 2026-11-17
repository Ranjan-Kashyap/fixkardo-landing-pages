# FixKardo Meta Ads Landing Pages

Self-contained HTML landing pages for FixKardo Meta (Facebook / Instagram) campaigns. Built for **GoHighLevel (GHL)** on `app.fixkardo.com` — each page is one file with inline CSS and vanilla JS (no build step, no frameworks).

Prepared with ScaleRise · November 2026.

---

## Pages

| Preview (full HTML) | Paste into GHL Custom HTML | Campaign | Live URL (later) |
|---|---|---|---|
| `sales/salon-at-home/index.html` | `sales/salon-at-home/ghl-paste.html` | Women's salon at home | `app.fixkardo.com/salon-at-home` |
| `sales/paonta-home-services/index.html` | `sales/paonta-home-services/ghl-paste.html` | Home services in Paonta Sahib | `app.fixkardo.com/paonta-home-services` |
| `partner/join-as-a-partner/index.html` | `partner/join-as-a-partner/ghl-paste.html` | Partner onboarding | `app.fixkardo.com/join-as-a-partner` |

Also included:

- `head-snippet.html` — Google Fonts + Meta Pixel base code for GHL's **head** tracking box
- `assets/` — images hosted via GitHub → jsDelivr CDN (same pattern as Manas Yoga Routine)
- `ghl-paste.html` next to each page — **exactly** what to copy into GHL (the `#fk-lp` block)

---

## 1. Preview locally

Open any page in a browser (double-click or drag into Chrome):

- `sales/salon-at-home/index.html`
- `sales/paonta-home-services/index.html`
- `partner/join-as-a-partner/index.html`

**Salon city test:** open with a query param, e.g.

`sales/salon-at-home/index.html?city=solan`

Unknown or missing city falls back to **"your city"** (ref code `GEN`).

---

## 2. Set up in GoHighLevel

For **each** page:

1. Create a funnel or website page with the matching slug (`salon-at-home`, `paonta-home-services`, `join-as-a-partner`).
2. Add **one full-width section** with a single **Custom HTML / Custom Code** element (section padding 0 if GHL offers it).
3. Open the matching `ghl-paste.html`, select all, copy, and paste into that element.
4. Open the page's **Tracking Code → Head** (or site-level head tracking) and paste the contents of `head-snippet.html` (optional but recommended for Meta Pixel + earlier font load). Brand fonts and Material Symbols also self-load from the paste JS, so icons still work if the head snippet is missing.
5. In both the head snippet and the page `CONFIG` object, replace `REPLACE_WITH_META_PIXEL_ID` with your real Pixel ID (or leave the placeholder — the Pixel simply won't load).
6. For the partner page, set `FORM_WEBHOOK_URL` to your GHL **Inbound Webhook** URL from the workflow that should capture partner leads.
7. **Push this repo to GitHub** and keep it **public** so jsDelivr can serve `assets/` (see below). No GHL Media Library needed.

> CSS is scoped under `#fk-lp`. A small script expands GHL's parent column/row so the page is full-bleed (same approach as Manas Yoga Routine). Fonts self-load from the paste; Pixel stays in the head snippet (or page `CONFIG`).

---

## 3. CONFIG fields

Each page has a `CONFIG` object near the top of its `<script>`.

| Field | Pages | What it does | Where to get it |
|---|---|---|---|
| `PIXEL_ID` | All | Meta Pixel ID. If it still starts with `REPLACE_`, Pixel is skipped (no errors). | Meta Events Manager → your Pixel |
| `PHONE_DISPLAY` | All | Phone shown in the footer | Client |
| `PHONE_TEL` | All | `tel:` link value (E.164, no spaces) | Client |
| `WHATSAPP_NUMBER` | Sales | Digits for `wa.me` (country code, no `+`) | Client |
| `PRIVACY_URL` | All | Privacy Policy link in footer / consent | Confirm live URL on fixkardo.com |
| `PAGE_NAME` | All | Used as `content_category` in Pixel events | Leave as-is |
| `IMAGES` | All | Map of image keys → jsDelivr CDN URLs | Served from this GitHub repo's `assets/` |
| `CITY` | Paonta only | Fixed city label | Leave as `"Paonta Sahib"` |
| `FORM_WEBHOOK_URL` | Partner only | GHL inbound webhook for the short form `POST` | GHL Workflow → Inbound Webhook trigger |
| `REGISTER_URL` | Partner only | Where partners finish signup after the form | `https://fixkardo.com/register/business` |

### Partner webhook payload

```json
{
  "name": "…",
  "phone": "+91XXXXXXXXXX",
  "city": "…",
  "service": "…",
  "source": "meta_partner_lp",
  "page_url": "…",
  "utm_source": "…",
  "utm_medium": "…",
  "utm_campaign": "…",
  "utm_content": "…",
  "utm_term": "…",
  "fbclid": "…",
  "submitted_at": "ISO-8601"
}
```

On success (or if the webhook is a placeholder / fails / times out after 4s), the partner is redirected to `REGISTER_URL` with `name`, `phone`, `city`, `service`, and UTM / `fbclid` query params.

---

## 4. Ad URL examples

```
https://app.fixkardo.com/salon-at-home?city=solan&utm_source=meta&utm_campaign=salon_solan
https://app.fixkardo.com/salon-at-home?city=chandigarh&utm_source=meta&utm_medium=paid&utm_campaign=salon_chd&utm_content=carousel_1
https://app.fixkardo.com/paonta-home-services?utm_source=meta&utm_campaign=paonta_home
https://app.fixkardo.com/join-as-a-partner?utm_source=meta&utm_campaign=partner
```

### Salon `city` whitelist

| slug | Display | WhatsApp ref |
|---|---|---|
| `vikasnagar` | Vikasnagar | `VKN` |
| `paonta` | Paonta Sahib | `PAO` |
| `nahan` | Nahan | `NAH` |
| `solan` | Solan | `SOL` |
| `baddi` | Baddi | `BDI` |
| `shimla` | Shimla | `SML` |
| `chandigarh` | Chandigarh | `CHD` |
| `mohali` | Mohali | `MOH` |

---

## 5. Pixel events

| Action | Event | Params |
|---|---|---|
| Page load | `PageView` | (base code) |
| WhatsApp click | `Contact` | `content_name: WhatsApp`, `content_category`, `city` |
| Call click | `Contact` | `content_name: Call`, `content_category`, `city` |
| Partner form success | `Lead` | `content_name: Partner signup form`, `city`, `service` |

UTMs and `fbclid` are stored in `sessionStorage` on every page.

---

## 6. Assets (GitHub → jsDelivr)

GHL has no project image folder for custom HTML, so images live in this repo and are linked via **jsDelivr** (same as Manas Yoga Routine):

```
https://cdn.jsdelivr.net/gh/Ranjan-Kashyap/fixkardo-landing-pages@main/assets/<filename>
```

**Requirement:** this GitHub repo must be **public** (Manas is public; jsDelivr cannot read private repos). Then commit + push `assets/` to `main`. After an image change, wait ~1–2 minutes (or bump `?v=2` on the URL if CDN is cached).

| File | Use |
|---|---|
| `fixkardo-logo.png` | Top bar + footer |
| `salon-hero.webp` | Salon hero (4:5) |
| `salon-door.webp`, `salon-facial.webp`, `salon-hairspa.webp`, `salon-manicure.webp`, `salon-blowdry.webp`, `salon-waxing.webp`, `salon-threading.webp`, `salon-mehendi.webp` | Salon services / strip |
| `paonta-hero.webp` | Paonta hero (4:5) |
| `svc-electrician.webp`, `svc-plumber.webp`, `svc-ro.webp`, `svc-tank.webp`, `svc-mens-salon.webp` | Paonta service cards |
| `partner-hero.webp` | Partner hero (4:5) |

---

## 7. Brand tokens (from fixkardo.com)

| Token | Value |
|---|---|
| Green | `#0F9F59` |
| Yellow | `#F4B400` |
| Navy text | `#0F172A` |
| Background | `#FAFAF5` |
| Dark CTA | `#112119` |
| WhatsApp | `#25D366` |
| Font | Work Sans + Mukta (Devanagari) |
| Icons | Material Symbols Rounded |
| Radius | 12px (cards 16px) |
