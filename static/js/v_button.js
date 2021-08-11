$(function(){
    $(Document).on('click', '.result_btn', function(){
        //alert('뮤비 버튼 진입')
        //alert($('.v_button').attr('data-videoCd')+' '+encodeURI($('.v_button').attr('data-videoTitle'))+' '+encodeURI($('.v_button').attr('data-videoArtist')))
        document.location.href = '/music/musicvideo/'+$('.result_btn').attr('data-videoCd')+'/'+encodeURI($('.result_btn').attr('data-videoTitle'))+'/'+encodeURI($('.result_btn').attr('data-videoArtist'))+'/'
    })
})