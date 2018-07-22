window.onload = function() {

    var myClass = document.getElementsByClassName('logout-href');
    myClass[0].addEventListener("click", function(e) {;
        console.log('ye')
        var data = { request_url: '/', flag: 'logout' }

        console.log(window.location.hostname)
        contactServer(data);
    })
    var profileClass = document.getElementsByClassName('profile-href');
    profileClass[0].addEventListener('click', function(e) {;
        console.log('profile')
        var data = { request_url: '/', flag: 'register' }
        contactServer(data);

    })
}
var contactServer = function(data) {
    $.ajax({
        type: 'POST',
        url: '/api/validate/',
        data: data,
        success: function(response) {
            console.log(response);
            console.log(response['Route']);
            console.log(response['Status']);
            window.location.replace(response['Route']);
        },
        error: function(error) {
            console.log('wow')
            console.log(error);
            console.log(window.location)
        }
    })
}