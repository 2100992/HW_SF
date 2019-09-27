const header = new Headers({
    'Access-Control-Allow-Credentials': true, 
    'Access-Control-Allow-Origin': '*'
})

function postVote(url, animal){
    const fullURL = url+'/sse/vote/'+animal;
    let ajax = new XMLHttpRequest();
    ajax.open('POST', fullURL);
    ajax.withCredentials = true;
    // ajax.setRequestHeader('Access-Control-Allow-Credentials', true)
    //ajax.setRequestHeader('Access-Control-Allow-Origin', fullURL)
    //console.log('setHeaders')
    // console.log(ajax)
    ajax.send(null);
    //console.log('send')
    
}

const buttonDogs = $('#dogs')
const buttonCats = $('#cats')
const buttonParrots = $('#parrots')

buttonCats.click(() => {
    postVote(serverURL, 'cats')
})

buttonDogs.click(() => {
    postVote(serverURL, 'dogs')
})

buttonParrots.click(() => {
    postVote(serverURL, 'parrots')
})
