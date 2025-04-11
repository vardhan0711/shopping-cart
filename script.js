var video=document.querySelector("#video-container");
var mov=document.querySelector("#play");

video.addEventListener("mouseenter",function(){
    gsap.to(mov,{
        opactiy:1,
        scale:1
        
    })
})
video.addEventListener("mouseleave",function(){
    gsap.to(mov,{
        opactiy:0,
        scale:0
        
    })
})
video.addEventListener("mousemove",function(dets){
    gsap.to(mov,{
        left:dets.x-60,
        top:dets.y-80
    })
})
// mov.style.background="green";