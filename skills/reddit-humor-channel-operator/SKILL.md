---
name: reddit-humor-channel-operator
description: End-to-end Telegram humor channel operations via Adam user account (q tg): create/brand channel, source top Reddit jokes/memes, prepare approval-first candidate queue with rationale, publish after explicit approval, forward published posts to owner, run 4x/day optimization loops with growth analysis and critical review of new promotion articles.
---

# Reddit Humor Channel Operator

## Use this skill to
- Launch a new humor channel from scratch.
- Run an approval-first editorial pipeline (candidate -> owner approval -> publish).
- Operate via `q tg` (Telethon/user account) when user-context actions are required.
- Maintain growth loop with recurring research and strategy updates.

## Operating rules
1. Keep owner identity private by default:
   - Prefer private channel during setup.
   - Avoid unnecessary linked chats and signature attribution.
2. Never publish candidate content before explicit owner approval unless owner asked for immediate posting in the same request.
3. For every candidate, provide:
   - source link,
   - why it should work (hook + relatability + repost potential),
   - publication format (text/image/video, caption draft, CTA).
4. After publishing, forward the exact post to owner DM and report `channel_post_id` + `forward_message_id`.
5. CRITICAL formatting rule: never send literal `\\n` in Telegram text/captions. Use actual newline characters only.

## Daily cycle (4x/day)
1. Pull fresh top content from selected Reddit sources.
2. Filter for language risk, NSFW risk, cultural mismatch.
3. Prepare 3 shortlist candidates for approval.
4. Analyze channel traction (views/forwards/sub growth where available).
5. Find 5 new growth articles not used previously.
6. Critically evaluate advice (evidence quality, survivorship bias, paywalled upsell bias).
7. Update action plan and propose one concrete experiment for next cycle.

## Suggested Reddit source mix
- `r/Jokes` (text punchlines)
- `r/funny` (broad visual humor)
- `r/meirl` (relatable content)
- Optional rotation: `r/WhitePeopleTwitter`, `r/ProgrammerHumor`, `r/2meirl4meirl`

## Publication framework
- Adapt, do not blindly copy.
- Keep Russian copy concise and native.
- Add lightweight attribution: `Источник идеи: r/<subreddit>`.
- End with short engagement prompt when suitable.

## Cron recommendation
- Run every 6 hours (`0 */6 * * *`, UTC).
- Reminder text must explicitly mention it is a reminder and include required checklist.

## Minimal deliverable format to owner
- Candidate A/B/C
- Why each may perform
- Suggested posting time slot
- Recommended pick
- "Publish now?" confirmation prompt
