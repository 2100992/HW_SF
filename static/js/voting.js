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
    console.log(`POST sended to ${fullURL}`)
}

const buttonDogs = $('#dogs')
const buttonCats = $('#cats')
const buttonParrots = $('#parrots')
const resultsLink = $('.resultsLink')

buttonCats.click(() => {
    postVote(serverURL, 'cats')
    resultsLink.css('display', 'block')
})

buttonDogs.click(() => {
    postVote(serverURL, 'dogs')
    resultsLink.css('display', 'block')
})

buttonParrots.click(() => {
    postVote(serverURL, 'parrots')
    resultsLink.css('display', 'block')
})
