// Exercise 1
function reduceFraction(num, den) {
    return undefined;
}

// Exercise 2
function isMagicDate(day, month, year) {

    let dayMonth = day * month;
    let yearDigits = year.toString().slice(2);
    

    if (dayMonth == yearDigits){
        return true;
    } else {
        return false;
    }

}

// Exercise 3
function sublist(l) {

    let lst = [];
    

    for (let i = 0; i < l.length +1; i++){
        for (let j = i; j < l.length +1 ; j++){

            let items = l.slice(i,j);
            lst.push(items); 
        }
    }

    let finalList = lst.filter(itemCheck => itemCheck.some(x=> x != ''));
    finalList.unshift([]);
    finalList.sort();

    return finalList
}

// Exercise 4
function pigLatin(word) {
    return undefined
}

// Exercise 5
function morseCode(message) {

    let codeMessage = '';

    const morse = {
        'a': '.- ',
        'b': '-... ',
        'c': '-.-. ',
        'd': '-.. ',
        'e': '. ',
        'f': '..-. ',
        'g': '--. ',
        'h': '.... ',
        'i': '.. ',
        'j': '.--- ',
        'k': '-.- ',
        'l': '.-.. ',
        'm': '-- ',
        'n': '-. ',
        'o': '--- ',
        'p': '.--. ',
        'q': '--.- ',
        'r': '.-. ',
        's': '... ',
        't': '- ',
        'u': '..- ',
        'v': '...- ',
        'w': '.-- ',
        'x': '-..- ',
        'y': '-.-- ',
        'z': '--.. ',
        
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
        '0': '----- ',

        'A': '.- ',
        'B': '-... ',
        'C': '-.-. ',
        'D': '-.. ',
        'E': '. ',
        'F': '..-. ',
        'G': '--. ',
        'H': '.... ',
        'I': '.. ',
        'J': '.--- ',
        'K': '-.- ',
        'L': '.-.. ',
        'M': '-- ',
        'N': '-. ',
        'O': '--- ',
        'P': '.--. ',
        'Q': '--.- ',
        'R': '.-. ',
        'S': '... ',
        'T': '- ',
        'U': '..- ',
        'V': '...- ',
        'W': '.-- ',
        'X': '-..- ',
        'Y': '-.-- ',
        'Z': '--.. ',
    }

    for (let i = 0; i < message.length;i++){
        let a = message[i];
        for(key in morse){
            if (key == message[i]){
                codeMessage += morse[key];
            }  
        }
    }
    let trimmedCodeMessage = codeMessage.trimEnd();

    return trimmedCodeMessage;
}

// Exercise 6
function int2Text(num) {
    return undefined
}

// Exercise 7
function missingComment(filename) {

    const fs = require('fs');
    const file = fs.readFileSync(filename,'utf8');
    const splitFile = file.toString().split('\n');

    let functList = [];
    let prevLine  = '';
    let currentLine = '';

    

    return splitFile;
}

// Exercise 8
function consistentLineLength(filename, length) {
    return undefined
}

// Exercise 9
function knight(start, end, moves) {
    return undefined
}

// Exercise 10
function warOfSpecies(environment) {
    return undefined
}

module.exports = {
    reduceFraction: reduceFraction,
    isMagicDate: isMagicDate,
    sublist: sublist,
    pigLatin: pigLatin,
    morseCode: morseCode,
    int2Text: int2Text,
    missingComment: missingComment,
    consistentLineLength: consistentLineLength,
    knight: knight,
    warOfSpecies: warOfSpecies
}