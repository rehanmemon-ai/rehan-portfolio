(function () {
  try {
    var t = localStorage.getItem('theme');
    if (t === 'light') {
      document.documentElement.classList.remove('dark');
      document.documentElement.classList.add('light');
      var m = document.querySelector('meta[name="theme-color"]');
      if (m) m.setAttribute('content', '#f7f7f2');
    }
  } catch (e) {}
})();
