
function initMap(){
    var myLatlng = new google.maps.LatLng(-12.05334389,-77.08542377);
    var mapOptions = {
      zoom: 15,
      center: myLatlng
    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var marker = new google.maps.Marker({
        position: myLatlng,
        title:"1st store!"
    });

    marker.setMap(map);
    }