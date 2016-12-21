// 兼容手机页面
function setPageSize() {
    var w = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    if (w < 800) {
        $("#navbar-left").hide();
        $(".header").hide();
        $("#rtd-search-form").hide();
        $(".rst-content").closest(".col-lg-8").width(w-30);
        $("html").css({"overflow-x":"hidden", "width":w+"px"});
    } else {
        $("#navbar-left").show();
        $(".header").show();
        $("#rtd-search-form").show();
        $(".rst-content").closest(".col-lg-8").removeAttr("style");
        $("html").removeAttr("style");
    }
}

$(document).ready(function() {

    // 兼容手机页面
    setPageSize();
    $(window).resize(function(){
        setPageSize();
    });

    url = window.location.href;
    if(url.indexOf("jpush")>0){
        $("#jpush-top").css("border-bottom", "solid 3px #1b75bb");
    }
    //console.log(url.indexOf("jpush"));

        url = window.location.href;
    if(url.indexOf("jmessage")>0){
        $("#jmessage-top").css("border-bottom", "solid 3px #1b75bb");
    }
    //console.log(url.indexOf("jmessage"));

        url = window.location.href;
    if(url.indexOf("jsms")>0){
        $("#jsms-top").css("border-bottom", "solid 3px #1b75bb");
    }
    //console.log(url.indexOf("jmessage"));

            url = window.location.href;
    if(url.indexOf("janalytics")>0){
        $("#janalytics-top").css("border-bottom", "solid 3px #1b75bb");
    }
    //console.log(url.indexOf("jmessage"));


    $("li .current").parent().css("display", "block");
    $("li .current").parent().siblings().css("display", "block");
    $("li .current").parent().children(".subnavli").children().children("a").children().children("img").attr("src", "/img/icon/down.png");


    $(".subnavul li").mouseover(function() {
        $(this).css("background-color", "#eeeeee");
        $("li .current").css("background-color", "#1d75bb");
    });

    $(".subnavul li").mouseout(function() {
        $(this).css("background-color", "#f8f8f8");
        $("li .current").css("background-color", "#1d75bb");
    });

    $(".download-icon").mouseover(function() {
        $(this).css("background-color", "#666666");
        $(this).children().css("color", "#FFFFFF");
    });

    $(".download-icon").mouseout(function() {
        $(this).css("background-color", "#f8f8f8");
        $(this).children().css("color", "#1d75bb");
    });

    $(".download-icon").click(function() {
        var url = $(this).children().attr("href");
        window.location.href = url;
    });

    $(".subnavli").click(function() {
        if ($(this).siblings().css("display") == "block") {
            //alert("yes");
            $(this).siblings().css("display","none");
            $(this).children().children().children().children().attr("src", "/img/icon/right.png");
            //$("li .current").parent().children().children("div").children("a").children("img").attr("src", "/img/icon/right.png");
            //var url = $(this).parent().parent().parent().children().first().children().children().children().children().attr("href");
            //alert(url);
            //window.location.href = "http://192.168.9.74/jpush/";
        } else {
            var url = $(this).next().children().attr("href");
            //alert("no");
            window.location.href = url;
            $("li .current").parent().css("display", "block");
            $("li .current").parent().siblings().css("display", "block");
            $("li .current").parent().children().children("div").children("a").children("img").attr("src", "/img/icon/down.png");
        }
    });
});
