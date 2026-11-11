// OwnVoice Studio: mobile navigation toggle, header state, footer year,
// and reveal on scroll. No libraries, no tracking, no cookies.
(function () {
  document.documentElement.classList.add("js");

  var header = document.querySelector(".site-header");
  var onScroll = function () {
    if (header) { header.classList.toggle("scrolled", window.scrollY > 24); }
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  var year = document.querySelector("[data-year]");
  if (year) { year.textContent = String(new Date().getFullYear()); }

  var reveals = document.querySelectorAll(".reveal");
  if (reveals.length) {
    if ("IntersectionObserver" in window &&
        !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1 });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add("in"); });
    }
  }
})();
