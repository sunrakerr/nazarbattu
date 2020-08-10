const remote = require('electron').remote

 document.getElementById('closebut').addEventListener('click',closewindow)
 document.getElementById('minbut').addEventListener('click',minwindow)

 function closewindow(){
    var win = remote.getCurrentWindow()
    win.close()
 }
 function minwindow(){
    var win = remote.getCurrentWindow()
    win.minimize()
 }


