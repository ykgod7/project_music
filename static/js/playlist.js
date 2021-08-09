
$(function (event) {
    $("#modal_trigger").leanModal({
        top: 100,
        overlay: 0.5,
        closeButton: ".modal_close",
        addButton: ".modal_add",
    });
    login()
});

function login() {
    $('#login_submit').click(function () {
        var csrf_token = $('[name=csrfmiddlewaretoken]').val();
        console.log($('#username').val())
        console.log(1)
        console.log($('#password').val())
        console.log(2)
        console.log($('.popuplogin_form').serialize())
        $.ajax({
            url: '/user/popuplogin/',
            type: 'post',
            dataType: 'json',
            headers: {
                'X-CSRFToken': csrf_token
            },
            data: $('.popuplogin_form').serialize(),
            success: function (response) {
                if (response.result == 'true') {
                    location.reload()
                    console.log('로그인됨')
                } else {
                    console.log('로그인 안됨')
                    console.log(response.con)
                    console.log(22)
                    $('err_msg').attr('display', '')
                }

            },
            error: function (response) {
                alert('뭔가 잘못됨')
                alert(response.result)
            }
        })
    })
};