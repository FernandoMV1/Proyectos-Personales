function question1(){
    var reponse=document.f1.foot.value;
    return(reponse=='Arg')
}

function question2(){
    var reponse=document.f1.distance.value;
    return(reponse=="10000")
}

function question3(){
    var invention1=document.f1.sca;
    var invention2=document.f1.tiede;
    var invention3=document.f1.para;
    return((invention1.checked)&&(!invention2.checked)&&(invention3.checked))
}

function question4(){
    var reponse=document.f1.intrus.value;
    return(reponse=="314")
}

function score(){
    let res=0;
    if (question1()) {
        res++;
        alert("question 1: BRAVO !"); 
    }
    if (question2()){
        res++;
        alert("question 2: BRAVO !");
      }
    if (question3()){
        res++;
        alert("question 3: BRAVO !"); 
    }
    if (question4()){
        res++;
        alert("question 4: BRAVO !");
    }
    alert ("votre score est de "+res)
}