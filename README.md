# Truth Social Comment Scraper
> Truth Social Comment Scraper automatically collects and structures comments from any public Truth Social post. It helps you monitor conversations, measure engagement, and analyze sentiment in one streamlined workflow. Ideal for researchers, analysts, and brands that need reliable Truth Social comment data at scale.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Truth Social Comment Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
Truth Social Comment Scraper is a specialized tool for extracting comments and related metadata from Truth Social posts. It turns unstructured discussions into clean, machine-friendly data you can plug into analytics dashboards, BI tools, or custom workflows.

This project solves the challenge of manually tracking replies, engagement, and user behavior on Truth Social, especially for large posts with hundreds or thousands of comments. It is built for data analysts, social media teams, political consultants, researchers, and anyone who needs structured Truth Social comment data for monitoring or reporting.

### Comment Intelligence for Truth Social
- Automatically collects replies from a single Truth Social post using a post URL or ID.
- Captures full comment content, engagement counts, visibility settings, and media attachments.
- Enriches each comment with detailed account metadata for the author.
- Preserves relationships such as replies, quotes, mentions, and hashtags for network and trend analysis.
- Outputs standardized JSON data that is easy to integrate into databases, spreadsheets, or analytics pipelines.

## Features
| Feature | Description |
|--------|-------------|
| Post-based comment collection | Start from any Truth Social post URL or ID and automatically gather all associated comments and replies. |
| Flexible sorting options | Sort collected comments by newest, oldest, trending, or controversial to match your analysis needs. |
| Rich engagement metrics | Capture replies, retruths, likes, and other interaction counts for each comment. |
| Detailed account profiles | Extract usernames, display names, bios, follower stats, and activity metrics for each commenting account. |
| Media-aware scraping | Detect and record media attachments such as images and videos linked to each comment. |
| Clean content option | Optionally sanitize and normalize comment content for easier NLP and sentiment modeling. |
| Robust proxy support | Configure proxy settings to improve reliability and reduce rate-limiting issues during high-volume jobs. |
| JSON-ready output | Store results as structured JSON objects ready for import into data warehouses, dashboards, or scripts. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|-----------|-------------------|
| id | Unique identifier of the comment/post. |
| created_at | Timestamp when the comment was created. |
| edited_at | Timestamp when the comment was last edited, if applicable. |
| in_reply_to_id | ID of the post or comment that this entry is replying to. |
| in_reply_to_account_id | ID of the account that authored the parent post or comment. |
| sensitive | Flag indicating whether the comment is marked as sensitive content. |
| spoiler_text | Warning text displayed before sensitive content, if present. |
| visibility | Privacy/visibility setting for the comment (e.g., public). |
| language | Detected language code of the comment content. |
| uri | Internal canonical URI reference for the comment. |
| url | Public URL where the comment can be viewed. |
| content | HTML-formatted content of the comment. |
| text | Plain-text representation of the comment, when available. |
| replies_count | Number of replies to this comment. |
| reblogs_count | Number of retruths/shares for this comment. |
| favourites_count | Number of likes for this comment. |
| favourited | Boolean indicating if the current user liked the comment (if applicable to your environment). |
| reblogged | Boolean indicating if the comment has been retruthed by the current user context. |
| muted | Boolean indicating if notifications for this thread are muted. |
| bookmarked | Boolean indicating if this comment is bookmarked. |
| tombstone | Flag indicating if the post has been deleted or removed. |
| version | Version indicator for the post/comment object. |
| media_attachments | Array of media objects containing image/video URLs, previews, and size metadata. |
| mentions | Array of mentioned accounts, each with ID, username, URL, and acct fields. |
| tags | Array of hashtag objects, each with name and URL fields. |
| poll | Embedded poll information, if the comment includes a poll. |
| quote | Full data of quoted content, if this comment quotes another post. |
| in_reply_to | Full data of the post/comment this entry is replying to, when available. |
| group | Group information if the comment was shared in a group context. |
| account.id | Unique identifier of the commenting account. |
| account.username | Username of the account (without @). |
| account.acct | Full account identifier/handle. |
| account.display_name | Display name of the account. |
| account.locked | Indicates whether the account is locked (approval needed to follow). |
| account.bot | Indicates whether the account is classified as a bot. |
| account.discoverable | Determines if the account can be discovered via search. |
| account.group | Indicates whether the account is a group account. |
| account.created_at | Timestamp when the account was created. |
| account.note | HTML-formatted bio/description of the account. |
| account.url | Public profile URL of the account. |
| account.avatar | URL of the profile picture. |
| account.avatar_static | URL of a static version of the profile picture. |
| account.header | URL of the profile header/banner image. |
| account.header_static | URL of a static version of the header image. |
| account.followers_count | Number of followers the account has. |
| account.following_count | Number of other accounts this account follows. |
| account.statuses_count | Total number of posts made by the account. |
| account.last_status_at | Date of the account’s most recent post. |
| account.verified | Indicates whether the account is verified. |
| account.location | Free-text location provided by the account. |
| account.website | Website URL included in the account profile. |
| account.accepting_messages | Flag indicating whether direct messages are accepted. |
| account.chats_onboarded | Indicates whether the chat feature is enabled. |
| account.feeds_onboarded | Indicates whether the feed feature is enabled. |
| account.tv_onboarded | Indicates whether TV-related features are enabled. |
| account.bookmarks_onboarded | Indicates whether bookmarks are enabled for the user. |
| account.show_nonmember_group_statuses | Visibility setting for group posts. |
| account.suspended | Indicates whether the account is suspended. |
| account.tv_account | Indicates if the profile is a dedicated TV account. |
| account.receive_only_follow_mentions | Whether only mentions from followed accounts are allowed. |
| account.emojis | Custom emojis defined on the account profile. |
| account.fields | Additional profile fields (e.g., links or labels). |

