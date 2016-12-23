// 兼容手机页面
function setPageSize() {
    var w = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    if (w < 800) {
        $(".header").hide();
        $("#rtd-search-form").hide();
        $(“.top-title”).css({“margin-top”: “90px”, “margin-bottom”: “-32px”});
        $("html").css({"overflow-x":"hidden", "width":w+"px"});
        if ($("#phone-head-menu").length <= 0) {
            var menu = ‘\
            <select id="phone-head-menu" onchange=mbar(this) style="position: absolute; top: 14px; right: 6px;font-weight: 600; -webkit-box-shadow: 0 3px 0 #ccc,0 -1px #fff inset; -moz-box-shadow: 0 3px 0 #ccc,0 -1px #fff inset; box-shadow: 0 3px 0 #ccc,0 -1px #fff inset; background: #1b75bb; color: #fff; font-size: 14px; border: none; outline: none;display: inline;-webkit-appearance: none;-moz-appearance: none;cursor: pointer;-webkit-border-radius: 0px;-moz-border-radius: 0px;border-radius: 0px;width: 62px;">\
                <option>菜单 +</option>\
                <option value="/jpush/guideline/intro/">JPush</option>\
                <option value="/janalytics/guideline/intro/">JAnalytics</option>\
                <option value="/jmessage/guideline/jmessage_guide/">JMessage</option>\
                <option value="/jsms/guideline/JSMS_guide/">JSMS</option>\
            </select>';
            $(".container-fluid").append(menu);
        }
    } else {
        $(".header").show();
        $("#rtd-search-form").show();
        $("html").removeAttr("style");
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

    $(".top-image-nav-div").mouseover(function() {
        $(this).css("border-color", "#1b75bb");
        var src=$(this).children().children().children().attr("src");
        var file_dir=src.substr(0,15);
        var file_id=src.substr(15,1);
        var id=parseInt(file_id);
        id=id+1;
        var id_string=id.toString();
        var new_src=file_dir+id_string+".png";
        //console.log(file_dir);
        //console.log(file_id);
        //console.log(new_src);
        $(this).children().children().children().attr("src",new_src);
    });
    $(".top-image-nav-div").mouseout(function() {
        $(this).css("border-color", "#e5e5e5");
        var src=$(this).children().children().children().attr("src");
        var file_dir=src.substr(0,15);
        var file_id=src.substr(15,1);
        var id=parseInt(file_id);
        id=id-1;
        var id_string=id.toString();
        var new_src=file_dir+id_string+".png";
        //console.log(file_dir);
        //console.log(file_id);
        //console.log(new_src);
        $(this).children().children().children().attr("src",new_src);
    });
});
