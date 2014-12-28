var myLatlng = new google.maps.LatLng(0,0);
        var map;
        function initialize() {
                geocoder = new google.maps.Geocoder();
                var mapOptions = {
                        zoom: 1,
                        center: myLatlng
                };

                map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
        }

        google.maps.event.addDomListener(window, 'load', initialize);
        refreshMap();

        function addRecord() {
                var city = document.getElementById("city").value
                var longitude = ""
                var latitude = ""
                geocoder.geocode( {'address':city}, function(results, status) {
                        if (status == google.maps.GeocoderStatus.OK) {
                                longitude = results[0]['geometry']['location']['D']
                                latitude = results[0]['geometry']['location']['k']
                                $.post('/add',
                                        {
                                                'name' : document.getElementById("name").value,
                                                'longitude': longitude,
                                                'latitude' : latitude
                                        });
                                refreshMap();
                        }
                });
        }

        function refreshMap() {
                $.get('/get', function(data) {
                        console.log(data);
                        console.log(data['records'][0]);
                        for(index = 0; index < data['records'].length; ++index ) {
                                var marker_loc = new google.maps.LatLng(data['records'][index]['latitude'], data['records'][index]['longitude'])
                                console.log(data['records'][index]['latitude']);
                                var marker = new google.maps.Marker({
                                        position: marker_loc,
                                        map: map,
                                        title: data['records'][index]['name']
                                });
                        };
                });
        }

