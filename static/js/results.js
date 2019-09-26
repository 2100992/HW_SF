const MyDogs = document.querySelector('#MyDogs')
const MyCats = document.querySelector('#MyCats')
const MyParrots = document.querySelector('#MyParrots')

const SFDogs = document.querySelector('#SFDogs')
const SFCats = document.querySelector('#SFCats')
const SFParrots = document.querySelector('#SFParrots')


const header = new Headers({
    'Access-Control-Allow-Credentials': true, 
    'Access-Control-Allow-Origin': '*'
})

// const SFURL = new URL(SFServerURL+'/sse/vote/stats')
const MyURL = new URL(MyServerURL+'/sse/vote/stats')

// const SFES = new EventSource(SFURL, header);
const MyES = new EventSource(MyURL, header);

// SFES.onopen = event => {
//     console.log(event)
// }

// SFES.onerror = error => {
//     SFES.readyState ? console.error("⛔ EventSource failed: ", error) : null;
// };

// SFES.onmessage = message => {
//     let dogs = message.data.data['dogs']
//     let cats = message.data.cats
//     let parrots = message.data.parrots
//     let allAnimals = dogs + cats + parrots
//     let ratioCats = cats / allAnimals * 100
//     let ratioDogs = dogs / allAnimals * 100
//     let ratioParrots = parrots / allAnimals * 100

//     console.log(`dogs = ${dogs}, ratioDogs = ${ratioDogs}`)

//     SFDogs.style.cssText = `width: ${ratioDogs}%;`
//     SFDogs.textContent = `${dogs}`

//     SFCats.style.cssText = `width: ${ratioCats}%;`
//     SFCats.textContent = `${cats}`

//     SFParrots.style.cssText = `width: ${ratioParrots}%;`
//     SFParrots.textContent = `${parrots}`
// }


MyES.onopen = event => {
    console.log(event)
  }
  
MyES.onerror = error => {
    MyES.readyState ? console.error("⛔ EventSource failed: ", error) : null;
};

MyES.onmessage = message => {
    console.log(message.data)
}



