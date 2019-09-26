const header = new Headers({
    'Access-Control-Allow-Credentials': true, 
    'Access-Control-Allow-Origin': '*'
})

const MyURL = new URL(MyServerURL)
const SFURL = new URL(SFServerURL)


const SFES = new EventSource(SFURL, header);
const MyES = new EventSource(MyURL, header);

SFES.onopen = event => {
    console.log(event)
}

SFES.onerror = error => {
    SFES.readyState ? console.error("⛔ EventSource failed: ", error) : null;
};

SFES.onmessage = message => {
    console.log(message.data)
}


MyES.onopen = event => {
    console.log(event)
  }
  
MyES.onerror = error => {
    MyES.readyState ? console.error("⛔ EventSource failed: ", error) : null;
};

MyES.onmessage = message => {
    console.log(message.data)
}



const MyDogs = document.querySelector('#MyDogs')
const MyCats = document.querySelector('#MyCats')
const MyParrots = document.querySelector('#MyParrots')

const SFDogs = document.querySelector('#SFDogs')
const SFCats = document.querySelector('#SFCats')
const SFParrots = document.querySelector('#SFParrots')