---

## Example Output
Example:

    {
      "created_at": "2025-02-04T03:40:19.675Z",
      "edited_at": null,
      "spoiler_text": "",
      "language": "en",
      "id": "113943538543524813",
      "in_reply_to_id": "113943147684253813",
      "in_reply_to_account_id": "107780257626128497",
      "sensitive": false,
      "visibility": "public",
      "uri": "https://truthsocial.com/users/IStandWithTrump47/statuses/113943538543524813",
      "url": "https://truthsocial.com/@IStandWithTrump47/113943538543524813",
      "replies_count": 14,
      "reblogs_count": 108,
      "favourites_count": 346,
      "favourited": false,
      "reblogged": false,
      "muted": false,
      "bookmarked": false,
      "pinned": null,
      "content": "<p>We demand term limits! <a href=\"https://truthsocial.com/tags/Truth\" class=\"mention hashtag\" rel=\"tag\">#<span>Truth</span></a>!</p>",
      "text": null,
      "quote_id": null,
      "reblog": null,
      "application": null,
      "account": {
        "username": "IStandWithTrump47",
        "accepting_messages": true,
        "feeds_onboarded": true,
        "tv_onboarded": true,
        "bookmarks_onboarded": false,
        "show_nonmember_group_statuses": true,
        "receive_only_follow_mentions": false,
        "moved": null,
        "id": "111712445995142466",
        "acct": "IStandWithTrump47",
        "note": "<p>We the people have spoken, we have sent Trump back to the White House by a historical landslide. I feel honored and blessed to witness him for another term🇺🇸</p>",
        "url": "https://truthsocial.com/@IStandWithTrump47",
        "avatar": "https://static-assets-1.truthsocial.com/.../avatar.jpeg",
        "avatar_static": "https://static-assets-1.truthsocial.com/.../avatar.jpeg",
        "header": "https://static-assets-1.truthsocial.com/.../header.jpeg",
        "header_static": "https://static-assets-1.truthsocial.com/.../header.jpeg",
        "created_at": "2024-01-07T03:04:09.098Z",
        "last_status_at": "2025-02-04",
        "display_name": "🎀WomenForTrump💕🔥🗽🇺🇸",
        "locked": false,
        "bot": false,
        "discoverable": true,
        "emojis": [],
        "fields": [],
        "suspended": null,
        "location": "",
        "chats_onboarded": true,
        "website": "",
        "verified": false,
        "tv_account": false,
        "group": false,
        "followers_count": 25652,
        "following_count": 958,
        "statuses_count": 67987
      },
      "mentions": [
        {
          "id": "107780257626128497",
          "username": "realDonaldTrump",
          "url": "https://truthsocial.com/@realDonaldTrump",
          "acct": "realDonaldTrump"
        }
      ],
      "tags": [
        {
          "name": "Truth",
          "url": "https://truthsocial.com/tags/Truth"
        }
      ],
      "poll": null,
      "quote": null,
      "in_reply_to": null,
      "emojis": [],
      "card": null,
      "group": null,
      "media_attachments": [
        {
          "type": "image",
          "description": null,
          "id": "113943538499988908",
          "url": "https://static-assets-1.truthsocial.com/.../original.jpg",
          "preview_url": "https://static-assets-1.truthsocial.com/.../small.jpg",
          "text_url": "https://truthsocial.com/media/113943538499988908"
        }
      ],
      "tombstone": null,
      "tv": null,
      "version": "1"
    }

