window.onload = function() {

    var submitButton = document.getElementById('btn');
    submitButton.addEventListener('click', sendForm);

    var myClass = document.getElementsByClassName('register-href');

    myClass[0].addEventListener("click", function(e) {;
        console.log('ye')
        var data = { request_url: 'register' }
        contactServer_logout(data);
    })
}
var contactServer_logout = function(data) {
    $.ajax({
        type: 'GET',
        url: 'api/validate/',
        data: data,
        success: function(response) {
            console.log(response);
            console.log(response['Route']);
            console.log('register');
            window.location.replace(response['Route']);
        },
        error: function(error) {
            console.log(error);
        }
    })
}
var sendForm = function(e) {
    //e.preventDefault();
    var userNameObject = document.getElementById('inputUsername');
    var userNameValue = userNameObject.value;

    var userPasswordObject = document.getElementById('inputPassword');
    var userPasswordValue = userPasswordObject.value;
    // TODO: Validate
    var data = { user: userNameValue, password: userPasswordValue }

    console.log(data);
    contactServer_login(data)
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