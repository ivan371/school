$(document).ready(function() {
       $('.dialog_name').click(function(){
            $('.dialog').each(function(){this.style.display = 'none';});
            var id = $('#dialog' + $(this).data('dialog'));
            id.css('display','block');
            id.load('/message/' + $(this).data('dialog') + '/');
            return false;
       });
});