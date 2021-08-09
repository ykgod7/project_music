$(function(event) {
    $('[id=search_btn]').on('click',function(event) {
        let keyword = $('#search_keyword').val()
        let apikey = "AIzaSyCXqe22SwyypvUQojB9UIjONWPqfwyWNs8"
        // let apikey = "AIzaSyCfuyiH7W-NJQTVdOjt8UC9SYoUZJegnOk";
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
                    html += '<div style="border-radius: 7%; justify-content: start; height:200px; width:180px; background-color: #5a5a5a; float: left; padding:10px; margin-right=10px;">' +
                        '<iframe width="150" height="150" src="https://www.youtube.com/embed/' + videoId + '"></iframe><br>' + videoTitle + '</div>'
                    $("#list").append(html);
               });
            },
            error : function() {
                alert('실패했어요!')
            }
        })
    })
})