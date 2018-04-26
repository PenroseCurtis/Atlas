$(function() {
$("#search-button").click(function(e) {
	var textField = $('#search-bar');
	console.log(textField.val())
	$.ajax({
	    url: '/MapDisplayer/search/',
	    data: {
		'key': textField.val()
		},
	    dataType: 'json',
            success: function(data) {
		console.log(data.data);
		var maps = data.data;
		$div = $("#map-list");
		$div.empty()
		for (map of maps)
		{
		    $link =$("<a></a>").text(map.name);
		    href = "/MapDisplayer/"+map.id+"/viewMap";
		    $link.attr("href",href);
		    $div.append($link)
		    $div.append($("<br>"))
		}
		}})
})
});
	
	
	
