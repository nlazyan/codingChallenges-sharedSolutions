const fs = require('fs');
var fileName = process.argv[2];
var fileContent = "";

if(fileName) {
    fileContent = fs.readFileSync(fileName).toString();
    console.log("JSON parse: ", parseJSON(fileContent));
}

function parseJSON(fileContent) {
    fileContent = fileContent.replaceAll(/\s/g,'');
    let json = parseSimpleJSON(fileContent);
    if(json) {
        return json;
    } else {
        return "Invalid JSON"
    } 
}
//step 1 
function parseSimpleJSON(fileContent) {
   if(fileContent === '{}'){
    let json = fileContent;
    return json; 
   } 
    return false;
}
