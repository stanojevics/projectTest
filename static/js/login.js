window.onload = function() {

    var submitButton = document.getElementById('btn');
    submitButton.addEventListener('click', sendForm);

    var myClass = document.getElementsByClassName('register-href');

    myClass[0].addEventListener("click", function(e) {;
        console.log('ye')
        var data = { request_url: '/api/register/', flag: 'register' }
        contactServer(data)
    })
}
var contactServer = function(data) {
    $.ajax({
        type: 'POST',
        url: 'api/validate/',
        data: data,
        success: function(response) {
            console.log(response)
            console.log(response['Route']);
            window.location.replace(response['Route']);
        },
        error: function(response) {
            console.log(response)
        }
    })
}

var sendForm = function(e) {
    var userNameObject = document.getElementById('inputUsername');
    var userNameValue = userNameObject.value;

    var userPasswordObject = document.getElementById('inputPassword');
    var userPasswordValue = userPasswordObject.value;
    // TODO: Validate
    var data = { user: userNameValue, password: userPasswordValue, flag: 'login' }

    console.log(data);
    contactServer(data)
}