$(document).ready(function() {
    // Highlight.js
    // hljs.initHighlightingOnLoad();
    $('table').addClass('table table-striped table-hover');

    // Improve the scrollspy behaviour when users click on a TOC item.
    $(".bs-sidenav a").on("click", function() {
        var clicked = this;
        setTimeout(function() {
            var active = $('.nav li.active a');
            active = active[active.length - 1];
            if (clicked !== active) {
                $(active).parent().removeClass("active");
                $(clicked).parent().addClass("active");
            }
        }, 50);
    });

});


$('body').scrollspy({
    target: '.bs-sidebar',
});

/* Toggle the `clicky` class on the body when clicking links to let us
   retrigger CSS animations. See ../css/base.css for more details. */
$('a').click(function(e) {
    $('body').toggleClass('clicky');
});

/* Prevent disabled links from causing a page reload */
$("li.disabled a").click(function() {
    event.preventDefault();
});

$('.demo-download').hover(function(){
	$(this).children(".code").children(".download-text").css('visibility', 'visible');
	$(this).children(".apk").css('border', 'none');
	$(this).css('border', '1px solid #ccc').css('border-radius', '2px')
}, function(){
	$(this).children(".code").children(".download-text").css('visibility', 'hidden');
	$(this).children(".apk").css('border', '1px solid #ccc').css('border-radius', '2px')
	$(this).css('border', 'none');
});