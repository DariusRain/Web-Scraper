const fs = require('fs')

const directoryPath = process.cwd() + '\\all-data';

console.log(directoryPath);
const allJSON = [];

let count = 0;

fs.readdir(directoryPath, function (err, files) {
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    } 
    files.forEach( async (file) => {

        const filePath = process.cwd() + '\\all-data\\' + file;
            
            try {
                const rawTxt = fs.readFileSync(filePath, 'utf-8');
                
                const parsed = JSON.parse(rawTxt);
                if (parsed.bizs === undefined) console.log('caught', file);
                parsed.bizs.forEach(data => {
                    const parsedBiz = JSON.parse(data);
                    allJSON.push(parsedBiz)                 
                });
            } catch (err) {
                console.log(err.message, file);
            }
           
    });
    writeJSONFile(allJSON)

});

function writeJSONFile(jsonArr) {

    const stringified = JSON.stringify(jsonArr)

    fs.writeFileSync('compiledJSON.json', stringified)
}