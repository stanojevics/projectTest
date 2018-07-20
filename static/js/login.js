window.onload = function() {

    var submitButton = document.getElementById('btn');
    submitButton.addEventListener('click', sendForm);
}

var sendForm = function(e) {
    e.preventDefault();
    var userNameObject = document.getElementById('inputUsername');
    var userNameValue = userNameObject.value;

    var userPasswordObject = document.getElementById('inputPassword');
    var userPasswordValue = userPasswordObject.value;
    // TODO: Validate
    var data = { user: userNameValue, password: userPasswordValue }

    console.log(data);
    contactServer(data)
}

var contactServer = function(data) {
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