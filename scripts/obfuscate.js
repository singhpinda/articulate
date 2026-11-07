// Scrambles the app's JavaScript so it cannot be read or copied easily from the APK.
const fs = require('fs');
const JO = require('javascript-obfuscator');
const f = 'www/index.html';
let html = fs.readFileSync(f, 'utf8');
const re = /<script>([\s\S]*)<\/script>/;
const m = html.match(re);
if (!m) throw new Error('inline script not found');
const out = JO.obfuscate(m[1], {
  compact: true,
  stringArray: true,
  stringArrayEncoding: ['base64'],
  stringArrayThreshold: 1,
  splitStrings: true,
  splitStringsChunkLength: 6,
  identifierNamesGenerator: 'hexadecimal',
  disableConsoleOutput: true,
  numbersToExpressions: true
}).getObfuscatedCode();
html = html.replace(re, () => '<script>' + out + '</script>');
html = html.replace(/<!--[\s\S]*?-->/g, '');
fs.writeFileSync(f, html);
console.log('obfuscated', out.length, 'bytes');
