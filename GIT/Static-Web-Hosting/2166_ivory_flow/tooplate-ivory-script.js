/* JavaScript Document

Tooplate 2166 Ivory Flow
    
https://www.tooplate.com/view/2166-ivory-flow

*/

(function() {
  'use strict';

  /* ── IntersectionObserver — Scroll Reveal ── */
  var revealEls = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window) {
    var revealObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    revealEls.forEach(function(el) { revealObs.observe(el); });

    /* 3-second safety fallback for iframe previews */
    setTimeout(function() {
      revealEls.forEach(function(el) { el.classList.add('visible'); });
    }, 3000);
  } else {
    revealEls.forEach(function(el) { el.classList.add('visible'); });
  }

  /* ── Timeline items — fade in at center viewport ── */
  var timelineItems = document.querySelectorAll('[data-timeline]');

  if ('IntersectionObserver' in window) {
    var timelineObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
        } else {
          entry.target.classList.remove('in-view');
        }
      });
    }, { rootMargin: '-30% 0px -30% 0px' });

    timelineItems.forEach(function(el) { timelineObs.observe(el); });

    setTimeout(function() {
      timelineItems.forEach(function(el) { el.classList.add('in-view'); });
    }, 3000);
  } else {
    timelineItems.forEach(function(el) { el.classList.add('in-view'); });
  }

  /* ── Active pill nav link ── */
  var pillLinks = document.querySelectorAll('.pill-nav a');
  var sections = document.querySelectorAll('.canvas-section');

  if ('IntersectionObserver' in window) {
    var navObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var id = entry.target.id;
          pillLinks.forEach(function(link) {
            link.classList.toggle('active', link.getAttribute('href') === '#' + id);
          });
        }
      });
    }, { threshold: 0.4 });

    sections.forEach(function(sec) {
      if (sec.id) navObs.observe(sec);
    });
  }

  /* ── Mouse-following Buy Circle (LERP) ── */
  var buyCircle = document.getElementById('buyCircle');
  var productZone = document.getElementById('productImageZone');
  var mouseX = 0, mouseY = 0, circleX = 0, circleY = 0;
  var isOverProduct = false;
  var rafId = null;

  if (productZone && buyCircle && window.innerWidth > 768) {
    productZone.addEventListener('mouseenter', function() {
      isOverProduct = true;
      buyCircle.classList.add('visible');
      if (!rafId) lerpLoop();
    });

    productZone.addEventListener('mouseleave', function() {
      isOverProduct = false;
      buyCircle.classList.remove('visible');
    });

    productZone.addEventListener('mousemove', function(e) {
      mouseX = e.clientX;
      mouseY = e.clientY;
    });

    function lerpLoop() {
      circleX += (mouseX - circleX) * 0.12;
      circleY += (mouseY - circleY) * 0.12;
      buyCircle.style.left = circleX - 60 + 'px';
      buyCircle.style.top = circleY - 60 + 'px';

      if (isOverProduct || Math.abs(mouseX - circleX) > 0.5) {
        rafId = requestAnimationFrame(lerpLoop);
      } else {
        rafId = null;
      }
    }
  }

  /* ── Lookbook: Momentum drag + Arrow buttons ── */
  var track = document.querySelector('.lookbook-track');
  if (track) {
    var isDragging = false;
    var startX = 0;
    var scrollStart = 0;
    var velX = 0;
    var lastX = 0;
    var lastTime = 0;
    var momentumId = null;

    track.addEventListener('mousedown', function(e) {
      cancelMomentum();
      isDragging = true;
      startX = e.clientX;
      lastX = e.clientX;
      scrollStart = track.scrollLeft;
      lastTime = Date.now();
      velX = 0;
      track.classList.add('is-dragging');
    });

    document.addEventListener('mousemove', function(e) {
      if (!isDragging) return;
      e.preventDefault();
      var now = Date.now();
      var dt = now - lastTime;
      var dx = e.clientX - lastX;
      if (dt > 0) velX = dx / dt;
      lastX = e.clientX;
      lastTime = now;
      track.scrollLeft = scrollStart - (e.clientX - startX);
    });

    document.addEventListener('mouseup', function() {
      if (!isDragging) return;
      isDragging = false;
      track.classList.remove('is-dragging');
      startMomentum();
    });

    function startMomentum() {
      if (Math.abs(velX) < 0.1) return;
      var speed = -velX * 18;
      function step() {
        speed *= 0.94;
        if (Math.abs(speed) < 0.5) return;
        track.scrollLeft += speed;
        momentumId = requestAnimationFrame(step);
      }
      momentumId = requestAnimationFrame(step);
    }

    function cancelMomentum() {
      if (momentumId) {
        cancelAnimationFrame(momentumId);
        momentumId = null;
      }
    }

    /* Arrow buttons */
    var prevBtn = document.getElementById('lbPrev');
    var nextBtn = document.getElementById('lbNext');
    var cards = track.querySelectorAll('.lookbook-card');

    function getScrollStep() {
      return cards.length ? cards[0].offsetWidth + 28 : 400;
    }

    function smoothScroll(target) {
      cancelMomentum();
      var start = track.scrollLeft;
      var dist = target - start;
      var duration = 600;
      var startTime = null;

      function ease(t) {
        return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
      }

      function animate(now) {
        if (!startTime) startTime = now;
        var elapsed = now - startTime;
        var progress = Math.min(elapsed / duration, 1);
        track.scrollLeft = start + dist * ease(progress);
        if (progress < 1) requestAnimationFrame(animate);
      }

      requestAnimationFrame(animate);
    }

    if (prevBtn) prevBtn.addEventListener('click', function() {
      smoothScroll(track.scrollLeft - getScrollStep());
    });

    if (nextBtn) nextBtn.addEventListener('click', function() {
      smoothScroll(track.scrollLeft + getScrollStep());
    });
  }

  /* ── Hamburger ── */
  var hamburger = document.querySelector('.hamburger');
  var mobileNav = document.querySelector('.mobile-nav');
  var mobileLinks = document.querySelectorAll('.mobile-nav a');

  hamburger.addEventListener('click', function() {
    hamburger.classList.toggle('open');
    mobileNav.classList.toggle('open');
    document.body.style.overflow = mobileNav.classList.contains('open') ? 'hidden' : '';
  });

  mobileLinks.forEach(function(link) {
    link.addEventListener('click', function() {
      hamburger.classList.remove('open');
      mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  /* ── Smooth scroll for pill nav ── */
  pillLinks.forEach(function(link) {
    link.addEventListener('click', function(e) {
      var href = this.getAttribute('href');
      if (href && href.length > 1 && href.startsWith('#')) {
        e.preventDefault();
        var target = document.querySelector(href);
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();