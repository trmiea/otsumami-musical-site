const url = 'https://docs.google.com/spreadsheets/d/10wIqAp99erzJC_SZ6IpCdkxFUMMWPsv5dW6nvXsWOwo/gviz/tq?tqx=out:json&sheet=' + encodeURIComponent('フォームの回答 1');
fetch(url)
  .then(res => res.text())
  .then(text => {
    console.log(text.substring(0, 200));
  })
  .catch(console.error);
