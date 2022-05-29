balanceParens = (str) => {
    parensTracker = [[],[]];
    str = str.split('');  // parensTracker[0] will act as thestack; parensTracker[1] will remember multiple '(' index locations
    str.forEach((char, i) => {
        if (char === '(') {
            parensTracker[0].push(char);
            parensTracker[1].push(i);
        }
        if (char === ')') {
            if (parensTracker[0].length === 0) {
                //console.log(`removing ${char} at index ${i}`)
                //console.log(`before: ${str}`)
                str[i] = '';
                //console.log(`after: ${str}`)
            } else {
                parensTracker[0].pop();
                parensTracker[1].pop();
            }
        }
    })
    
    if (parensTracker[1].length > 0) {
        parensTracker[1].forEach(i => {
            str[i] = '';
        })
    }

    return str.join('')
}

module.exports = { balanceParens }
