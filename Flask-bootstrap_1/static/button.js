// A $( document ).ready() block.
$( document ).ready(function() {
    alert("posted");
    $("#button").click(function(event) {
    	$.post("/test",{"data": "1"});
    alert("posted);
    	});
    
    event.preventDefault();
});