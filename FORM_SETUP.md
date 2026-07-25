# Google Forms setup for 214southave.com

Use **Google Forms** (free, works on mobile QR traffic). Responses can email **savagepropsllc@gmail.com**.

Create **two forms** while signed into the Google account that owns `savagepropsllc@gmail.com` (or that can forward to it).

---

## Form 1 — Offering packet + showing request (`{{FORM_URL}}`)

**Title:** `214 South Ave SE — Offering Packet / Showing Request`

**Suggested fields:**
1. Full name (Short answer, Required)
2. Email (Short answer, Required)
3. Phone (Short answer, Required)
4. What do you need? (Multiple choice, Required)
   - Offering packet
   - Request a showing
   - Both
5. Are you working with a buyer’s agent? (Multiple choice)
   - Yes / No / Not sure
6. Agent name & brokerage (Short answer)
7. Anything else we should know? (Paragraph)

**Get the short link:**
1. Open the form → **Send** (top right)
2. Click the **link** icon
3. Turn on **Shorten URL**
4. Copy the `https://forms.gle/...` link

**Email every response to savagepropsllc@gmail.com:**
1. In the form editor, open the **Responses** tab
2. Click the Google Sheets icon → create a linked sheet (recommended)
3. Or: three-dot menu → **Get email notifications for new responses**
4. If the form is owned by another account, add `savagepropsllc@gmail.com` as an editor, or set the linked Sheet to notify that inbox

**Optional — prefill “what do you need?” from each button:**  
Google Forms supports URL params. For now both buttons can share the same short link; the multiple-choice field covers packet vs showing.

---

## Form 2 — Post-visit feedback (`{{FEEDBACK_FORM_URL}}`)

**Title:** `214 South Ave SE — Visit Feedback`

**Suggested fields:**
1. Email (optional)
2. Did you tour the property? (Yes / No)
3. What stood out? (Paragraph)
4. Any concerns? (Paragraph)
5. Interest level (Multiple choice: Strong / Maybe / Not a fit)

Same steps: **Send → link → Shorten URL**, plus email notifications to `savagepropsllc@gmail.com`.

---

## Wire the links into the site

In `index.html`, search/replace:

| Placeholder | Paste |
|---|---|
| `{{FORM_URL}}` | your packet/showing `https://forms.gle/...` |
| `{{FEEDBACK_FORM_URL}}` | your feedback `https://forms.gle/...` |

There are multiple `{{FORM_URL}}` instances (header, hero, documents, offer, contact, footer). Replace all.

Then commit and push so Vercel deploys.

---

## Quick test checklist

- [ ] Open form on your phone; submit a test response
- [ ] Confirm email arrives at `savagepropsllc@gmail.com`
- [ ] Tap **Get the Offering Packet** and **Request a Showing** on the live site
- [ ] Tap footer **Share your feedback**
