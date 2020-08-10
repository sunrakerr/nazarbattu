const electron = require('electron');
const {app, BrowserWindow} = require('electron');
const ipcMain = electron.ipcMain
const path = require('path');
const url = require('url');

var child = require('child_process').execFile;




let mainWindow = null 

//FrameChunk
app.on('ready',function(){
    mainWindow = new BrowserWindow({
        width:1920,
        height:800,
        frame: false,
        resizable:false,
        webPreferences: {
            nodeIntegration: true
        }
    })
    
    //webPageChunk
    mainWindow.loadURL(url.format({
        pathname:path.join(__dirname,'launch.html'),
        protocol:'file:',
        slashes:true
        
    }))
    mainWindow.setBackgroundColor('#111111')
      
        ipcMain.on('resize', function(e,x,y) {
                mainWindow.setSize(x,y);
            })

        ipcMain.on('logoutt', function() {
                app.quit();
            })

    mainWindow.on('closed',() =>{
        win = null
    })

})





