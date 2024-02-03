function button1Function() {
	console.log('Button 1 clicked');
}

function button2Function() {
	console.log('Button 2 clicked');
}

function button3Function() {
	console.log('Button 3 clicked');
}

function button4Function() {
	console.log('Button 4 clicked');
}

function button5Function() {
	console.log('Button 5 clicked');
	ws = new WebSocket("ws://localhost:8000/practice");
	ws.onmessage = (data) => console.log(data.data);
	ws.onopen = () => {
		ws.send("PING");	
	}
}


