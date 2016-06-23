function initMap(){
    "use strict";

    var csrftoken = getCookie('csrftoken');
    var url = window.Tienda.url?window.Tienda.url:"http://127.0.0.1:8000";
    var myLatlng = new google.maps.LatLng(-12.046374,-77.0427934);
    var mapOptions = {
      zoom: 12,
      center: myLatlng
    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);


    url+= "api/ListStores/";
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
            console.log(value);
            var tienda = value;
            var myLatlng = new google.maps.LatLng(tienda.localizacion.latitud, tienda.localizacion.longitud);
            var marker = new google.maps.Marker({
                position: myLatlng,
                title: tienda.nombre,
                icon: "../media/logoSMstore2.png",
            });
            //var content = getContenidoPopup();
            var infowindow = new google.maps.InfoWindow({
                content: content(tienda.nombre,tienda.imagen,tienda.direccion,tienda.horario_atencion,tienda.telefono)
            });
            marker.addListener('click', function() {
                infowindow.open(map, marker);
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

function content(nombre,imagen,direccion,horario_atencion,telefono){
    html="<div style='background-color: black;'>";
    html= "<b>"+nombre+"</b><br>";
    html+="<img style='width: 150px;height: 100px;' src='"+imagen+"' />";
    html+="<p>"+direccion+"<br />";
    html+="<p>"+horario_atencion+"</p>";
    html+="<p>"+telefono+"</p>";
    html+="</div>";
    return html;
}
/*
		var data;
	   	$(".lista-lugares a").on("click", function(evt){

		  	 var shop =  $(evt.currentTarget).data("shop");
		  	var urlApi = "http://catlifestyle.pe/wp-content/themes/theme_cat";
		  	urlApi = urlApi + "/store-locator/api.php";

		  	var objecto = {};
		  	objecto.f = "get_shop_data";
		  	objecto.a = [shop];
		  	var texto = JSON.stringify(objecto);
		  	urlApi = urlApi+"?app_data="+texto;

		  	 $.ajax({
				  type: "GET",
				  url: urlApi,
				  dataType:"JSON"
				})
				  .done(function( msg ) {
				  	data=msg;

				    //showPopupMarker(data);
				    showPopupStore(data);
	  			});

		   	});
			function showPopupStore(msg){
				//////////////////zoom-mapa

				    var map = new google.maps.Map(document.getElementById('map'), {
				      zoom: 16,
				      center: new google.maps.LatLng(msg.latitude,msg.longitude),
				      mapTypeId: google.maps.MapTypeId.ROADMAP
				     });
				    //////////////////marcador-tienda
			    	var infowindow = new google.maps.InfoWindow();
	    			marker = new google.maps.Marker({
			        position: new google.maps.LatLng(msg.latitude,msg.longitude),
			        map: map,
			        icon: "http://catlifestyle.pe/wp-content/themes/theme_cat/store-locator/images/marker.png",
			        shadow: "http://catlifestyle.pe/wp-content/themes/theme_cat/store-locator/images/marker-shadow.png"
			     	 });
			     	/////////////////iniciar con info de marcador por 3s
		            infowindow.setContent(getContenidoPopup(msg.city,msg.image,msg.shop_address,msg.district,msg.hours,msg.phone));
		            infowindow.open(map, marker);
				    setTimeout(function(){
				    	infowindow.close();},5000);
				    /////////////////mostrar info de marcador
				    google.maps.event.addListener(marker, 'click', (function(marker) {
					        return function() {
					          infowindow.setContent(getContenidoPopup(msg.city,msg.image,msg.shop_address,msg.district,msg.hours,msg.phone));
					          infowindow.open(map, marker);
					           setTimeout(function(){
				    			infowindow.close();},5000);
					        }
					      })(marker));

			}
			function getContenidoPopup(city,image,shop_address,district,hours,phone){
				html= city+"<br><br>"
				html+="<img class='img-store' src='"+image+"' />";
				html+="<p>"+shop_address+"<br />";
				html+=""+district+"</p>";
				html+="<p>"+hours+"</p>";
				html+="<p>"+phone+"</p>";
				return html;
			}
*/