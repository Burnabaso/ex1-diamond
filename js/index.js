function printDiamonds(rows){
    var row = "";
    for(var i = 1;i <= rows;i++)
    {
        row += " ".repeat(rows-i)+ "*".repeat((2*i)-1) +"\n"
    }
    console.log(row);
}   
(function (){
    // const userInput = prompt("Enter number of rows: ");
    printDiamonds(4);
   
})();