function addlist() {
    $("#add_list").click(function () {
        var value = $('#new_playlist').val()
        console.log(value)
        var cnt = $('#playlist').children().length
        var cname = 'check_list' + String(cnt + 1)
        console.log(cname)
        var ptag = "<p>"
        ptag += `<input type="checkbox" id=${cname} name="check_list" value="new" sytle="zoom:2.0"/>`
        ptag += `<label for=${cname} style="top: -3px; position: relative; font-size: 20pt">${value}</label>`
        ptag += "</p>"
        $('#playlist').append(ptag)
        $('#new_playlist').val('')
        $("#pl_add").removeClass('bi bi-dash-lg').addClass('bi bi-plus-lg')
        $(".hidden_playlist").hide();
        return false;
    });
};

function savelist() {
    $(document).on('click', '#modal_addd', function () {
        var csrf_token = $('[name=csrfmiddlewaretoken]').val();
        var id = $('input:checkbox[name="check_list"]:checked').attr('id')
        if ($('input:checkbox[name="check_list"]:checked').length == 0) {
            alert('재생목록을 선택해주세요')
        } else {
            $.ajax({
                url: $(location).attr('pathname'),
                type: 'post',
                dataType: 'json',
                headers: {
                    'X-CSRFToken': csrf_token
                },
                data: {
                    mp_name: $(`label[for=${id}]`).text(),
                    mp_key: $('input:checkbox[name="check_list"]:checked').val()
                },
                success: function (response) {
                    console.log(response.data)
                    $("#lean_overlay").click()
                },
                error: function () {
                    console.log(response.data)
                }
            })
        }
    })
};

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
                    console.log(response.con.password)
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


$(function (event) {
    // Calling Login Form
    $(".footer_title").click(function () {
        if ($(".hidden_playlist").css('display') == 'none') {
            $("#pl_add").removeClass('bi bi-plus-lg').addClass('bi bi-dash-lg')
            $(".hidden_playlist").show();
        } else {
            $(".hidden_playlist").hide();
            $("#new_playlist").val('')
            $("#pl_add").removeClass('bi bi-dash-lg').addClass('bi bi-plus-lg')
        }

        return false;
    });

    $(function (event) {
        $(document).on('click', 'input[type="checkbox"][name="check_list"]', function (event) {
            if ($(this).prop('checked')) {
                $('input[type="checkbox"][name="check_list"]').prop('checked', false);
                $(this).prop('checked', true);
                $('#add_btn').attr('src', "/static/add2.png");
            }
        })
    });

    $("#modal_trigger").leanModal({
        top: 200,
        overlay: 0.5,
        closeButton: ".modal_close",
        addButton: ".modal_add",
    });
    $("#modal_trigger2").leanModal({
        top: 200,
        overlay: 0.5,
        closeButton: ".modal_close",
        addButton: ".modal_add",
    });

    addlist()
    savelist()
    login()
});