let currentPage=0
labelImgId.innerText="0"
labelRate.innerText="30"
btnPage1.addEventListener("click",e=>{
    currentPage=0;
    showPage0()
})
btnPage2.addEventListener("click",e=>{
    currentPage=1;
    showPage1()
})
imageId.addEventListener("change",e=>{
    console.log(e.target.value)
    imgToCompress.src="http://127.0.0.1:5000/getImage?img="+e.target.value
    labelImgId.innerText=e.target.value
})
imageId2.addEventListener("change",e=>{
    imgToClass.src="http://127.0.0.1:5000/getUnseenImage?img="+e.target.value
    labelImgId2.innerText=e.target.value
})
compressionRate.addEventListener("change",e=>{
    labelRate.innerText=e.target.value
})
compressBtn.addEventListener("click",e=>{
    imgResultatCompress.src=`http://127.0.0.1:5000/compressImage?img=${imageId.value}&nbEig=${compressionRate.value}`
})
classify.addEventListener("click",e=>{
    classResult.innerText=""
    var xhr = new XMLHttpRequest();
    fetch("http://127.0.0.1:5000/getClass?img="+imageId2.value).then(function(response) {
        return response.text();
      }).then(e=>{
        classResult.innerText=e
          
      })
    
    
})
function showPage0(){
    imageCompression.style.display="block";
    imgRecognizer.style.display="none";
}
function showPage1(){
    imageCompression.style.display="none";
    imgRecognizer.style.display="block";
}
console.log("hello")