$(function(event){
    $('#rank_wheel').on('mousewheel',function(event){
        //alert('진입!')
        event.preventDefault();
        var m = event.originalEvent.wheelDelta;
        var sb = $('#rank_wheel').height();

        if(m > 1 && scrollEvent == false && count >= 1){
            console.log(count);
            scrollEvent = true;
            count--;
            $('#rank_wheel').stop().animate({scrollTop:sb*count}, {
                duration:300, complete: function(){
                    scrollEvent = false;
                    }
                });
        }
        else if(m < 1 && scrollEvent == false && count < 3){
            console.log(count);
            scrollEvent = true;
            count++;
            $('#rank_wheel').stop().animate({scrollTop:sb*count}, {
                duration:300, complete: function(){
                    scrollEvent = false;
                    }
                });
        }
    });
})