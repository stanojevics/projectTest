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

var contactServer_register = function(data) {
    $.ajax({
        type: 'GET',
        url: '/register',
        data: data,
        success: function(response) {
            console.log(response);
            console.log(response['Route']);
            console.log('register');
            window.location.replace(response['Route']);
        },
        error: function(response) {
            console.log(error);
        }
    })
}

var contactServer_login = function(data) {
    $.ajax({
        type: 'POST',
        url: 'api/validate/',
        data: data,

        success: function(response) {
            console.log(response);
            console.log(response['Route']);
            console.log(response['user_id'])
            window.location.replace('/api/users/' + response['user_id']);
        },
        error: function(error) {
            console.log(error);
        }
    })
}