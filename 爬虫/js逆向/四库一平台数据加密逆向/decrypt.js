const Crypto = require("E:/js/node_modules/crypto-js");

const m = {sigBytes: 16, words: [808530483, 875902519, 943276354, 1128547654]};
const f = {sigBytes: 16, words: [1785673834, 964118391, 624314466, 2019968622]};

function h(t) {
    var e = Crypto.enc.Hex.parse(t),
        n = Crypto.enc.Base64.stringify(e),
        a = Crypto.AES.decrypt(n, f, {
            iv: m,
            mode: Crypto.mode.CBC,
            padding: Crypto.pad.Pkcs7
        }),
        r = a.toString(Crypto.enc.Utf8);
    return r.toString()
}

