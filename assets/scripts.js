$(document).ready(function(){
    
    $popover = $(".message-popover");
    if($popover.length) {
        window.setTimeout(function() {
            $popover.fadeOut(1000);
        }, 2000);
    }

    $popover = $(".message-popover");
    if($popover.length) {
        window.setTimeout(function() {
            $popover.fadeOut(1000);
        }, 2000);
    }

    $('#start-screen').click(function(){
        $('.push-notification').addClass("fade-in");
    });

    $('#btnSearch').click(function(){
                // show a hidden div to indicate progression
        $('#someHiddenDiv').show();

        // kick off AJAX
        $.ajax({
            url: this.action,
            type: this.method,
            data: $(this).serialize(),
            success: function() {
                // AJAX request finished, handle the results and hide progress
                $('#someHiddenDiv').hide();
            }
        });
        return false;
    }); 
});