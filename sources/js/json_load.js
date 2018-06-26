$(document).ready(function(){
    var blog2dispay=[]
    $('[id="blog_selector"]').click(function(){
        blog2dispay=$(this).attr('name')
        $.getJSON( "./sources/ajax/blog_content.json", function( data ) {
            $(".content_blog").html(data[blog2dispay]["Content"])
        });
    });
});

$.getJSON( "./sources/ajax/blog_content.json", function( data ) {
    var titles = [];
    var blogcont = [];
    var counter=0
    $.each( data, function( key, val ) {
        titles = "<div id='blog_selector' name='" + key + "'>" + "<div>"+ val["Title"] + "</div>" + "<p>" + val["Date"] + "</p></div>";
        if (counter==0){
            blogcont = val["Content"];
            counter = 1 
        }
        else{
            blogcont=''
        }
        $(".left_column").append(titles)
        $(".content_blog").append(blogcont)
    });
});

$.getJSON( "./sources/ajax/tools_content.json", function( data ) {
    count = Object.keys(data).length;
    var titles = [];
    var texttools = [];
    var counter=0
    key="tool_"+randomFromTo(1, count)
    val=data[key]
    titles = "<div id='background_tool' name='" + key + "'>" + "<div>"+ val["title"] + "</div>" + "<p>" + val["text"] + "</p></div>";
    $('.tools_content').css({'height':100+'vh','width':100+'vw','background-color':val["background_color"]});
    
    $(".tools_content").append(titles)
    pathstr=val["figure"]
    filestr=pathstr.split("/")
    filenamestr=filestr[filestr.length-1]
    format=filenamestr.split(".")
    if (format[format.length-1]=='mp4'){
        background= "<div class='video_tools'> <video poster='' playsinline autoplay muted loop><source src='"+val["figure"]+"' type='video/mp4'></video></div>"
        
    }
    else{
        background=''
    }
    
    $(".tools_content").append(background)
    var percent_bar = 60.0/count
    
    $.each( data, function( key, val ) {
        if (counter==0){
            $(".slidemenu_tools").append('<span class="left"></span><li style="margin-bottom:1.5vh;width:'+percent_bar+'%" class="tool_list '+key+'" name="'+key+'"></li>')
            counter=counter+1
        }
        else if (counter == count-1){
            $(".slidemenu_tools").append('<li style="margin-bottom:1.5vh;width:'+percent_bar+'%" class="tool_list '+key+'" name="'+key+'"></li><span class="right"></span>')
        }
        else{
            $(".slidemenu_tools").append('<li style="margin-bottom:1.5vh;width:'+percent_bar+'%" class="tool_list '+key+'" name="'+key+'"></li>')
            counter=counter+1
        }
    });  
    $("."+key).css({'background-color':val["bar_color"]})
});

