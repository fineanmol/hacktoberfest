# Quick Guide: How Hacktoberfest Works

> Short, practical guide you can add to any repo to help contributors make valid Hacktoberfest PRs.

---

## What is Hacktoberfest?

Hacktoberfest is an annual month-long celebration of open source where contributors from around the world make pull/merge requests (PRs/MRs) to public repositories. It’s run in partnership with DigitalOcean, MLH, and community sponsors.

## What counts as a valid contribution?

* A **valid** contribution is a pull/merge request that maintainers accept during the event month.
* Good contributions include bug fixes, documentation improvements, test coverage, and small features. Avoid trivial or spammy changes.

## Participation goals and rewards

* The community challenge is to make up to **6 accepted PRs/MRs** during the event to reach the top reward tier.
* Contributors unlock a digital badge as their PRs are accepted.
* The first limited set of "Super Contributors" (official limit per year) who complete the required accepted PRs may receive special swag.

## How to prepare your repository for Hacktoberfest contributors

1. **Add labels**: `good first issue`, `help wanted`, `documentation`.
2. **Create a CONTRIBUTING.md** with steps to run the project locally and how to submit PRs.
3. **Add templates**: Provide an ISSUE_TEMPLATE and PULL_REQUEST_TEMPLATE that guides contributors.
4. **Tag issues** with clear steps and the expected difficulty.
5. **Mention license & code of conduct** so people know how they can contribute safely.

## A short template for a CONTRIBUTING.md (copy into repo)

```
# Contributing to <PROJECT>

Thanks for your interest! To contribute:

1. Fork the repo and clone your fork.
2. Create a branch: `git checkout -b feature/your-short-desc`.
3. Make changes, add tests if relevant.
4. Commit with clear messages: `git commit -m "fix: short description"`.
5. Push and open a PR from your branch: `git push origin feature/your-short-desc`.

Please read our CODE_OF_CONDUCT.md and ensure changes are helpful and non-spammy.
```

## Quick checklist for maintainers reviewing Hacktoberfest PRs

* Is the PR helpful and non-trivial?
* Does it follow style and tests (if available)?
* Is there a clear description and linked issue (if applicable)?
* If you will not accept, politely close with a helpful suggestion.

## Tips for contributors (to make PRs more likely to be accepted)

* Read the project’s README and CONTRIBUTING first.
* Start with documentation, tests, or labeled `good first issue` tasks.
* Ask maintainers if you are unsure about scope—use Issues or Discussions.
* Keep PRs focused and well-documented.

## Suggested `HACKTOBERFEST.md` short blurb for your repo homepage

```
We welcome Hacktoberfest contributions! If you'd like to help, look for issues with `good first issue` or `hacktoberfest` labels. Follow CONTRIBUTING.md before opening a PR.
```

---

### How to use this file

* Copy this markdown into `HACKTOBERFEST_QUICKGUIDE.md` (or add into `CONTRIBUTING.md`) and open a PR.
* If you want, I can tailor the guide to your specific repo (commands to run, dev setup, recommended starter issues).

---

*Created to help maintainers welcome Hacktoberfest contributors with clear expectations.*
