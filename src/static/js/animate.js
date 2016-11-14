function animation(id, effect){
    document.getElementById(id).classList.add(effect);
    setTimeout( function(){
        document.getElementById(id).classList.remove(effect);
    }, 1000);
}