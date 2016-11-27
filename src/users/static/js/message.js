cur_id = 1 ;
function select_message(id)
{
    document.getElementById(cur_id).style.display = "none";
    document.getElementById(id).style.display = "block";
    cur_id = id;
}

is_blocked = 0;
function block_message()
{
    if(is_blocked == 0)
    {
        document.getElementById("sms").style.display = "block";
        is_blocked = 1;
    }
    else
    {
        document.getElementById("sms").style.display = "none";
        is_blocked = 0;
    }
}

$(document).ready(function() {
    $('.mess').click(function() {
        $('.content-dialog').load('/message/');
        return false;
    });
    $(document).on('submit', '.ajax-form', function(){
        var form = $(this);
        $.post(form.attr('action'), form.serialize(), function(data){
            alert(1);
            if(data == 'OK') {
                window.location.reload();
            }
            form.html(data);

        })
            .fail(function(xhr, errmsg, err){
 						alert(xhr.status + ": " + xhr.responseText);
            });;
        return false;
    });
});

