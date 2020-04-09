
function Copy(){
    var codepaster = document.getElementById("codepaster");
    var codeholder = document.getElementById("id_code");
    var code = document.getElementById("code").value;
    codepaster.onclick = function(){
       codeholder.value = code;
    }
    
}






