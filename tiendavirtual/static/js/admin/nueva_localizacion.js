function nueva_localizacion(csrftoken, latitud, longitud){
    var url = "http://127.0.0.1:8000/";
    url+= "api/localizacion/crear";
    var tiendas;
    var data = {latitud: latitud, longitud: longitud};
    $.ajax({
        url: url,
        data: data,
        type: "POST",
        beforeSend: before
    })
    .error(function(data){
        console.log(data);
    })
    .success(function(data){
        console.log(data);

        $("#id_localizacion").append($("<option></option>")
                             .attr("value",data.id)
                             .text("("+data.latitud+", "+data.longitud+")"));
        $("#id_localizacion").val(data.id);
        $('#id_localizacion').material_select();

    })
    function before(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
}