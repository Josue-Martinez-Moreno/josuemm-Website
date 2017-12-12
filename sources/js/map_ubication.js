    var myLatlng = new google.maps.LatLng(-35.283848, 149.115027);
    
    var contentString =  '<div id="content">'+
        '<div id="siteNotice">'+
        '</div>'+
        '<h1 id="firstHeading" class="firstHeading">Research School of Earth Sciences</h1>'+
        '<div id="bodyContent">'+
        '<p>The study of Earth and marine sciences is fundamental to our understanding of the precious balance of life on Earth and how the Solar System in which we live was formed. Our focus is on both Earth processes and environmental science.</p>'+
        '</div>'+
        '</div>';
    
    function initialize() {
        
            
        var infowindow = new google.maps.InfoWindow({
            content: contentString
        });
        
        var mapOptions = {
            zoom: 14,
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