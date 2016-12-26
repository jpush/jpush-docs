// 修改兼容手机 start
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
        if ($("#phone-head-menu").length <= 0) {
            var menu = '\
            <select id="phone-head-menu" onchange=mbar(this) style="position: absolute; top: 14px; font-weight: 600; -webkit-box-shadow: 0 3px 0 #ccc,0 -1px #fff inset; -moz-box-shadow: 0 3px 0 #ccc,0 -1px #fff inset; box-shadow: 0 3px 0 #ccc,0 -1px #fff inset; background: #1b75bb; color: #fff; font-size: 14px; border: none; outline: none;display: inline;-webkit-appearance: none;-moz-appearance: none;cursor: pointer;-webkit-border-radius: 0px;-moz-border-radius: 0px;border-radius: 0px;width: 62px;">\
                <option>菜单 +</option>\
                <option value="/jpush/guideline/intro/">JPush</option>\
                <option value="/janalytics/guideline/intro/">JAnalytics</option>\
                <option value="/jmessage/guideline/jmessage_guide/">JMessage</option>\
                <option value="/jsms/guideline/JSMS_guide/">JSMS</option>\
            </select>';
            $(".container-fluid").append(menu);
            $("#phone-head-menu").css({"left": (w-100)+"px"});
        }
    } else {
        $("#navbar-left").show();
        $(".header").show();
        $("#rtd-search-form").show();
        $(".rst-content").closest(".col-lg-8").removeAttr("style");
        $("html").removeAttr("style");
        if ($("#nav_more").length > 0) {
            $("#nav_more").remove();
        }
        if ($("#phone-head-menu").length > 0) {
            $("#phone-head-menu").remove();
        }
    }
}

// 手机端菜单选择
function mbar(sobj) {
    var docurl = sobj.options[sobj.selectedIndex].value;
    if (docurl != "") {
        open(docurl, '_self');
        sobj.selectedIndex = 0;
        sobj.blur();
    }
}

$(document).ready(function() {

    // 监听窗口大小是否变化
    setPageSize();
    $(window).resize(function(){
        setPageSize();
    });
    // 修改兼容手机 end

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
