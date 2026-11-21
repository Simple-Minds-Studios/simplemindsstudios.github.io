# Thinking Clearer inline player — November 21, 2026

The homepage Listen section now lets visitors load any of the three published
Thinking Clearer episodes in one responsive YouTube player. This implements the
recommendation recorded in [2lincolns issue 15](https://github.com/Bartron773/2lincolns/issues/15).

- The player is created only after a visitor selects an episode or chooses
  **Load episode player**. There is no embedded YouTube player on initial load.
- The privacy-enhanced `youtube-nocookie.com` embed uses `autoplay=0`.
  Visitors start playback with YouTube's own play control.
- Selecting another episode reuses the single iframe and replaces its source.
  **Close player** removes it and restores focus to the load button.
- The selected episode has an accessible pressed state and a matching
  **Watch on YouTube** fallback. A no-JavaScript message links all three episodes.
- The existing contact information, project catalog, canonical metadata,
  favicon, analytics, and sharing image are retained.

## Validation before publication

- YouTube's official oEmbed endpoint returned HTTP 200 for all three video IDs
  and identified Simple Minds Studios as the author.
- Browser checks confirmed click-to-load behavior, the three matching embed
  URLs, one iframe after switching, zero after closing, and restored focus.
- The native YouTube player and play control loaded for all three episodes.
  Selecting Play on episode 001 produced an active video element; this is not
  a full uninterrupted playback or audio-quality test.
- Layout checked at desktop, 390 × 844, and 320 × 740. No horizontal page
  overflow occurred at the phone sizes. The narrow-screen placeholder was
  adjusted to show the full title, action, and loading note.
- JavaScript syntax and HTML ID/episode checks passed. Both custom-domain and
  project-path builds passed.
- The live public catalog comparison passed: 23 entries, covering all 22 public
  organization repositories and the Hart exhibit.

YouTube can restrict playback by video, browser, network, or region. The external
fallback remains visible without depending on iframe load events as proof that
the video can play.

## Live verification

Implementation commit: `c74b716e485895171ec509a84ba1ca7ab17f57a3`.
[GitHub Pages deployment](https://github.com/Simple-Minds-Studios/simplemindsstudios.github.io/actions/runs/44954846809)
succeeded. The live homepage, stylesheet, and player script returned HTTP 200
and matched the committed source byte for byte.

On the public domain, the player was absent initially, appeared after selecting
an episode, and switched to Borrowed Thoughts with one iframe and the matching
YouTube fallback. The native YouTube controls and episode cover loaded. A full
audio-playback test was not confirmed in the test browser; the video's elapsed
time remained at zero after pressing Play.

Live visual record: [Listen section](../.github/reports/podcast-player-live-2026-11-21.jpg).
