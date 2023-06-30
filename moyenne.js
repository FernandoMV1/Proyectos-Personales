function Moyenne() {
    let n=parseInt(prompt("nombre de notes"))
    let sommeNote=0
    for (let i = 1; i <= n; i++) {
        let note = parseFloat(prompt('note'+i));
        sommeNotes =+ note;

      }
    let moy = sommeNotes/n  
    document.getElementById("maDiv").innerHTML=moy   
        if  (moy<8)
        {document.getElementById("maDiv").classlist.add("RED")}
        else if (moy<12)
        {document.getElementById("maDiv").classlist.add("JAU")}
        else if (moy<17)
        {document.getElementById("maDiv").classlist.add("BLE")}
        else
        {document.getElementById("maDiv").classlist.add("VER")}
    
}




