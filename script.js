// Smooth scroll for anchor links
document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector(".site-header");
  const navLinks = document.querySelectorAll(".header-nav a[href^='#']");
  const sections = Array.from(document.querySelectorAll("main section[id]"));
  const navToggle = document.querySelector(".nav-toggle");
  const headerInner = document.querySelector(".header-inner");

  function getHeaderOffset() {
    return header ? header.offsetHeight + 8 : 0;
  }

  function smoothScrollTo(targetId) {
    const el = document.getElementById(targetId);
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const offsetTop = window.scrollY + rect.top - getHeaderOffset();

    window.scrollTo({
      top: offsetTop,
      behavior: "smooth",
    });
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href") || "";
      if (!href.startsWith("#")) return;
      const targetId = href.slice(1);
      e.preventDefault();
      smoothScrollTo(targetId);
      if (headerInner.classList.contains("nav-open")) {
        headerInner.classList.remove("nav-open");
      }
    });
  });

  // Intersection observer to highlight active nav item
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const id = entry.target.getAttribute("id");
          if (!id) return;
          const link = document.querySelector(`.header-nav a[href="#${id}"]`);
          if (!link) return;
          if (entry.isIntersecting) {
            navLinks.forEach((l) => l.classList.remove("active"));
            link.classList.add("active");
          }
        });
      },
      {
        rootMargin: "-55% 0px -40% 0px",
        threshold: 0.05,
      }
    );

    sections.forEach((section) => observer.observe(section));
  }

  // Mobile nav toggle
  if (navToggle && headerInner) {
    navToggle.addEventListener("click", () => {
      headerInner.classList.toggle("nav-open");
    });
  }
});

