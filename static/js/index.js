///top100리스트
const popup_width = 720;
const popup_height = 600;
const popup_x = (window.screen.width / 2) - (popup_width / 2);
const popup_y = (window.screen.height / 2) - (popup_height / 2);

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
        error : function() {
            alert('실패했어요~')
        }
    })
    })
})

$(function(event) {
    $('[id=list_btn]').on('click',function(event) {
    $.ajax({
        url:'/music/list_rank/',
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
        url:'/music/list_rank/',
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