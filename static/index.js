window.addEventListener("scroll", function() {showFunction()});

function showFunction(){
  if (document.body.scrollTop > 900 || document.documentElement.scrollTop > 900){
    document.getElementById("card").style.display="block";
  }else{
    document.getElementById("card").style.display="none";
  }
}