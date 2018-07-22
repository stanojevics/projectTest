window.onload = function() {
    var submitButton = document.getElementById('btn');
    submitButton.addEventListener('click', sendForm);
    var myClass = document.getElementsByClassName('logout-href');
    myClass[0].addEventListener("click", function(e) {;
        console.log('ye')
        var data = { request_url: '/', flag: 'logout' }

        console.log(window.location.hostname)
        contactServer(data);
    })
    var contentClass = document.getElementsByClassName('content-href');
    contentClass[0].addEventListener("click", function(e) {;
        console.log('ye')
        var data = { request_url: '/', flag: 'messages' }

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

var sendForm = function(e) {
    var oldPasswordObject = document.getElementById('oldPassword');
    var oldPasswordValue = oldPasswordObject.value;

    var newPasswordObject = document.getElementById('newPassword');
    var newPasswordValue = newPasswordObject.value;
    // TODO: Validate
    if (oldPasswordValue === newPasswordValue) {
        alert('New Password can not be same as old password!');
    } else {
        var data = { oldPassword: oldPasswordValue, newPassword: newPasswordValue, flag: 'change-password' }

        console.log(data);
        contactServer(data)
    }

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