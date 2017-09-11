function xmlreq(){
	var xmlhttp;
	xmlhttp=new XMLHttpRequest();
	xmlhttp.open("GET","/getmessage/",true);
	xmlhttp.send();
	xmlhttp.onreadystatechange=function()
  	{
  	if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
		
		jsonObject = JSON.parse(xmlhttp.responseText);
		list = jsonObject.list;
		console.log(list)
		for(var i in list)
			{
				container = document.getElementsByClassName("container-fluid")[0]
				container.innerHTML += "<div class='row-fluid'>" + "<div class='span12'>" + "<div class='col'>" + "<p class='text-center'>" + list[i].message + "</p>" + "</div>" + "</div>" + "</div>"
			}
		scrollToBottom();

		
    }
  	}
}


function settime(){
	window.setInterval(xmlreq,5000);
}
window.onload=function(){
	console.log('222')
	xmlreq();
	settime();
	
};
var delay = 10;//in milliseconds
var scroll_amount = 10;// in pixels
var interval;
function scroller() {
    var old = document.body.scrollTop;//保存当前滚动条到顶端的距离
    document.body.scrollTop += scroll_amount;//让滚动条继续往下滚动
    if (document.body.scrollTop == old) {//到底部后就无法再增加scrollTop的值
        clearInterval(interval);
    }
}
function scrollToBottom()
{
  interval = setInterval("scroller()",delay);
}

