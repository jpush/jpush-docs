$(document).ready(function() {
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
