(function ($) {
    "use strict";

    /*****************************
     * Commons Variables
     *****************************/
    var $window = $(window),
        $body = $('body');

    /****************************
     * Sticky Menu
     *****************************/
    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll < 100) {
            $(".sticky-header").removeClass("sticky");
        } else {
            $(".sticky-header").addClass("sticky");
        }
    });

    /*****************************
     * Off Canvas Function
     *****************************/
    (function () {
        var $offCanvasToggle = $('.offcanvas-toggle'),
            $offCanvas = $('.offcanvas'),
            $offCanvasOverlay = $('.offcanvas-overlay'),
            $mobileMenuToggle = $('.mobile-menu-toggle');
        $offCanvasToggle.on('click', function (e) {
            e.preventDefault();
            var $this = $(this),
                $target = $this.attr('href');
            $body.addClass('offcanvas-open');
            $($target).addClass('offcanvas-open');
            $offCanvasOverlay.fadeIn();
            if ($this.parent().hasClass('mobile-menu-toggle')) {
                $this.addClass('close');
            }
        });
        $('.offcanvas-close, .offcanvas-overlay').on('click', function (e) {
            e.preventDefault();
            $body.removeClass('offcanvas-open');
            $offCanvas.removeClass('offcanvas-open');
            $offCanvasOverlay.fadeOut();
            $mobileMenuToggle.find('a').removeClass('close');
        });
    })();


    /**************************
     * Offcanvas: Menu Content
     **************************/
    function mobileOffCanvasMenu() {
        var $offCanvasNav = $('.offcanvas-menu'),
            $offCanvasNavSubMenu = $offCanvasNav.find('.mobile-sub-menu');

        /*Add Toggle Button With Off Canvas Sub Menu*/
        $offCanvasNavSubMenu.parent().prepend('<div class="offcanvas-menu-expand"></div>');

        /*Category Sub Menu Toggle*/
        $offCanvasNav.on('click', 'li a, .offcanvas-menu-expand', function (e) {
            var $this = $(this);
            if ($this.attr('href') === '#' || $this.hasClass('offcanvas-menu-expand')) {
                e.preventDefault();
                if ($this.siblings('ul:visible').length) {
                    $this.parent('li').removeClass('active');
                    $this.siblings('ul').slideUp();
                    $this.parent('li').find('li').removeClass('active');
                    $this.parent('li').find('ul:visible').slideUp();
                } else {
                    $this.parent('li').addClass('active');
                    $this.closest('li').siblings('li').removeClass('active').find('li').removeClass('active');
                    $this.closest('li').siblings('li').find('ul:visible').slideUp();
                    $this.siblings('ul').slideDown();
                }
            }
        });
    }
    mobileOffCanvasMenu();

    /************************************************
     * Nice Select
     ***********************************************/
    $('select').niceSelect();


    /*************************
     *   Hero Slider Active
     **************************/
    var heroSlider = new Swiper('.hero-slider-active.swiper-container', {
        slidesPerView: 1,
        speed: 1500,
        watchSlidesProgress: true,
        loop: true,
        autoplay: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },

    });


    /****************************************
     *   Product Slider Active - 4 Grids 1 Row
     *****************************************/
    var default_slider = new Swiper('.default-slider .swiper-container', {
        slidesPerView: 4,
        spaceBetween: 45,
        speed: 1500,
        loop: true,
        autoplay: true,
        navigation: {
            nextEl: '.default-arrow .swiper-button-next',
            prevEl: '.default-arrow .swiper-button-prev',
        },

        breakpoints: {

            0: {
                slidesPerView: 1,
            },
            576: {
                slidesPerView: 2,

            },
            768: {
                slidesPerView: 2,
            },
            992: {
                slidesPerView: 3,
            },
            1200: {
                slidesPerView: 3,
            },
            1800: {
                slidesPerView: 4,
            }

        }
    });


    /****************************************
     *   Client Logo - 6 Grids 1 Row
     *****************************************/
    var client_logo_slider = new Swiper('.client-logo-slider .swiper-container', {
        slidesPerView: 6,
        autoplay: true,
        speed: 1500,
        loop: true,

        breakpoints: {

            0: {
                slidesPerView: 2,
            },
            576: {
                slidesPerView: 3,
            },
            768: {
                slidesPerView: 4,
            },
            992: {
                slidesPerView: 5,
            },
            1200: {
                slidesPerView: 6,
            },
            1800: {
                slidesPerView: 6,
            }

        }
    });

    /****************************************
     *   Blog Feed - 2 Grids 1 Row
     *****************************************/
    var blog_feed_slider = new Swiper('.blog-feed-slider .swiper-container', {
        slidesPerView: 2,
        spaceBetween: 45,
        speed: 1500,
        loop: true,
        autoplay: true,
        breakpoints: {

            0: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 2,
                spaceBetween: 20,
            },
            992: {
                slidesPerView: 2,
                spaceBetween: 30,
            },
            1200: {
                slidesPerView: 1,
            },
            1400: {
                slidesPerView: 2,
            }

        }
    });


    /************************************************
     * Counter Up
     ***********************************************/
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

    /************************************************
     * Video  Popup
     ***********************************************/
    $('.video-play-btn').venobox();

    /************************************************
     * Scroll Top
     ***********************************************/
    $('body').materialScrollTop();


    /************************************************
     * Product Grid Pagination
     * Uses pure CSS classes + Isotope's hide() API to avoid display:none collapse
     ***********************************************/
    $('.projects-wrapper').imagesLoaded(function () {
        var $grid = $('.projects-wrapper').isotope({
            itemSelector: '.filtr-item',
            percentPosition: true,
            masonry: {
                columnWidth: '.grid-sizer'
            }
        });

        var ITEMS_PER_PAGE = 12;
        var currentPage = 1;
        var currentFilter = '';  // empty string = show all

        function getFilteredItems() {
            var $all = $grid.find('.filtr-item');
            return currentFilter ? $all.filter('.' + currentFilter) : $all;
        }

        function applyPage() {
            var $all = $grid.find('.filtr-item');
            var $filtered = getFilteredItems();
            var totalPages = Math.ceil($filtered.length / ITEMS_PER_PAGE);

            if (currentPage > totalPages && totalPages > 0) currentPage = totalPages;
            if (currentPage < 1) currentPage = 1;

            var start = (currentPage - 1) * ITEMS_PER_PAGE;
            var end = start + ITEMS_PER_PAGE;

            // Mark which items should be visible this page
            $all.removeClass('on-page');
            $filtered.slice(start, end).addClass('on-page');

            // Use Isotope's own filter - avoids the display:none height-collapse issue
            $grid.isotope({ filter: '.on-page' });

            renderPagination(totalPages);
        }

        function renderPagination(totalPages) {
            var $p = $('#product-pagination');
            if (!$p.length) return;
            $p.empty();
            if (totalPages <= 1) return;

            var prevDisabled = (currentPage === 1) ? ' disabled' : '';
            var nextDisabled = (currentPage === totalPages) ? ' disabled' : '';

            $p.append('<button class="page-btn prev' + prevDisabled + '"><i class="icofont-rounded-left"></i></button>');

            for (var i = 1; i <= totalPages; i++) {
                var activeClass = (i === currentPage) ? ' active' : '';
                $p.append('<button class="page-btn num' + activeClass + '" data-page="' + i + '">' + i + '</button>');
            }

            $p.append('<button class="page-btn next' + nextDisabled + '"><i class="icofont-rounded-right"></i></button>');
        }

        function scrollUp() {
            var top = $('.projects-gallery-filter-nav').offset().top - 80;
            $('html, body').animate({ scrollTop: top }, 400);
        }

        // Set initial page after Isotope finishes layout
        setTimeout(applyPage, 300);

        // Category filter buttons
        $('.projects-gallery-filter-nav').on('click', 'button', function () {
            var raw = $(this).attr('data-filter') || '*';
            currentFilter = (raw === '*') ? '' : raw.replace(/^\./, '');
            currentPage = 1;
            applyPage();
            $(this).siblings('.active').removeClass('active');
            $(this).addClass('active');
        });

        // Pagination: page number
        $(document).on('click', '#product-pagination .page-btn.num', function () {
            currentPage = parseInt($(this).attr('data-page'), 10);
            applyPage();
            scrollUp();
        });

        // Pagination: previous
        $(document).on('click', '#product-pagination .page-btn.prev:not(.disabled)', function () {
            currentPage--;
            applyPage();
            scrollUp();
        });

        // Pagination: next
        $(document).on('click', '#product-pagination .page-btn.next:not(.disabled)', function () {
            currentPage++;
            applyPage();
            scrollUp();
        });
    });


        /************************************************
    * Hash Link Scroll To Top Prevent
    ***********************************************/
    $('a[href="#"]').on('click', (function (e) {
        e.preventDefault ? e.preventDefault() : e.returnValue = false;
    }));


})(jQuery);
