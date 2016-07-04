(function(){
    $('.btn-add-loc').click(openMod);

    $('#formRegLoc').submit(registrarLocalizacion);
    function openMod(e){
        e.preventDefault();
        var prod = $(e.currentTarget);
    }
    function registrarLocalizacion(e){
        e.preventDefault();
        var latitud = $(e.currentTarget).find('.latitud').val();
        var longitud = $(e.currentTarget).find('.longitud').val()
        var csrftoken = getCookie('csrftoken',latitud,longitud);

        nueva_localizacion(csrftoken, latitud, longitud);
    }




})();