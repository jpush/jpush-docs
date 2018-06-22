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

//android
$('.download-btn-android').click(function(event) {
    if ($('.andorid-voice').is(':checked')) { //音视频地址
        $('.android-href').attr('href', 'https://www.jiguang.cn/downloads/server_sdk/im/JMRTC_Android');
    } else{
        $('.android-href').attr('href', 'https://www.jiguang.cn/downloads/sdk/im_android/');
    }
});

//ios
$('.download-btn-ios').click(function(event) {
    if ($('.ios-voice').is(':checked')) { //音视频地址
        $('.ios-href').attr('href', 'https://www.jiguang.cn/downloads/server_sdk/im/JMRTC_iOS');
    } else{
        $('.ios-href').attr('href', 'https://www.jiguang.cn/downloads/sdk/im_ios/');
    }
});