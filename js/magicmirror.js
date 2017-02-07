
  
  $(document).ready(function() {
   
   setInterval(function() {
                  updateDisplay();
                }, 1000); 
  });
  
  function updateTime()
  {
	 
	var d = new Date();	
	a = formatAMPM(d);
	$("#timeHolder").text(a);
  }
  
  function formatAMPM(date) 
  {
	  var hours = date.getHours();
	  var minutes = date.getMinutes();
	  var ampm = hours >= 12 ? 'pm' : 'am';
	  hours = hours % 12;
	  hours = hours ? hours : 12; // the hour '0' should be '12'
	  minutes = minutes < 10 ? '0'+minutes : minutes;
	  var strTime = hours + ':' + minutes + ' ' + ampm;
	  return strTime;
}
  
  function updateDate()
  {
	var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
	var months = ["Jan","Feb","Mar","Apr","May","Jun","July", "Aug", "Sep", "Oct", "Nov", "Dec"];
	var daySubscript=""; 
	
	currentTime = new Date();
	date= currentTime.getDate();
	month= months[currentTime.getMonth()];
	day=currentTime.getDay();	
	weekday=days[day];
	
	if(date==1 || date==21 || date==31)
	{
		daySubscript="st"
	}
	else if(date==2 || date==22)
	{
		daySubscript="nd"
	}
	else if(date==3 || date==23)
	{
		daySubscript="rd"
	}
	else 
	{
		daySubscript="th"
	}
	displayTime=weekday + ", " + month + " "+ date+daySubscript;
	
	
	$("#dateHolder").html("<b>"+displayTime+"</b>");
  }
  
  function updateDisplay()
  {
	  updateTime();
	  updateDate();
  }
  
  
  
