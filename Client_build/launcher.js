const { ipcRenderer } = require('electron')
const fs = require('fs') 





function loader(){
    var log = fs.readFileSync('devlogs.txt','utf8')
    document.getElementById('newsdiv').innerHTML = log

}

loader();











