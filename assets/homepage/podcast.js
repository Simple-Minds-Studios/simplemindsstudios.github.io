/* One click-to-load YouTube player; episode links remain available as a fallback. */
(() => {
  const slot = document.querySelector('#podcast-player-slot');
  const placeholder = document.querySelector('#podcast-placeholder');
  const loadButton = document.querySelector('#podcast-load');
  const closeButton = document.querySelector('#podcast-close');
  const title = document.querySelector('#podcast-selected-title');
  const watchLink = document.querySelector('#podcast-youtube');
  const message = document.querySelector('#podcast-message');
  const buttons = [...document.querySelectorAll('[data-podcast-episode]')];
  if (!slot || !placeholder || !loadButton || !closeButton || !title || !watchLink || !message || !buttons.length) return;

  const episodes = buttons.map(button => ({
    button,
    id: button.dataset.podcastEpisode,
    title: button.querySelector('strong').textContent.trim()
  })).filter(episode => /^[A-Za-z0-9_-]{11}$/.test(episode.id));
  if (!episodes.length) return;

  let selected = episodes[0];
  let iframe = null;

  function selectEpisode(episode) {
    selected = episode;
    title.textContent = episode.title;
    loadButton.setAttribute('aria-label', 'Load the YouTube player for ' + episode.title);
    watchLink.href = 'https://www.youtube.com/watch?v=' + episode.id;
    watchLink.setAttribute('aria-label', 'Watch ' + episode.title + ' on YouTube');
    for (const row of episodes) {
      row.button.setAttribute('aria-pressed', String(row === episode));
      row.button.querySelector('.episode-action').textContent = row === episode ? 'Selected' : 'Listen here';
    }
  }

  function loadEpisode(episode = selected) {
    selectEpisode(episode);
    if (iframe && iframe.dataset.videoId === episode.id) return;

    if (!iframe) {
      iframe = document.createElement('iframe');
      iframe.id = 'podcast-iframe';
      iframe.referrerPolicy = 'strict-origin-when-cross-origin';
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      iframe.allowFullscreen = true;
      iframe.addEventListener('load', () => {
        message.textContent = 'If ' + selected.title + ' cannot play here, use Watch on YouTube.';
      });
      iframe.addEventListener('error', () => {
        message.textContent = 'The player could not load. Use Watch on YouTube, or close the player and try again.';
      });
      slot.append(iframe);
    }

    placeholder.hidden = true;
    closeButton.hidden = false;
    iframe.dataset.videoId = episode.id;
    iframe.title = 'Thinking Clearer with Lincoln — ' + episode.title;
    const url = new URL('https://www.youtube-nocookie.com/embed/' + episode.id);
    url.searchParams.set('playsinline', '1');
    url.searchParams.set('rel', '0');
    url.searchParams.set('autoplay', '0');
    iframe.src = url.href;
    message.textContent = 'Loading ' + episode.title + '. Use the player’s play control when it is ready.';
  }

  loadButton.addEventListener('click', () => loadEpisode());
  for (const episode of episodes) episode.button.addEventListener('click', () => loadEpisode(episode));
  closeButton.addEventListener('click', () => {
    iframe?.remove();
    iframe = null;
    placeholder.hidden = false;
    closeButton.hidden = true;
    message.textContent = 'Player closed. Load an episode whenever you’re ready.';
    loadButton.focus();
  });
  selectEpisode(selected);
})();
