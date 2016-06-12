function tiendas(){
    "use strict";
    var csrftoken = getCookie('csrftoken');
    var url = window.Tienda.url?window.Tienda.url:"http://127.0.0.1:8000";
    url+= "api/tiendas";
    var tiendas;
    $.ajax({
        url: url,
        type: "GET",
        beforeSend: before
    })
    .error(function(data){
        tiendas = data;
    })
    .success(function(data){
        tiendas = data;
    })
    function before(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }

}

