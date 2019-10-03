const header = new Headers({
    'Access-Control-Allow-Credentials': true, 
    'Access-Control-Allow-Origin': '*'
})

const SFDogs = document.querySelector('#SFDogs')
const SFCats = document.querySelector('#SFCats')
const SFParrots = document.querySelector('#SFParrots')


const SFURL = new URL(SFServerURL+'/sse/vote/stats')
const SFES = new EventSource(SFURL, header);

SFES.onopen = event => {
    // console.log(event)
}

SFES.onerror = error => {
    SFES.readyState ? console.error("⛔ EventSource failed: ", error) : null;
};

SFES.onmessage = message => {
    console.log(message)
    console.log(`SF typeof(message) = ${typeof(message)}`)
    console.log(message.data)
    console.log(`SF typeof(message.data) = ${typeof(message.data)}`)
    let result = JSON.parse(message.data)
    let dogs = result.dogs
    let cats = result.cats
    let parrots = result.parrots
    let allAnimals = dogs + cats + parrots
    let ratioCats = cats / allAnimals * 100
    let ratioDogs = dogs / allAnimals * 100
    let ratioParrots = parrots / allAnimals * 100

    // console.log(`dogs = ${dogs}, ratioDogs = ${ratioDogs}`)

    SFDogs.style.cssText = `width: ${ratioDogs}%;`
    SFDogs.textContent = `${dogs}`

    SFCats.style.cssText = `width: ${ratioCats}%;`
    SFCats.textContent = `${cats}`

    SFParrots.style.cssText = `width: ${ratioParrots}%;`
    SFParrots.textContent = `${parrots}`
}

const MyDogs = document.querySelector('#MyDogs')
const MyCats = document.querySelector('#MyCats')
const MyParrots = document.querySelector('#MyParrots')

const MyURL = new URL(MyServerURL+'/sse/vote/stats')
const MyES = new EventSource(MyURL, header);

MyES.onopen = event => {
    // console.log(event)
  }
  
MyES.onerror = error => {
    MyES.readyState ? console.error("⛔ EventSource failed: ", error) : null;
};

MyES.onmessage = message => {
    console.log(message)
    console.log(`typeof(message) = ${typeof(message)}`)
    console.log(message.data)
    console.log(`typeof(message.data) = ${typeof(message.data)}`)
    let result = JSON.parse(message.data)
    console.log(result)
    let dogs = result.dogs
    let cats = result.cats
    let parrots = result.parrots
    let allAnimals = dogs + cats + parrots
    let ratioCats = cats / allAnimals * 100
    let ratioDogs = dogs / allAnimals * 100
    let ratioParrots = parrots / allAnimals * 100

    console.log(`dogs = ${dogs}, ratioDogs = ${ratioDogs}`)

    MyDogs.style.cssText = `width: ${ratioDogs}%;`
    MyDogs.textContent = `${dogs}`

    MyCats.style.cssText = `width: ${ratioCats}%;`
    MyCats.textContent = `${cats}`

    MyParrots.style.cssText = `width: ${ratioParrots}%;`
    MyParrots.textContent = `${parrots}`
}



