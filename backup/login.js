$(function() {
    $('button').click(function() {
        var user = $('#inputUsername').val();
        var pass = $('#inputPassword').val();
        $.ajax({
            url: '/login',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                window.location.replace('/');
            },
            error: function(error) {
                console.log('123');
                console.log(error);
            }
        });
    });
});