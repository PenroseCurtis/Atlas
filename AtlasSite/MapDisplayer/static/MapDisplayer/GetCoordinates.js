function renderMapInfo(map) {
	document.getElementById("mapSummary").innerHTML=map.summary;
	document.getElementById("mapName").innerHTML=map.name;
	document.getElementById("detailLink").href=map.full_link;
}
$(function() {
$("#test").click(function(e) {
	var offset = $(this).offset();
	var relativeX = (e.pageX - offset.left);
	var relativeY = (e.pageY - offset.top);
	/*if(mapSelected)
	{
		width=currentMap.width;
		height=currentMap.height;
		XCoord=width*(relativeX/$(this.width()));
		YCoord=height*(relativeY/$(this.height()));
		regionIndex=XCoord + YCoord*width;
		for region in 
		console.log(mapSelectedID);
	
			console.log("Success");
			console.log(data.summary);
			console.log(data.name);
			renderMapInfo(data.region);
			//document.getElementById("mapSummary").innerHTML=data.summary;
			//document.getElementById("mapName").innerHTML=data.name;
			//document.getElementById("detailLink").href=data.URL;
			console.log(path);
			currentMapID = mapSelectedID;
			mapSelected = false;
			mapList.length=navIndex+1;
			mapList.push(map);
			navIndex++;
			},
			})
	}	
	*/
	$(".position").val("afaf");
	$.ajax({
          url: '/MapDisplayer/getRegionFromCoordinates/',
	  data: {
		'x': relativeX/$(this).width(),
		'y': relativeY/$(this).height(),
		'mapID':currentMapID,
		},
	  dataType: 'json',
	  success: function(data) {
		//console.log(data.Index);
		//console.log(data.mapName);
		if(data.ID>=0)
		{
			mapSelectedID = data.ID;
			isMapSelected = true;
			map = {
				'summary':data.Summary,
				'full_link':data.full_link_URL,
				'imageURL':data.URL,
				'name':data.map_name,
				'ID':data.ID
				}
			document.getElementById("mapSummary").innerHTML=map.summary;
			document.getElementById("mapName").innerHTML=map.name;
			document.getElementById("detailLink").href=map.full_link;
		}
		}})
	
});
});

$(function() {
$("#test").dblclick(function() {
	console.log("Hello");
});
});

$(function() {
$("#back").click(function(e){
	console.log(navIndex);
	if(navIndex==0)
	{
		console.log("You cannot go back further");
	}
	else {
		navIndex--;
		currentMap=mapList[navIndex];
		renderMapInfo(currentMap);
		loadNewMap(currentMap);
	}	
});
});
$(function() {
$("#next").click(function(e){
	console.log(navIndex);
	if(navIndex==mapList.length)
	{
		console.log("You cannot go any further");
	}
	else
	{
		navIndex++;
		currentMap=mapList[navIndex];
		renderMapInfo(currentMap);
		loadNewMap(currentMap);
	}
});
});
		
function loadNewMap(mapToLoad) {
	path = "/static/MapDisplayer/"+mapToLoad.imageURL;
	document.getElementById("test").src=path;	
};

$(function() {
$("#Load").click(function(e) {
	if(map != null)
	{	
		renderMapInfo(map);
		loadNewMap(map);
		currentMap = map;
		navIndex++;
		mapList.length=navIndex;
		mapList.push(map);

	}	
	else {
	console.log("No map selected to load");
	}
});
});
	

