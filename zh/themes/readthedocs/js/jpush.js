
// 兼容手机页面
function setPageSize() {
    var w = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    if (w < 800) {
        // 隐藏左侧导航
        $("#navbar-left").hide();
        // 隐藏头部导航
        $(".header").hide();
        // 隐藏搜索框
        $("#rtd-search-form").hide();
        // 设置内容宽度
        $(".rst-content").closest(".col-lg-8").width(w-30);
        $("html").css({"overflow-x":"hidden", "width":w+"px"});
        // 添加左侧导航
        var more = '<div id="nav_more" style="display: inline-block; position: absolute; top: 20px; left: 150px; color: #1b75bb;">>>></div>';
        if ($("#nav_more").length <= 0) {
            $(".container-fluid").append(more);
            $("#nav_more").show();
        }
        var mask = '<div id="my_mask" style="z-index: 99; pointer-events: none; position: fixed; top: 0; left: 0; bottom: 0; right: 0; background: rgba(0,0,0,.8);"></div>'
        $("#nav_more").on("click", function() {
            $("body").append(mask);
            $("#navbar-left").css({"z-index": 100}).show();
        });
    } else {
        $("#navbar-left").show();
        $(".header").show();
        $("#rtd-search-form").show();
        $(".rst-content").closest(".col-lg-8").removeAttr("style");
        $("html").removeAttr("style");
        if ($("#nav_more").length > 0) {
            $("#nav_more").remove();
        }
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

    $(".auto-download-icon").mouseover(function() {
        $(this).css("background-color", "#666666");
        $(this).children().css("color", "#FFFFFF");
    });

    $(".auto-download-icon").mouseout(function() {
        $(this).css("background-color", "#f8f8f8");
        $(this).children().css("color", "#1d75bb");
    });

    $(".auto-download-icon").click(function() {
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
