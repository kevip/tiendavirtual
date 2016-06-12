function initMap(){
    "use strict";

    var csrftoken = getCookie('csrftoken');
    var url = window.Tienda.url?window.Tienda.url:"http://127.0.0.1:8000";
    var myLatlng = new google.maps.LatLng(-12.046374,-77.0427934);
    var mapOptions = {
      zoom: 11,
      center: myLatlng
    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);


    url+= "api/tiendas";
    $.ajax({
        url: url,
        type: "GET",
        beforeSend: before
    })
    .error(function(data){
        console.log(data);
    })
    .success(function(data){
        $.each( data, function( key, value ) {
            var myLatlng = new google.maps.LatLng(value.fields.latitud, value.fields.longitud);
            var marker = new google.maps.Marker({
                position: myLatlng,
                title:"1st store!"
            });
            marker.setMap(map);
        });

    });
    function before(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }


}

function getTiendas(){
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
        return data;
    })
    .success(function(data){
        return data;
    })
    function before(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
}