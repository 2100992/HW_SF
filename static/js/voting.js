const ajax = new XMLHttpRequest();

function postVote(url, animal){
    const fullURL = url+'/sse/vote/'+animal;
    ajax.open('POST', fullURL);
    ajax.send();
}
