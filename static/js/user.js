window.onload = function() {

    var myClass = document.getElementsByClassName('logout-sadwhref');

    myClass[0].addEventListener("click", function(e) {;
        console.log('ye')
        var data = { state: 'false' }

        console.log(window.location.hostname)
        contactServer_register(data);
    })
}

var contactServer_register = function(data) {
    $.ajax({
        type: 'POST',
        url: 'api/users/id',
        data: data,
        success: function(response) {
            console.log(response);
            console.log(response['Route']);
            console.log('register');
            //window.location.replace(response['Route']);
        },
        error: function(error) {
            console.log(error);
            console.log(window.location)
        }
    })
}