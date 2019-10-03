let checkBoxes = [
        '#defaultCheck1',
        '#defaultCheck2',
        '#defaultCheck3',
        '#defaultCheck4',
        '#defaultCheck5',
        '#defaultCheck6',
        '#defaultCheck7',
]


function getStorageItems(){
    let iter = ''
    let lsiter = ''
    for (i in checkBoxes) {
        iter = $(checkBoxes[i])
        lsiter = localStorage.getItem(checkBoxes[i])
        iter.prop('checked', lsiter)
    }
}

function setStorageItems(){
    let iter = ''
    let lsiter = ''
    for (i in checkBoxes) {
        iter = $(checkBoxes[i]).prop('checked')
        localStorage.setItem(checkBoxes[i], iter)
    }
}

let secondCheck = $('#defaultCheck6')
secondCheck.prop("checked")
secondCheck.prop("checked", true)


function init() {
    // $('#preferencesID').addClass('active');
}

$(document).ready(init);