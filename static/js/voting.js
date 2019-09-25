const ajax = new XMLHttpRequest();

function postVote(url, animal){
    const fullURL = url+'/sse/vote/'+animal;
    ajax.open('POST', fullURL);
    ajax.send();
}



const header = new Headers({
    'Access-Control-Allow-Credentials': true, 
    'Access-Control-Allow-Origin': '*'
})

const ES = new EventSource('https://sf-pyw.mosyag.in/sse/stream', header);

ES.onopen = event => {
  console.log(event)
}

ES.onerror = error => {
  ES.readyState ? console.error("⛔ EventSource failed: ", error) : null;
};

ES.onmessage = message => {
	console.log(message.data)
}