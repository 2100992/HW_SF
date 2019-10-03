const header = new Headers({
    'Access-Control-Allow-Credentials': true, 
    'Access-Control-Allow-Origin': '*'
})

const progressDogs = document.querySelector('#SFDogs')
const progressCats = document.querySelector('#SFCats')
const progressParrots = document.querySelector('#SFParrots')


const url = new URL('https://sf-pyw.mosyag.in/sse/vote/stats')
const ES = new EventSource(url, header);

ES.onopen = event => {
    console.log(event)
}

ES.onerror = error => {
    ES.readyState ? console.error("⛔ EventSource failed: ", error) : null;
};

ES.onmessage = message => {
    let result = JSON.parse(message.data)
    let dogs = result.dogs
    let cats = result.cats
    let parrots = result.parrots
    let allAnimals = dogs + cats + parrots
    let ratioCats = cats / allAnimals * 100
    let ratioDogs = dogs / allAnimals * 100
    let ratioParrots = parrots / allAnimals * 100

    SFDogs.style.cssText = `width: ${ratioDogs}%;`
    SFDogs.textContent = `${dogs}`

    SFCats.style.cssText = `width: ${ratioCats}%;`
    SFCats.textContent = `${cats}`

    SFParrots.style.cssText = `width: ${ratioParrots}%;`
    SFParrots.textContent = `${parrots}`
}