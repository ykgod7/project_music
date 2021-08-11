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
                //if(musicList.length==0){console.log(musicList)}
                for (let i = 0; i < 2; i++) {	//반복문을 쓰는 이유는 track 내에 이름을 모두 출력하기 위함. '3' 위치에 나중에 넣을 변수 : musicList.length
                    if(musicList.length==0){
                        var html = ''
                        html += '<div class="container" style="text-align:center; height:260px">' +
                            '<div class="container" style="display:inline-block; text-align:center; margin-top:20px; width:360px; height:240px; ">' +
                            '<iframe style="margin-bottom:10px;" width="320" height="180" src="https://img.youtube.com/vi/wnudr9qjrbA/mqdefault.jpg"></iframe><br>' +
                            '<h6>검색 결과가 없어요. 검색어를 다시 확인해주세요!</h6></div></div>'
                        $("#list").append(html);
                        break;
                    }
                    let albumTitle = musicList[i]["name"]
                    let albumArtist = musicList[i]["artist"]
                    let albumUrl = musicList[i]["url"]
                    //console.log(albumTitle, albumArtist)
                    /////// 썸네일 동영상 ID값을 가져오기 위한 ajax 추가 영역

                    //let apikey = "AIzaSyB1nDzwhecsIlKfq3LmBHxRoO6x6yVn7iQ";   //이문열
                    //let apikey = "AIzaSyCfuyiH7W-NJQTVdOjt8UC9SYoUZJegnOk";   //장경진
                    //let apikey = "AIzaSyCXqe22SwyypvUQojB9UIjONWPqfwyWNs8"  //황지현
                    let apikey = "AIzaSyBh6AzV_s_uLAXesssb6A67G6-nj4XKRaY"  //황지현 신규 키
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
                                albumTitleToEncoding = albumTitle.replace(/ /g, '%20')    /* 속성에 띄어쓰기 인식이 안 돼서 직접 encoding 시킨 후 보냄 */
                                //alert(albumTitleToEncoding)
                                var html = '';
                                html += '<div class="container" style="text-align:center; height:260px; margin-bottom:20px;">' +
                                    '<div class="container" style="display:inline-block; text-align:center; margin-top:10px; margin-bottom:10px;">' +
                                    '<iframe style="margin-bottom:10px;" width="320" height="180" src="https://img.youtube.com/vi/'+varId+'/mqdefault.jpg"></iframe><br>' +
                                    '<button type="button" class="result_btn" onclick="location.href=\'/music/musicvideo/'+varId+'/'+albumTitleToEncoding+'/'+albumArtist+'/\'">'+
                                    albumArtist + ' : ' + albumTitle +
                                    '</button></div></div>'
                                $("#list").append(html);
                            },
                            error : function(err) {
                                console.log(err)
                                console.log('샘플 videoId=BlackPink:Kill This Love')
                                //albumTitle = 'Kill This Love'
                                //albumArtist = 'Black Pink'
                                albumTitleToEncoding = albumTitle.replace(/ /g, '%20')    /* 속성에 띄어쓰기 인식이 안 돼서 직접 encoding 시킨 후 보냄 */
                                //alert(albumTitleToEncoding)
                                var html = '';
                                var varId = '2S24-y0Ij3Y';
                                html += '<div class="container" style="text-align:center; height:260px; margin-bottom:20px;">' +
                                    '<div class="container" style="display:inline-block; text-align:center; margin-top:10px; margin-bottom:10px;">' +
                                    '<iframe style="margin-bottom:10px;" width="320" height="180" src="https://img.youtube.com/vi/'+varId+'/mqdefault.jpg"></iframe><br>' +
                                    '<button type="button" class="result_btn" onclick="location.href=\'/music/musicvideo/'+varId+'/'+albumTitleToEncoding+'/'+albumArtist+'/\'">'+
                                    //'<button type="button" class="result_btn" data-videoCd='+varId+' data-videoTitle='+albumTitleToEncoding+' data-videoArtist='+albumArtist+'>' +
                                    albumArtist + ' : ' + albumTitle +
                                    '</button></div></div>'
                                $("#list").append(html);
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