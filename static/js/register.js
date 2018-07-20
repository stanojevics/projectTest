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

    var userEmail = document.getElementById('inputEmail');
    var userEmailValue = userEmail.value;

    var data = { user: userNameValue, password: userPasswordValue, email: userEmailValue }
        //call server:
    console.log(data);
    contactServer(data);
}

var contactServer = function(data) {
    $.ajax({
        type: 'POST',
        url: '/api/register/',
        data: data,

        success: function(response) {
            console.log(response)
            console.log(response['Route'])
            window.location.replace(response['Route']);

        },
        error: function(error) {
            console.log(error);
        }

    })
}