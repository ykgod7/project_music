$(function(event) {
    $('[id=search_btn]').on('click',function(event) {
    let keyword = $('#search_keyword').val()
    let apikey = "AIzaSyCfuyiH7W-NJQTVdOjt8UC9SYoUZJegnOk";
    $.ajax({
        url:'https://www.googleapis.com/youtube/v3/search',
        type:'get',
        dataType:'json',
        data:{part:'snippet',key:apikey,q:keyword, maxResults:6,type:'video',videoEmbeddable:'true'},
        success:function (data){
            $("#list").empty();
            $.each(data.items, function(i, item) {
                videoId = item.id.videoId;
                videoTitle = item.snippet.title;
                var html = '';
                html += '<div style="border-radius: 7%; justify-content: space-between, space-around; height:200px; width:180px; background-color: #5a5a5a; float: left; padding:10px; margin-right=10px;"><iframe width="150" height="150" src="https://www.youtube.com/embed/' + videoId +
                '"></iframe><br>' + videoTitle + '</div>'
                $("#list").append(html);
           });
        },
        error : function() {
            alert('실패했어요!')
        }
    })
    })
})

///top100리스트
$(function(event) {
    $('[id=top100_btn]').on('click',function(event) {
    $.ajax({
        url:'/music/music_rank/f_like',
        type:'get',
        dataType:'html',
        success:function(data) {
            $("#list").empty();
            $("#list").html(data);
        },
        error:function(request,status,error){
        alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
        }
    })
    })
})



$(function(event) {
    $('[id=list_btn]').on('click',function(event) {
    $.ajax({
        url:'/music/playlist_rank/l_like',
        type:'get',
        dataType:'html',
        success:function(data2) {
            $("#list").empty();
            $("#list").html(data2);
        },
        error : function() {
            alert('실패했어요!')
        }
    })
    })
})

window.onload = function(){
    $.ajax({
        url:'/music/playlist_rank/l_like',
        type:'get',
        dataType:'html',
        success:function(data2) {
            $("#list").empty();
            $("#list").html(data2);
        },
        error : function() {
            alert('실패했어요!')
        }
    })
};
