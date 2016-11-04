/* $(function () { $("[data-toggle='tooltip']").tooltip(); }); */

var timer;
var cur_status;

// milliseconds to wait before refreshing status when action occurs, eg. Run Now
var short_timeout = 400;

timer = setTimeout(updateCoffeeStatus, short_timeout);

function updateCoffeeStatus() {
  //logmsg('updating status, url='+$('#status_url').attr('value'));
  //console.log('updating...');
  $.ajax({
    url: '/api/status',
    dataType: 'jsonp'
  }).done(function( data ) {
  	//console.log('data='+JSON.stringify(data))
    var status = data['data']['objects'][0]['station_status'];

    //console.log('updating status='+status)//,', brew_time='+getLocalTime(data['objects']['brew_time']))

    //$('#intraday_start').text(getLocalTime(data['data']['start_date']));
 
 	if (status != cur_status) {
 	  if (status == 1) {
 	    console.log('updating pot to full')
 	    $('.status').attr('src', '/static/images/CoffeePot_full.png');
 	  } else {
 	    console.log('updating pot to empty')
 	    $('.status').attr('src', '/static/images/CoffeePot_empty.png');
 	  }
 	  cur_status = status; 		
 	}

 	timer = setTimeout(updateCoffeeStatus, short_timeout);
    
  });

  return status;
}

function getLocalTime(date) {
  m = moment(date);
  localTime = m.hours()+":"+(m.minutes()<10?'0':'')+m.minutes();
  //logmsg("getLocalTime="+localTime);
  return m.format("h:mm A");
}
