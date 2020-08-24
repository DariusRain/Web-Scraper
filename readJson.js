const fs = require('fs')
const data = fs.readFileSync('./scraped/bizs-52.json', 'utf-8');

const json = JSON.parse(data);

json.bizs.forEach(elm => {
    obj = JSON.parse(elm)
    console.log(elm);
});