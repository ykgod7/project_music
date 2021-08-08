$(function(){
    $(Document).on('click', '.v_button', function(){
        //alert('뮤비 버튼 진입')
        alert($('.v_button').attr('data-videoCd'))
        document.location.href = '/music/musicvideo/'+$('.v_button').attr('data-videoCd')+'/'+encodeURI($('.v_button').attr('data-videoTitle'))+'/'+encodeURI($('.v_button').attr('data-videoArtist'))+'/'
    })
})