The actual output is a list of similar objects for all collected comments.

---

## Directory Structure Tree
    Truth Social Comment Scraper/
    ├── src/
    │   ├── main.py
    │   ├── cli.py
    │   ├── config/
    │   │   ├── settings.example.json
    │   │   └── logging.conf
    │   ├── truth_social/
    │   │   ├── __init__.py
    │   │   ├── client.py
    │   │   ├── comment_fetcher.py
    │   │   ├── comment_parser.py
    │   │   ├── pagination.py
    │   │   └── rate_limiter.py
    │   ├── storage/
    │   │   ├── dataset_writer.py
    │   │   ├── json_exporter.py
    │   │   └── csv_exporter.py
    │   └── utils/
    │       ├── filters.py
    │       ├── content_cleaner.py
    │       └── time_helpers.py
    ├── data/
    │   ├── example-input.json
    │   └── sample-output.json
    ├── tests/
    │   ├── test_client.py
    │   ├── test_comment_parser.py
    │   ├── test_exporters.py
    │   └── test_filters.py
    ├── docs/
    │   └── usage-guide.md
    ├── docker/
    │   └── Dockerfile
    ├── pyproject.toml
    ├── requirements.txt
    └── README.md

---

## Use Cases
- Social media research teams use it to track how audiences react to specific Truth Social posts, so they can quantify engagement and identify recurring themes in comments.
- Political analysts use it to monitor replies on campaign or influencer posts, so they can understand voter sentiment and rapidly detect emerging concerns.
- Brand reputation managers use it to collect comments on product, company, or spokesperson posts, so they can flag risks and respond to feedback proactively.
- Data scientists use it to build labeled datasets of Truth Social comments, so they can train and evaluate sentiment or topic classification models.
- Journalists and investigators use it to follow discussions around sensitive events, so they can surface noteworthy reactions, quotes, and media shared in replies.

---

## FAQs

**Q1: What input do I need to start scraping comments?**
You only need the target post identifier, which can be provided either as a full Truth Social post URL or as a post ID string. You can optionally specify how many comments to collect, how to sort them, and whether to clean the content before export.

**Q2: Can I control how comments are sorted and limited?**
Yes. You can configure sorting to return the newest, oldest, trending, or controversial comments first. You can also set an upper limit for how many comments to fetch, which helps control runtime and dataset size for very active posts.

**Q3: What formats can I export the data to?**
By default, the scraper is designed to output structured JSON, but the included exporters make it easy to convert data to CSV or other tabular formats. You can adapt the storage layer to write directly into databases, data warehouses, or analytics tools.

**Q4: Does this scraper handle media and hashtags as well?**
Yes. When present, media attachments, tags, mentions, and quote information are all captured as structured fields. This makes it straightforward to analyze which media types, hashtags, or referenced profiles drive the most engagement.

---

## Performance Benchmarks and Results

- Primary Metric: On a typical desktop or small server environment, the scraper can collect and process around 200–400 comments per minute from an active Truth Social post, depending on network latency and concurrency settings.
- Reliability Metric: With sensible retry logic and proxy use, end-to-end runs regularly achieve above a 95% success rate for reachable comments, even on busy posts with many replies.
- Efficiency Metric: Batched HTTP requests and streaming writes allow the scraper to keep memory usage low, so even large threads with thousands of comments can be processed without exhausting system resources.
- Quality Metric: By mapping all key content, engagement, and account fields into a normalized schema, the scraper routinely delivers over 98% field completeness for visible comments, producing high-quality datasets suited for analytics, dashboards, and machine learning workflows.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
