$(function(event) {
    $('#search_btn').on('click',function(event) {
        //alert('검색 버튼 인식');
        let keyword = $('#search_keyword').val()
        $.ajax({
            url: 'https://ws.audioscrobbler.com/2.0/?method=track.search&track='+keyword+'&api_key=0359193840e4b4c3350827519eb08dc1&format=json',
            type: 'GET',
            dataType: 'json',
            success: function (response){
                //alert('검색 진입')
                $("#list").empty();
                let musicList = response["results"]["trackmatches"]["track"];
                for (let i = 0; i < musicList.length; i++) {	//반복문을 쓰는 이유는 track 내에 이름을 모두 출력하기 위함
                    let albumTitle = musicList[i]["name"]
                    let albumArtist = musicList[i]["artist"]
                    let albumUrl = musicList[i]["url"]
                    //console.log(albumTitle, albumArtist)
                   // getMusicHtml(albumTitle, albumArtist)

                    var html = '';
                    html += '<div class="container" style="text-align:center; border-radius: 15%; height:180px; width:320px; background-color: #5a5a5a;'
                    if(i%2 == 0){
                        html += 'float: left;'
                    }
                    else{
                        html += 'float: right;'
                    }
                    html += 'padding:10px; margin-right=10px;"><a href="' + albumUrl + '">' +
                            albumArtist + ':' + albumTitle +
                            '</a></div>'
                    $("#list").append(html);
                };
            },
            error : function() {
                alert('실패했어요!')
            }
        })
    })
})