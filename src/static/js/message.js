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
is_title = 0;
function change_post()
{
    if(is_title == 0)
    {
        document.getElementById("create-post-title").style.display = "none";
        document.getElementById("create-post").style.display = "block";
        is_title = 1;
    }
    else {
        document.getElementById("create-post").style.display = "none";
        document.getElementById("create-post-title").style.display = "block";
        is_title = 0;
    }
}
