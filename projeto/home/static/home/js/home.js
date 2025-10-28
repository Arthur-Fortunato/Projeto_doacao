document.addEventListener('DOMContentLoaded', () => {
  const userMenu = document.querySelector('.user-menu');
  if (userMenu) {
    const button = userMenu.querySelector('.user-btn');
    button.addEventListener('click', () => {
      userMenu.classList.toggle('active');
    });

    document.addEventListener('click', (e) => {
      if (!userMenu.contains(e.target)) {
        userMenu.classList.remove('active');
      }
    });
  }
});
