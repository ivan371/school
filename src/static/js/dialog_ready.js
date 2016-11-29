var messageid = 0;
$(document).ready(function() {
       $('.dialog_name').click(function(){
            $('.dial').each(function(){
                this.style.display = 'none';
            });
            $('.dialcreate').each(function(){
                this.style.display = 'none';
            });
            var id = $($(this).data('dialogid'));
            id.css('display','block');
            id.load($(this).data('dialogload'));
            $($(this).data('dialogcreate')).css('display', 'block');
            $($(this).data('dialogcreate')).load($(this).data('dialogformload'));
            messageid = $(this).data('dialog');
            return false;
       });
       window.setInterval(function(){
           $('#dialog' + messageid).load('/message/' + messageid + '/');
       }, 1000);
});