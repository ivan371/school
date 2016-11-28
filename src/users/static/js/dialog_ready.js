var messageid = 0;
$(document).ready(function() {
       $('.dialog_name').click(function(){
            $('.dialog').each(function(){
                this.style.display = 'none';
            });
            var id = $('#dialog' + $(this).data('dialog'));
            id.css('display','block');
            id.load('/message/' + $(this).data('dialog') + '/');
            $('#create' + $(this).data('dialog')).load('/message/' + $(this).data('dialog') + '/form_message/');
            messageid = $(this).data('dialog');
            return false;
       });
       //window.setInterval(function(){
       //    $('#messages' + messageid).load('/message/' + messageid + '/');
       //}, 1000);
});