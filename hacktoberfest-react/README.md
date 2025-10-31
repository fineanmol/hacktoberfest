# Hacktoberfest React App (Vite + TypeScript)

A modern React app for showcasing Hacktoberfest contributors with search, sorting, optional GitHub profile enrichment, a splash loader, and rate‑limit friendly UX.

## Tech Stack

- **React + TypeScript** (Vite)
- **Tailwind CSS** for styling (utility classes in `src/index.css`)
- **framer-motion** for subtle animations
- **react-hot-toast** for non-blocking notifications
- Optional data enrichment via **GitHub REST API**

## Quick Start

1. Install dependencies
```bash
npm install
```
2. Start the dev server
```bash
npm run dev
```
3. Build for production
```bash
npm run build && npm run preview
```

> Note: You may see Node engine warnings from Vite plugins if your Node version is slightly below the suggested range. The app should still run. If you prefer, upgrade Node to the version shown in the warnings.

## Project Structure

- `src/App.tsx` – main page (search, filters, contributor grid, splash overlay, token UI)
- `src/components/Navbar.tsx` – sticky top navigation
- `src/components/Footer.tsx` – footer with links
- `src/components/ContributorCard.tsx` – contributor card UI
- `src/components/Loader.tsx` – animated SVG loader (styled-components)
- `src/index.css` – Tailwind utilities and custom classes (buttons, inputs, gradients)
- `contributors/` – two JS lists loaded at runtime (combined/deduped in `App.tsx`)

## Features

- **Search** by name or username
- **Sort** by name or public repos (asc/desc)
- **Profile enrichment**: optional GitHub API calls fetch avatar/name/company/location/public repos for visible contributors
- **Debounce** on inputs to reduce unnecessary fetches
- **Splash Loader**: a full-screen overlay ensures the loader is visible briefly on initial load
- **Rate-limit handling**: toast + inline message; optional GitHub token to raise limits

## GitHub Personal Access Token (PAT)

Unauthenticated requests are limited by IP (typically ~60 req/hour). To increase limits, provide a **GitHub PAT** via `.env`.

- Variable: `VITE_GITHUB_TOKEN`
- File: create `.env` (or `.env.local`) at project root
- Example:

```env
VITE_GITHUB_TOKEN=ghp_yourTokenHere
```

Notes:
- Vite only exposes variables prefixed with `VITE_` to client code.
- For public profile reads, scopes are generally not required; `read:user` is sufficient if you prefer.
- Restart the dev server after changing `.env`.

Error handling:
- `401` → “Invalid GitHub token” toast
- `403` → rate limit reached → inline message suggests adding `.env` token; the app also uses cached data to reduce API calls

## Loader Splash Behavior

- The loader is rendered as a full-screen overlay while either:
  - Initial data is being prepared, or
  - The minimum splash timer is active (see `minSplashMs` in `src/App.tsx`)
- Adjust `minSplashMs` to control minimum visibility (e.g., to guarantee N animation cycles)

## Data Caching

- Profile details fetched from GitHub are cached in `localStorage` under `gh_profile_cache`.
- On subsequent visits or reloads, cached profiles are used to avoid re-fetching and reduce rate-limit pressure.

## Styling

- Tailwind utilities are defined/used in `src/index.css` via `@apply`
- Helpful classes:
  - `.btn-primary`, `.card`, `.input-field`, `.text-gradient`, `.divider`
- If your editor flags `@apply`/`@theme` as unknown at-rules, that’s a tooling lint—build still works under Vite/Tailwind

## Scripts

- `npm run dev` – start development server
- `npm run build` – build production assets
- `npm run preview` – preview the production build

## Environment & Security

- PAT is stored in browser `localStorage` only; never committed to the repo
- Do not share your PAT; clear it if you are screen-sharing or handing off your machine

## Troubleshooting

- **API rate limit (403)**: Add a PAT in the UI; wait a few minutes; reduce batch size (handled internally)
- **Invalid token (401)**: Verify you pasted the token correctly; regenerate if needed
- **Node engine warnings**: Upgrade Node to the version mentioned by Vite for best compatibility
- **Tailwind `@apply` warnings**: Editor lints only; the app compiles and runs

## Contributing

Contributions are welcome! Typical flow:

- Fork the repo and create a feature branch
- Keep PRs focused and small when possible
- Run `npm run dev` locally and verify UI/UX
- If you add new configuration or features, update this README

