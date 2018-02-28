$(function() {
$("#test").click(function(e) {
	var offset = $(this).offset();
	var relativeX = (e.pageX - offset.left);
	var relativeY = (e.pageY - offset.top);
	alert(relativeX+':'+relativeY);
	$(".position").val("afaf");
	$.ajax({
          url: '/MapDisplayer/getDetail/',
	  data: {
		'x': relativeX,
		'y': relativeY,
		},
	  dataType: 'json',
	  success: function() {
		console.log("You did it")
		}})
});
});
