
const
  { cwd } = require("process"),
  fs = require("fs"),
  Biz = require("./Biz"),
  isEmpty = require("./isEmpty"),
  { default: validate } = require("validator"),
  stateMapCap = require("./stateMapCap"),
  { getState, allStates } = require('./stateFromZip'),
  firstCharNum = /^[0-9]/,
  nums = /[0-9]/,
  approvedDate = new Date(2020, 2, 2),
  validationCode = 'DARIUS20',
  dataPath = '../../data/scrapedBizsFiltered.json',

  defaultBiz = {
    validationCode: validationCode,
    poster_email: 'gabrielsherman.student@careerdevs.com',
    owner_ethn: "Black (African Decent)",
    business_type: 'Other',
    street_name:' ',
    street_num: ' ',
    zipcode: ' ',
    open_hour: 8,
    close_hour: 17,
    registered: false,
    listed: true,
    isImport: true,
    emailValidated: true,
    approved: {
      active: true,
      userId: null,
      teamId: null,
      timeStamp: approvedDate,
    },
  }

  let tested = false, count = 0;
function importBiz () {


  const rawData = fs.readFileSync( dataPath, 'utf-8');

  const dataArr = JSON.parse(rawData)

  // console.log(dataArr.length);
  const allBizs =  [];
  dataArr.forEach( (biz) => {

    const bizParsedData = parseData(biz);

    if (!bizParsedData) {
      return
    }

    const {name, phone, streetName, city, state, zipcode, about, email, twitter, instagram, facebook, type, categories} = bizParsedData;
    if (validate.isURL(name)) return
    allBizs.push({
      ...defaultBiz,
      business_type: type,
      category: categories,
      name: name,
      owner_email: email, 
      owner_phone: phone,
      twitter: twitter,
      instagram: instagram,
      facebook: facebook,
      street_name: streetName,
      city: city,
      state: state,
      zipcode: zipcode,
      about: about,
      photos: [],
    });  
  })

  // console.log(allBizs.length);

  fs.writeFileSync('allParsedData.json', JSON.stringify(allBizs))

};

function parseData( biz ) {

  const dataObj = {
    phone: '', streetName: '', city: '', state: '', zipcode: '', about: '', email: '', twitter: '', instagram: '', facebook: '', categories: []
  }

  const {city, state, zip, strName} = parseAdd(biz.address) 

  if (parseAdd === false) {
    return false
  } else {
    dataObj.city = city
    dataObj.state = state
    dataObj.zipcode = zip
    dataObj.streetName = strName
  }


  if (biz.description !== undefined && biz.description.trim() !== '') {
    dataObj.about = parseDesc(biz.description)
    // console.log(dataObj.about);
  }

  dataObj.categories = [...biz.categories].filter(cat => cat !== 'Other')

  dataObj.type = biz.name.toLowerCase().includes('inc') || biz.name.toLowerCase().includes('incorporated') ? 'Incorporated' : 'Other';

  dataObj.name = parseName(biz.name)
  

  biz.contact.forEach( info => {

    let cntData = info.data.trim()
    
    switch (info.type) {
      case 'phoneNumber':
        if (cntData.includes('\n')) {
          cntData = cntData.split('\n')[cntData.split('\n').length-1] 
        }
        const tempPhone = parsePhone(cntData);
        if (tempPhone != undefined && validate.isMobilePhone(tempPhone.trim())) {
          dataObj.phone = tempPhone.trim();
        }
        break;
      case 'email':
        if ( validate.isEmail(cntData) ) {
          dataObj.email = cntData
        }  
        break;    
      case 'twitter':
        dataObj.twitter = cntData
        break;
      case 'instagram':
        dataObj.instagram = cntData
        break;    
      case 'facebook':
          dataObj.facebook = cntData
        break;
    }
  });

  return dataObj
}

//title case a string
function titleCase(str) {
  if (str === 'LCC') return str
  return str.substring(0,1).toUpperCase()+str.substring(1, str.length).toLowerCase()
}

function parseName(str) {
    
  let parsedName = str.split(' ');
  
  parsedName = parsedName.map(e => {
      return titleCase(e)
  });

  parsedName = parsedName.join(' ');
  return parsedName
}

function parsePhone(str) {
  let parsedPhone = str
  .toLowerCase()
  .replace(/[a-z]/g, "")
  .replace(/-/g, "")
  .replace(/\+1/g, "")
  .replace(/\(/g, "")
  .replace(/\)/g, "")
  .replace(/ /g, "")
  .replace(/\./g, "");

  parsePhone = 
  parsePhone.length === 11 && parsePhone[0] === 1 
  ? parsePhone.slice(1, parsePhone.length-1) : parsePhone;
  return parsedPhone
}

function parseDesc(str) {
  const r = /[^a-zA-Z.\, ]/g;
  return str.replace(r, '')
}

function parseAdd(str) {

  let
  city,
  state,
  zip, 
  strName;

  const addrArr = str.split(',')

  const stateZip = addrArr[2] !== undefined ? addrArr[2].trim().split(' ') : undefined;

  if (addrArr[1].toLowerCase().includes('floor') && addrArr.length === 4) {
    addrArr[0] = addrArr[0] + addrArr[1]
    addrArr.splice(1, 1) 
  }

  if (addrArr.length === 3) {
    strName = addrArr[0].trim();
    city  = addrArr[1].trim();
    
    // console.log(stateZip[0]); 
    if (stateZip[0].length == '2' && allStates.includes(stateZip[0])) {
  
      state = stateZip[0].trim().toUpperCase()

      if (stateZip[1] != undefined && stateZip[1].length == '5' && validate.isPostalCode(stateZip[1], 'US')) {
       zip = stateZip[1] 
      }    
    } else if (stateZip[0] != undefined && stateZip[0].length == '5' && validate.isPostalCode(stateZip[0], 'US')) {

      zip = stateZip[0]
      state = getState(stateZip[0])

    }
    // console.log(stateZip);
  } else if (addrArr.length === 4 ){//&& addrArr[3].trim().split(' ')[0].length === 2) {
    const zipState = addrArr[3].trim().split(' ')
  
    if (addrArr[1].trim().toLowerCase().includes('suite')) {
  
      if (allStates.includes(zipState[0])) {
        state = zipState[0]
      } else {
        return false
      }
      
      if (zipState[1] != undefined && zipState[1].length == 5 && validate.isPostalCode(zipState[1], 'US')) {
        zip = zipState[1]
      }
    
      strName = addrArr[0].trim() +' '+ addrArr[1].trim();
      city  = addrArr[2].trim();

    } else {
      if (!allStates.includes(zipState[0])) {
        return false
      } else {
        state = zipState[0]
        if (zipState[1] != undefined && zipState[1].length == 5 && validate.isPostalCode(zipState[1], 'US')) {
          zip = zipState[1]
        }  
        city = addrArr[2]
        strName = addrArr[0]
      }
    }
    
  } else if ((addrArr.length === 6 || addrArr.length === 5) && addrArr[2].trim().split(' ')[0].length === 2 && allStates.includes(addrArr[2].trim().split(' ')[0])) {

    strName = addrArr[0].trim();
    city  = addrArr[1].trim();

    state = stateZip[0]

    if (stateZip[1] != undefined && stateZip[1].length == 5 && validate.isPostalCode(stateZip[1], 'US')) {
      zip = stateZip[1]
    }

    if (!allStates.includes(state)) {
      return false
    }
    
  } else {
    return false
  }


  return {
    city, state, zip, strName
  }

}

importBiz()

module.exports = importBiz