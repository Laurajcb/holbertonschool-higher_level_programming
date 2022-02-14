const $ = window.jQuery;
FrenchHello();

async function FrenchHello () {
  const response = await fetch('https://fourtonfish.com/hellosalut/?lang=fr');
  const result = await response.json();
  const french = result;
  $('DIV#hello').append(french.hello);
}
