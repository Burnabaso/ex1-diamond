// O(rows),rows being the user input
function printDiamonds(rows){
    var row = "";
    // upper part
    // O(rows), rows being the number of iterations based on input
    for(var i = 1;i <= rows;i++)
    {
        // accumulate rows of upper part in row
        row += " ".repeat(rows-i)+ "*".repeat((2*i)-1) +"\n"
    }
    // lower part
    // O(rows-1), rows being the user input
    for(var i =rows-1;i>0;i--){
        // add the lower part to rows
        row += " ".repeat(rows-i)+ "*".repeat((2*i)-1) +"\n"
    }
    console.log(row);
}   
(function (){
    const userInput = prompt("Enter number of rows: ");
    printDiamonds(userInput);
   
})();