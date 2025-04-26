document.addEventListener('DOMContentLoaded', () => {
    // Toggle “selected” on click for cards, badges, inline items & table rows
    document.querySelectorAll('.grid-item, .badge-item, .inline-item, .table-row')
      .forEach(el => el.addEventListener('click', () => el.classList.toggle('selected')));
  });
  