
document.getElementById("back").addEventListener('click',()=>{
    window.location = "launch.html";

})

const wall = document.getElementById('tab-main')

//fols must be a dynamic array that takes current date and pushes
var fols = ["2020-02-09","2020-02-10","2020-02-11","2020-02-12","2020-02-13"]



var b ="person"

document.getElementById('test').addEventListener('click',()=>{

    for(i=0;i<(5);i++){
        var card='<div class="rep-card">'+'<div class="rep-img" id="bg'+i+'"></div>'+' <div class="rep-text">'+'<div class="rep-title">'+"person"+'</div><div class="details">'+"1"+'</div>'+'</div>'+'</div>'
    wall.insertAdjacentHTML("afterbegin",card);	
    }
})



















