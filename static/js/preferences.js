let checkBoxes = [
        '#defaultCheck1',
        '#defaultCheck2',
        '#defaultCheck3',
        '#defaultCheck4',
        '#defaultCheck5',
        '#defaultCheck6',
        '#defaultCheck7',
]

// функция берет из LocalStorage данные и заполняет чекбоксы
// To Do.
// - переименование функции в более понятное
// - переименование переменных
// - передавать в функцию массив имен как параметр
function getStorageItems() {
    let iter = ''           //итератор по id чекбоксов
    let LSiter = ''         //итератор по сохраненным  в localStorage предметам
    for (i in checkBoxes) {
        iter = $(checkBoxes[i])
        LSiter = localStorage.getItem(checkBoxes[i])
        if (LSiter === 'true') {
            iter.prop('checked', true)
        } else {
            iter.prop('checked', false)
        }
    }
}

// функция состояние чекбоксов и сохраняет его в LocalStorage
// To Do.
// - переименование функции в более понятное
// - переименование переменных
// - передавать в функцию массив имен как параметр
function setStorageItems(){
    let iter = ''
    for (i in checkBoxes) {
        iter = $(checkBoxes[i]).prop('checked')
        localStorage.setItem(checkBoxes[i], iter)
    }
}

// деактивируем чекбоксы из массива
// To Do.
// - передавать в функцию массив имен как парамет
function disableCheckboxes() {
    for (i in checkBoxes) {
        $(checkBoxes[i]).prop('disabled', true)
    }
}

function init() {
    getStorageItems()
    $('#defaultCheck7').click(function() {
        setStorageItems()
        disableCheckboxes()
    })
    if ($('#defaultCheck7').prop('checked')) {
        disableCheckboxes()
    }

}

$(document).ready(init);