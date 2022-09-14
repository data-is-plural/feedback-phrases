# Data Is Plural “Feedback” Phrases

Each emailed edition of [Data Is Plural](https://www.data-is-plural.com/) concludes with a mostly-boilerplate paragraph that looks like this:

> *Dataset suggestions? Criticism? Praise? Send firmly-rooted feedback to jsvine@gmail.com, or just reply to this email. Looking for past datasets? [This spreadsheet contains them all](https://docs.google.com/spreadsheets/d/1wZhPLMCHKJvwOkP4juclhjFgqIY8fQFMemwKL2c64vk/edit#gid=0). Visit [data-is-plural.com](https://www.data-is-plural.com) to subscribe and to browse past editions.*

The structure has largely remained the same since the newsletter’s inception, but the phrase soliciting feedback changes (almost) every week. It typically reflects the topic of the fifth/final item in that week’s edition. For instance, in the example above, “firmly-rooted feedback” riffs on [that edition’s](https://www.data-is-plural.com/archive/2022-09-07-edition/) final item, a [dataset of 5,000,000+ urban trees](https://datadryad.org/stash/dataset/doi:10.5061/dryad.2jm63xsrf).

This repository — created in September 2022 to celebrate Data Is Plural’s 300th edition — provides a [dataset of all the feedback phrases](data/phrases.csv) in the newsletter’s history. (Hat-tip to [Aliza Aufrichtig](https://twitter.com/alizauf) for the fun idea 💫.) 

## The Dataset

The dataset is [available](data/) in two widely-supported open formats: CSV and JSON. Both files contain the same information and the same fields:


|Field|Description|Example Value|
|---|---|---|
|`date`|The date of the newsletter edition.|`2022-09-07`|
|`verb`|The verb that starts the full feedback phrase.|`Send`|
|`core`|The core part of the feedback phrase. In the original text, it comes directly after the verb and directly before the preposition. It typically (but not always) includes the word “feedback”.|`firmly-rooted feedback`|
|`preposition`|Either “to” or “at”. Directly precedes the feedback-receiving email address.|`to`|
|`fifth_hed`|The “hed” of the fifth (i.e., final) item in the edition, to which the feedback phrase is typically related. |`Even more street trees.`|

## Notes & Observations

- Although most of the `core` entries take the form of `[adjective] feedback`, not all do. Some counter-examples include entries without the word “feedback” (e.g., `angry hand gestures`), entries where the modifer follows instead of precedes the word “feedback” (e.g., `feedback via raven`), multi-word modifiers (e.g., `happy little bits of feedback`), and plain, unmodified `feedback`.

- Although every entry is supposed to be unique, they have sometimes repeated. This has been mostly unintentional, owing to some combination of bad memory, carelessness, and/or a lack of creativity.

- The `verb` has almost always been `Send`, but some exceptions include `Lob`, `Throw`, `Instagram`, and `Fling`.

- Likewise, the `preposition` has almost always been `to`, but occasionally becomes `at` when the `verb` demands it.

## Code

This repository also contains a [simple Python script](scripts/extract.py) to extract the dataset from the newsletter’s [Markdown-formatted archive](https://github.com/data-is-plural/newsletter-archive). For the script to work, you’ll need first to run this command from the repository’s root directory: `git clone https://github.com/data-is-plural/newsletter-archive.git archive`.

## Licensing

 The data files in this repository are available under the [Creative Commons Attribution 4.0 International (CC BY 4.0) license](https://creativecommons.org/licenses/by/4.0/). The code is available under the [MIT License](https://opensource.org/licenses/MIT).

## Meta-Feedback?

[Get in touch 📨](https://www.jsvine.com/)
