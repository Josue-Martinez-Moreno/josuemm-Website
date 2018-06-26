    var myLatlng = new google.maps.LatLng(-35.283642, 149.114862);
    
    var contentString =  '<div id="content">'+
        '<div id="siteNotice">'+
        '</div>'+
        '<h2>Address:</h2>'+
        '<div id="bodyContent">'+
        '<p>Jaeger 7, RSES, 142 Mills Rd, Acton ACT 0200</p>'+
        '<h1>Office:</h1>'+
        '<p> J7.222 </p>' +
        '<h1>Contact Details: </h1>'+
        '<p> Email: josue.martinezmoreno@anu.edu.au </p>' +
        '<p> Phone: 0426104364 </p>' +
        '</div>'+
        '</div>';
    
    function initialize() {
        
            
        var infowindow = new google.maps.InfoWindow({
            content: contentString
        });
        
        var mapOptions = {
            zoom: 17,
            center: myLatlng,
            scrollwheel: false,
            navigationControl: true,
            mapTypeControl: true,
            scaleControl: true,
            draggable: true,
            mapTypeId: google.maps.MapTypeId.TERRAIN,
            mapTypeControlOptions: {
                style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
                position: google.maps.ControlPosition.BOTTOM_CENTER
                },
            zoomControl: true,
            zoomControlOptions: {
                style: google.maps.ZoomControlStyle.LARGE,
                position: google.maps.ControlPosition.LEFT_CENTER
            },
            scaleControl: true,
            streetViewControl: false,
            streetViewControlOptions: {
                position: google.maps.ControlPosition.LEFT_TOP
            }
        }
        
        var map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
        
        var marker = new google.maps.Marker({
            position: myLatlng,
            map: map,
            animation: google.maps.Animation.DROP,
            title: 'Research School of Earth Sciences (ANU)!'
        });
        
        google.maps.event.addListener(marker, 'click', function() {
            infowindow.open(map,marker);
        });
        
    }

    google.maps.event.addDomListener(window, 'load', initialize);