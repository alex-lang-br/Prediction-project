function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }

function getBedValue(){
    var uiBeds = document.getElementsByName('uiBeds');
    for(var i in uiBeds) {
        if(uiBeds[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1;
}

function getCarValue(){
    var uiCars = document.getElementsByName('uiCars');
    for(var i in uiCars) {
        if(uiCars[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1;
}


function onClickedEstimatePrice(){
    console.log("Estimate price button was clicked");
    var bath = getBathValue();
    var bed = getBedValue();
    var car = getCarValue();
    var location = document.getElementById('uiLocations');
    var estimatedPrice = document.getElementById('uiEstimatedPrice');

    //var url = " http://127.0.0.1:5000/predict_home_price"; Use this url if you want to run the server locally
    var url = "/api/predict_home_price";

    $.post(url, {
        location: location.value,
        bed: bed,
        bath: bath,
        car: car
    },function(data, status){
        console.log(data.estimated_price);
        estimatedPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "Million USD </h2>";
        console.log(status);
    });
}


function onPageLoad() {
    console.log( "document loaded" );
    //var url = "http://127.0.0.1:5000/get_location_names"; Use this url if you want to run the server locally
    var url = '/api/get_location_names';
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;