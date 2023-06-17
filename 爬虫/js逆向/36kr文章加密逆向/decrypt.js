const Crypto = require("E:/js/node_modules/crypto-js");

const ne = {'sigBytes':16, 'words': [1701208418, 1667458405, 761411381, 875377763]};

function decrypt(re) {
   return Crypto.AES.decrypt(re, ne, {
        mode: Crypto.mode.ECB,
        padding: Crypto.pad.Pkcs7
    }).toString(Crypto.enc.Utf8).toString()
}