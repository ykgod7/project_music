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
                for (let i = 0; i < 5; i++) {	//반복문을 쓰는 이유는 track 내에 이름을 모두 출력하기 위함. '3' 위치에 나중에 넣을 변수 : musicList.length
                    let albumTitle = musicList[i]["name"]
                    let albumArtist = musicList[i]["artist"]
                    let albumUrl = musicList[i]["url"]
                    //console.log(albumTitle, albumArtist)
                    /////// 썸네일 동영상 ID값을 가져오기 위한 ajax 추가 영역

                    //let apikey = "AIzaSyB1nDzwhecsIlKfq3LmBHxRoO6x6yVn7iQ";   //이문열
                    let apikey = "AIzaSyCfuyiH7W-NJQTVdOjt8UC9SYoUZJegnOk";   //장경진
                    //let apikey = "AIzaSyCXqe22SwyypvUQojB9UIjONWPqfwyWNs8"  //황지현
                    let q_keyword = albumTitle + ' ' + albumArtist + ' official'
                    console.log(q_keyword);
                    (function(i){
                        $.ajax({
                            url:'https://www.googleapis.com/youtube/v3/search',
                            type:'get',
                            dataType:'json',
                            data:{part:'id',key:apikey,q:q_keyword, maxResults:1, type:'video',videoEmbeddable:'true'},
                            success:function (datalist){
                                varId = datalist.items[0].id.videoId;
                                //console.log(videoId);
                                //console.log('순서 확인용 (안)'+varId)
                                var html = '';
                                html += '<div class="container" style="text-align:center; height:240px">' +
                                    '<div class="container" style="display:inline-block; text-align:center; border-radius: 15%; margin-top:20px; width:360px; height:220px; background-color: #BECDFF;">' +
                                    '<iframe style="margin-top:20px;" width="320" height="180" src="https://img.youtube.com/vi/'+varId+'/mqdefault.jpg"></iframe><br>' +
                                    '<a href="music/musicvideo/">' +
                                    albumArtist + ' : ' + albumTitle +
                                    '</a></div></div>'
                                $("#list").append(html);
                            },
                            error : function(err) {
                                console.log(err)
                            }
                        })
                    })(i);
                }
            },
            error : function() {
                alert('검색 실패')
            }
        })
    })
})