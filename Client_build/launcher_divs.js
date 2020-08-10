

const wall = document.getElementById('wall')
const search_but = document.getElementById('search-but')
var i = 0;
var fols = ["2020-02-09","2020-02-10","2020-02-11","2020-02-12","2020-02-13"]
for(i=0;i<fols.length;i++){
var diver= "<div class='bins' id='"+fols[i]+"'>"+fols[i]+"</div>"
wall.insertAdjacentHTML("afterbegin",diver );	
}
var tes = 0;


search_but.addEventListener('click',()=>{
	var a = document.getElementById("search").value //ex:fol3
	tes = tes+1

	for(i=0;i<fols.length;i++){
		if(fols[i].toString().startsWith( a)){
			var b=document.getElementById(fols[i])
			b.style.display = 'block'
		}
		else{
		var b=document.getElementById(fols[i])
		b.style.display = 'none'
		}
	}
		
	//}
})

document.getElementById(fols[0]).addEventListener('click',()=>{
	window.location= "complain.html";
  })

